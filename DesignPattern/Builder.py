# coding=utf-8
__author__ = 'Siglud'
#建造者模式


class Product(object):
    def __init__(self):
        self.log = list()

    def add(self, string):
        self.log.append(string)
        return

    def getLog(self):
        return self.log


class Builder(object):
    def BuilderPart(self):
        raise SyntaxError


class ConcreteBuilderA(Builder):
    def __init__(self):
        self.product = Product()

    def addBody(self):
        self.product.add("add body from builder A")

    def addCase(self):
        self.product.add("add case from builder A")

    def check(self):
        self.product.add("check done from builder A")

    def BuilderPart(self):
        self.addBody()
        self.addCase()
        self.check()

    def getResult(self):
        return self.product


class ConcreteBuilderB(Builder):
    def __init__(self):
        self.product = Product()

    def addBody(self):
        self.product.add("add body from builder B")

    def addCase(self):
        self.product.add("add case from builder B")

    def check(self):
        self.product.add("check done from builder B")

    def BuilderPart(self):
        self.addBody()
        self.addCase()
        self.check()

    def getResult(self):
        return self.product


class Director(object):
    def __init__(self):
        self.builder = Builder()

    def Construct(self, builder):
        self.builder = builder
        self.builder.BuilderPart()


if __name__ == "__main__":
    builder = ConcreteBuilderA()
    director = Director()

    director.Construct(builder)
    product = builder.getResult()

    log = product.getLog()
    for i in log:
        print(i)