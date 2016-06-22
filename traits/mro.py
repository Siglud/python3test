class E(object):
    def lets_try(self):
        print('E try')


class A(E):
    def lets_try(self):
        print('A try')
        super().lets_try()


class B(object):
    def lets_try(self):
        print('B try')
        super().lets_try()


class C(E):
    def lets_try(self):
        print('C try')


class MroTest(A, B, C):
    """
    探索Python的MRO逻辑
    其继承顺序满足两点：
    1.在继承树树中左边的优先
    2.在继承图中，从入口类开始依次从图中拿掉派生的类为空的类就是最后的继承顺序

    运行super()的方式与MRO的顺序完全相同，
    哪怕是MIXIN类自身无此方法最后使用MIXIN的类依然能够正确的调用到其父节点的对应方法
    """
    def lets_try(self):
        super().lets_try()


if __name__ == '__main__':
    print(MroTest.__mro__)
    a = MroTest()
    a.lets_try()
