from typing import Iterator
from itertools import chain
from itertools import zip_longest
"""
The both functions receives a list of iterables.
The function interleave, returns a list of all the iterables values sorted by their indexes.
The function interleave_generator is generator which its values as interleave.


Websites I used for help:
zio_chain: https://www.geeksforgeeks.org/python-itertools-chain/
zip_longest: https://www.geeksforgeeks.org/python-itertools-zip_longest/
The logic behind the functions: https://docs.python.org/3/library/itertools.html
"""


def interleave(*args: tuple) -> list:
    """
    The function returns a list of the received iterable values,
    sorted by their indexes at their iterable.
    :param args: Iterables values.
    :return: List of the received values sorted by their previous indexes.
    """
    return [x for x in chain.from_iterable(zip_longest(*args)) if x is not None]


def interleave_generator(*args: tuple) -> Iterator[any]:
    """
    The function is a generator which returns the received
    sorted by their indexes at their iterable.
    Note: The function don't use zip_longest because it returns a data
          struct that can be very big, which violates the generator logic.
    :param args: Iterables values.
    :return: List of the received values sorted by their previous indexes.
    """
    lst = [iter(x) for x in args]
    while lst:
        for iterator in lst:
            try:
                yield next(iterator)
            except StopIteration:
                lst.remove(iterator)


if __name__ == '__main__':
    print(interleave([1, 2, [5, 5, 6]], '12388', {7, 8, 9}, {0: 123, 123: 888}))
    for i in interleave_generator([1, 2, [5, 5, 6]], '12388', {7, 8, 9}, {0: 123, 123: 888}):
        print(i)
