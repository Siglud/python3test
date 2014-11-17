# coding=utf-8
__author__ = 'Siglud'
#状态模式


class State(object):
    def write(self, w):
        raise SyntaxError


class NoneState(State):
    def write(self, w):
        if w.getHour() < 12:
            print("当前时间为: %d, 写程序中..." % w.getHour())
        else:
            w.setState(AfterState())
            w.write()


class AfterState(State):
    def write(self, w):
        if w.getHour() < 14:
            print("当前时间为: %d, 吃午饭中..." % w.getHour())
        else:
            w.setState(EveningState())
            w.write()


class EveningState(State):
    def write(self, w):
        if w.getFinish():
            print("当前时间为: %d, 睡觉..." % w.getHour())
        else:
            print("当前时间为: %d, 加班..." % w.getHour())


class Work(object):
    def __init__(self):
        self.__hour = None
        self.__state = NoneState()
        self.__finish = False

    def getHour(self):
        return self.__hour

    def setHour(self, hour):
        self.__hour = hour

    def setState(self, state):
        self.__state = state

    def getFinish(self):
        return self.__finish

    def write(self):
        self.__state.write(self)


if __name__ == "__main__":
    work = Work()
    work.setHour(10)
    work.write()

    work.setHour(15)
    work.write()