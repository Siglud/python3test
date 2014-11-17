# coding=utf-8
__author__ = 'Siglud'
#适配器模式


class Worker(object):
    def __init__(self, name):
        self.name = name

    def working(self):
        raise SyntaxError


class ArtWorker(Worker):
    def working(self):
        print("%s is working" % self.name)


class Painter(Worker):
    def working(self):
        print("%s is painting" % self.name)


class ForeignWorker(Worker):
    def doing(self):
        print("%s is working" % self.name)


class Translator(Worker):
    def __init__(self, name):
        super().__init__(name)
        self.foreignWorker = ForeignWorker(name)

    def working(self):
        self.foreignWorker.doing()


if __name__ == "__main__":
    a = ArtWorker("aaa")
    b = Painter("bbb")
    c = Translator("ccc")

    a.working()
    b.working()
    c.working()
