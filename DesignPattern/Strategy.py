# coding=utf-8
__author__ = 'Siglud'
#策略


class Strategy(object):
    """策略模式"""
    def algorithmInterface(self):
        raise SyntaxError


class ConcreteStrategyA(Strategy):
    """具体策略A"""
    def algorithmInterface(self):
        print("Plan A")


class ConcreteStrategyB(Strategy):
    """具体策略B"""
    def algorithmInterface(self):
        print("Plan B")


class Context(object):
    """环境角色"""
    def __init__(self, strategy):
        self.__strategy = strategy

    def contextInterface(self):
        self.__strategy.algorithmInterface()


if __name__ == "__main__":
    strategyA = ConcreteStrategyA()
    context = Context(strategyA)
    context.contextInterface()

    strategyB = ConcreteStrategyB()
    context = Context(strategyB)
    context.contextInterface()