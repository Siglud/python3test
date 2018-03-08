import asyncio
import json
import uuid
from collections import defaultdict
from functools import lru_cache

import aio_pika
from aio_pika import ExchangeType, IncomingMessage
from aio_pika.message import Message
from tornado import web, websocket, netutil, process
from tornado.httpserver import HTTPServer
from tornado.platform.asyncio import AsyncIOMainLoop


class MQBroker:
    """
    一个Tornado + RabbitMQ实现的聊天服务器样板
    """
    __MQ_EXCHANGE = 'test_talk'
    __SOCKETS = defaultdict(set)

    def __init__(self):
        self.__loop = None
        self.__conn = None  # type: aio_pika.Connection

        self.__key_ch = dict()

    @classmethod
    async def create(cls):
        self = MQBroker()
        self.__conn = await aio_pika.connect_robust("amqp://test:test@192.168.0.11:5672/test",
                                                    loop=asyncio.get_event_loop())
        return self

    @lru_cache(5)
    def __get_exchange(self, key):
        return "{}_{}".format(self.__MQ_EXCHANGE, key)

    async def subscribe(self, key, socket):
        if key not in self.__SOCKETS:
            channel = await self.__conn.channel()
            exchange = await channel.declare_exchange(name=self.__get_exchange(key), type=ExchangeType.FANOUT,
                                                      durable=True, auto_delete=False)
            self.__key_ch[key] = exchange
            queue = await channel.declare_queue(exclusive=True, auto_delete=True)
            await queue.bind(exchange=exchange)
            await queue.consume(self.__on_message, no_ack=True)
        self.__SOCKETS[key].add(socket)

    def __on_message(self, message: IncomingMessage):
        data = json.loads(message.body)
        for socket in self.__SOCKETS[data.get('key')]:
            socket.write_message(message.body)

    async def publish(self, key, data):
        data['key'] = key
        exchange = self.__key_ch[key]  # type: aio_pika.Exchange
        await exchange.publish(Message(json.dumps(data).encode()), routing_key="")

    @classmethod
    def unsubscribe(cls, key, socket):
        if key in cls.__SOCKETS and socket in cls.__SOCKETS[key]:
            cls.__SOCKETS[key].remove(socket)


class IndexHandler(web.RequestHandler):
    async def get(self, *args, **kwargs):
        self.render('index.html')


class ChatHandler(websocket.WebSocketHandler):
    __BROKER = None  # type: MQBroker

    @staticmethod
    async def __get_broker():
        if not ChatHandler.__BROKER:
            ChatHandler.__BROKER = await MQBroker.create()
        return ChatHandler.__BROKER

    async def open(self, *args, **kwargs):
        self.userid = uuid.uuid4()
        broker = await self.__get_broker()
        await broker.subscribe('room1', self)

    def on_close(self):
        self.__BROKER.unsubscribe('room1', self)

    async def on_message(self, message):
        if not message:
            return

        data = json.loads(message)
        data['user'] = self.userid.hex
        broker = await self.__get_broker()
        await broker.publish('room1', data)


if __name__ == '__main__':
    app = web.Application([
        ('^/chat', ChatHandler),
        ('^/', IndexHandler)
    ])

    sockets = netutil.bind_sockets(8000)
    process.fork_processes(0)
    AsyncIOMainLoop().install()
    server = HTTPServer(app)
    server.add_sockets(sockets)
    asyncio.get_event_loop().run_forever()
