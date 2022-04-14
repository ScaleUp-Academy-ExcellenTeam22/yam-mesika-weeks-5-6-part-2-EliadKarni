from typing import Callable
from time import time
from time import sleep
"""
The code runs a function which run the received function and returns its run time.
"""


def timer(func: Callable, *args) -> float:
    """
    The function run the received function and returns its run time.
    :param func: The tested function.
    :param args: The function's arguments.
    :return: The function's run time.
    """
    start_time = time()
    func(*args)
    return time() - start_time


if __name__ == "__main__":
    print(timer(sleep, 20))
