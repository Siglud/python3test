import types


class FuncDescriptorMixin:
    """
    实现了函数存储的类混合
    """
    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


class DecoratorWithoutParameter(FuncDescriptorMixin):
    """
    不带参数的装饰器本体，实现描述器协议，可独立使用
    """
    def __init__(self, fun, outer=None):
        """
        初始化一个装饰器
        :param fun: 输入函数
        :param outer: 外层输入数据
        """
        self.__fun = fun
        self.__outer = outer

    def __call__(self, *args, **kwargs):
        """
        函数调用
        :param args: 函数的原始输入参数
        :param kwargs: 同上
        :return:
        """
        if self.__outer:
            print(self.__outer.input_args)
        print(self.__fun.__name__)
        print(self.__fun.__doc__)
        self.__fun(*args, **kwargs)
        print('end')


class Decorator(FuncDescriptorMixin):
    """
    带参数的装饰器本体
    """
    def __init__(self, *args, **kwargs):
        self.input_args = args
        self.input_kwargs = kwargs

    def __call__(self, func):
        return DecoratorWithoutParameter(func, self)


@Decorator(2)
def use_this():
    print("this")


class Tester:
    def __init__(self):
        self.__this = "HOHO"

    @Decorator(3)
    def print_hoho(self):
        """
        do print hoho
        :return:
        """
        print(self.__this)

    @DecoratorWithoutParameter
    def print_haha(self):
        """
        do print haha
        :return:
        """
        print("haha")


if __name__ == '__main__':
    t = Tester()
    t.print_hoho()
    t.print_haha()
