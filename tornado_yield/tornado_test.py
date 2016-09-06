from functools import partial

import tornado.ioloop
import tornado.web
from tornado import gen
from tornado.httpclient import AsyncHTTPClient, HTTPRequest


class RequestSimple(object):

    @classmethod
    def currying_get_baidu(cls):
        return partial(cls.get_baidu, from_name='currying')

    @classmethod
    @gen.coroutine
    def get_baidu(cls, request, from_name=None):
        http = AsyncHTTPClient()
        print('request to baidu from {}'.format(from_name))
        request = yield http.fetch(request)
        print('request to baidu done!')
        raise gen.Return(request.body)

    @classmethod
    def get_baidu_proxy(cls):
        print('before request!')
        request = HTTPRequest('http://www.baidu.com')
        print('after request!')
        return cls.get_baidu(request)

    @classmethod
    def get_baidu_proxy_currying(cls):
        print('before request!')
        request = HTTPRequest('http://www.baidu.com')
        print('after request!')
        return cls.currying_get_baidu()(request)

    @classmethod
    def get_baidu_proxy_v35(cls):
        request = HTTPRequest('http://www.baidu.com')
        return cls.get_baidu_v35(request)

    @classmethod
    async def get_baidu_v35(cls, request):
        http = AsyncHTTPClient()
        print('request to baidu')
        request = await http.fetch(request)
        print('request to baidu done!')
        return request.body


class MainHandler(tornado.web.RequestHandler):

    @gen.coroutine
    def get(self, *args, **kwargs):
        c = yield RequestSimple.get_baidu_proxy()
        self.write(c)


class CurryingHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        c = yield RequestSimple.get_baidu_proxy_currying()
        self.write(c)


class OtherHandler(tornado.web.RequestHandler):
    async def get(self, *args, **kwargs):
        ho = RequestSimple()
        c = await ho.get_baidu_proxy_v35()
        self.write(c)


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/aaa', OtherHandler),
        (r'/bbb', CurryingHandler)
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
