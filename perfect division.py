from math import isqrt
from typing import Iterator
"""
The code calculates and prints all the perfect numbers it founds.

Websites I used for help:
perfect number formula: https://en.wikipedia.org/wiki/Perfect_number
"""


def get_perfect_number() -> Iterator[int]:
    """
    The function is a perfect numbers generator.
    It finds the next perfect number by Euclid Euler's rule.
    :return: Next perfect number any iteration.
    """
    power = 0
    while True:
        if is_prime(2**power - 1):
            yield 2**(power - 1) * (2**power - 1)
        power += 1


def is_prime(number: int) -> bool:
    """
    The function checks if the received number is prime.
    :param number: Tested number.
    :return: If the tested number is prime.
    """
    if number > 1:
        for i in range(2, isqrt(number) + 1):
            if not number % i:
                return False
        return True
    return False


if __name__ == '__main__':
    for p_number in get_perfect_number():
        print(p_number)
