from tornado.ioloop import IOLoop
from tornado import httpclient, gen
from tornado.httpclient import HTTPRequest, HTTPError


class AwaitSimple(object):
    @staticmethod
    async def tornado_req():
        http = httpclient.AsyncHTTPClient()
        req = HTTPRequest('http://www.google.com/', method="GET", connect_timeout=1, request_timeout=1)
        try:
            response = await http.fetch(req)
        except Exception as e:
            print(e)
            return ''
        print('we get body')
        return response.body

    @gen.coroutine
    def get_tornado_req(self):
        result = yield self.tornado_req()
        print(result)
        return result


if __name__ == "__main__":
    # IOLoop.current().spawn_callback(AwaitSimple().get_tornado_req)
    IOLoop.current().run_sync(AwaitSimple().get_tornado_req)
