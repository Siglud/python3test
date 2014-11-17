# coding=utf-8
__author__ = 'Siglud'
#外观模式


class Team(object):
    def __init__(self, name=None):
        self.__name = name

    def operation(self):
        print("%s Working..." % self.__name)


class CodingTeam(Team):
    """编码组"""
    def __init__(self, name="编码组"):
        super(CodingTeam, self).__init__(name)


class DesignTeam(Team):
    """设计组"""
    def __init__(self, name="设计组"):
        super(DesignTeam, self).__init__(name)


class Facade(object):
    def __init__(self):
        self.codingTeam = CodingTeam()
        self.designTeam = DesignTeam()

    def design(self):
        self.designTeam.operation()

    def coding(self):
        self.codingTeam.operation()


if __name__ == "__main__":
    facade = Facade()
    facade.design()
    facade.coding()