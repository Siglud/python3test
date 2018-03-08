import logging

import time
from tornado import ioloop
from tornado.ioloop import PeriodicCallback
from tornado.websocket import websocket_connect


class Client(object):
    """
    聊天服务器测试工具
    """
    def __init__(self, url, io_loop: ioloop.IOLoop, listener=1):
        self.__url = url
        self.__io_loop = io_loop
        self.__ws = None
        self.__listener = listener

    def start_test(self):
        PeriodicCallback(self.__sending, 3_000, io_loop=self.__io_loop).start()
        self.__io_loop.start()

    async def __connect(self):
        try:
            self.__ws = await websocket_connect(self.__url, on_message_callback=self.__on_message_callback)
        except Exception as e:
            logging.error("connection error at ", exec_info=True)
            raise e
        if self.__listener > 1:
            for i in range(1, self.__listener):
                await websocket_connect(self.__url, on_message_callback=self.__on_message_callback)

    def __on_message_callback(self, msg):
        if msg is None:
            logging.info("connection closed")
            self.__ws = None
        else:
            print("msg: {} received at {}".format(msg, time.time()))

    async def __sending(self):
        if self.__ws is None:
            await self.__connect()
        else:
            self.__ws.write_message('{"message": "Time ticking in %s"}' % time.time())


if __name__ == "__main__":
    client = Client("ws://localhost:8000/chat", ioloop.IOLoop.instance(), 20)
    client.start_test()
