# coding=utf-8
__author__ = 'Siglud'
#代理模式


class Subject(object):
    def request(self):
        pass


class RealSubject(Subject):
    def request(self):
        print("Real Request")


class Proxy(Subject):
    def __init__(self, realSubject=None):
        self.realSubject = realSubject

    def setRealSubject(self, subject):
        self.realSubject = subject

    def request(self):
        if self.realSubject is None:
            self.realSubject = RealSubject()
        self.realSubject.request()


if __name__ == "__main__":
    agent = Proxy()
    agent.request()
