from typing import TypeVar, Iterable, Tuple, Callable, Set, Mapping, Sequence


# 最简朴的
def greeting(name: str) -> str:
    return 'Hello' + name

# 预定义的
Url = str


def retry(url: Url, retry_count: int) -> Url:
    return '{}?retry={}'.format(url, retry_count)


T = TypeVar('T', int, float, complex)  # Must be int  float or complex
Vector = Iterable[Tuple[T, T]]


def inproduct(v: Vector) -> T:
    return sum(x * y for x, y in v)


# 传递可执行变量
def feeder(get_next_item: Callable[[int, str], str]) -> None:
    get_next_item('a', 1)


# 传递无视参数的可执行变量
def partial(func: Callable[..., str], *args) -> Callable[..., str]:
    return lambda x: x + func('bbb')


# 泛型
class Employee(object):
    def __init__(self, name, number):
        self.name = name
        self.number = number


def notify_by_email(employees: Set[Employee], overrides: Mapping[str, str]) -> None:
    for e in employees:
        e.number += 1
    for key, value in overrides:
        if key == 'str':
            value += ',ok'


T = TypeVar('T')


def first(l: Sequence[T]) -> T:
    return l[0]


if __name__ == '__main__':
    print(greeting(1))
    print(greeting('Siglud'))
