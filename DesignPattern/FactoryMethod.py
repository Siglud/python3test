# coding=utf-8
__author__ = 'Siglud'
#工厂方法模式


class Factory(object):
    def createProduct(self):
        raise SyntaxError


class ConcreteFactoryA(Factory):
    def createProduct(self):
        return ConcreteProductA()


class ConcreteFactoryB(Factory):
    def createProduct(self):
        return ConcreteProductB()


class Product(object):
    def show(self):
        raise SyntaxError


class ConcreteProductA(Product):
    def show(self):
        print('This is ProductA')


class ConcreteProductB(Product):
    def show(self):
        print('This is ProductB')


if __name__ == "__main__":
    factory = ConcreteFactoryA()
    product = factory.createProduct()
    product.show()

    factory = ConcreteFactoryB()
    product = factory.createProduct()
    product.show()