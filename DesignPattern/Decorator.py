# coding=utf-8
__author__ = 'Siglud'
#装饰模式


class Person(object):
    """装饰主体"""
    def __init__(self, name):
        self.__name = name

    def show(self):
        print("装饰的%s" % self.__name)


class Finery(Person):
    """服饰类"""
    def __init__(self):
        self.component = None

    def decorate(self, component):
        self.component = component

    def show(self):
        if self.component is not None:
            self.component.show()


class TShirts(Finery):
    """衬衣"""
    def show(self):
        print("T恤")
        self.component.show()


class BigTrouser(Finery):
    """垮裤"""
    def show(self):
        print("垮裤")
        self.component.show()

if __name__ == "__main__":
    person = Person("新人")
    TShirts = TShirts()
    bigTrouser = BigTrouser()
    TShirts.decorate(person)
    bigTrouser.decorate(TShirts)
    bigTrouser.show()