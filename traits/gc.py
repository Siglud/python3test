import gc

# 这段代码在Python2与Python3.5中的表现不同
# 展示了Python3.5在内存回收方面的改进


class A(object):
    def __del__(self):
        pass


class B(object):
    def __del__(self):
        pass

gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_LEAK)
a = A()
b = B()
a.b = b
b.a = a
del a
del b
gc.collect()

