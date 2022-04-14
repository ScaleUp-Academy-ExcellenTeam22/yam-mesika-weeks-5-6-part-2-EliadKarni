from typing import Iterable
from  typing import Callable
"""
Customized Filter:
The code is a filter like function.

used the web help:
Callable typing: https://stackoverflow.com/questions/37835179/how-can-i-specify-Callable-function-type-in-my-type-hints
"""


def my_filter(func: Callable, iterable: Iterable) -> Iterable:
    """
    The generator returns values that as a func parameters makes it return True value
    or a value equals to it.
    :param func: The function which the generator use to filter the iterable.
    :param iterable: Filtered iterable.
    :return: Yielding the iterable's members that as func parameter returns True value like.
    """
    for value in iterable:
        if func(value):
            yield value


if __name__ == "__main__":
    ls = [x for x in range(100)]
    print(list(my_filter(lambda x: x % 2 == 0, ls)))
    print(list(filter(lambda x: x % 2 == 0, ls)))
