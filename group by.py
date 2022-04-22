from typing import Iterable
from typing import Callable
"""
The code receives a function and iterable as parameters. Then, it returns a dictionary which contains
the iterable's contents return values as keys and list of the iterable values that its return value
is the key as a value.
    
"""


def group_by(func: Callable, it: Iterable) -> dict:
    """
    The function receives a function and iterable. Then, it returns a dictionary which contains
    the function's iterable's contents' return values as keys, and a list of the iterable values
    :param func: The function checked.
    :param it: The Iterable of the parameters.
    :return: Dict that contains the parameter's return value as a key, and a list of the iterable values
             that its return value is the key.
    """
    ans = {}
    for value in it:
        if func(value) in ans:
            ans[func(value)].append(value)
        else:
            ans[func(value)] = [value]
    return ans


if __name__ == "__main__":
    print(group_by(len, ['aaa', 'bbb', 'a', 'www', '123']))
