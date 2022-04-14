"""
The code receives a list of first, a list of last names and the minimum full name length if wanted (0 by default).
Then, the code returns all the possible full names combinations which their length is not lower then the received
minimum length.
"""


def full_names(f_names: list, l_names: list, min_len: int = 0) -> list:
    """
    The function receives a list of first names and last names. Then it returns each possible combination
    of values between first name and last name value that its combination length is not lower then the
    min_len value that is 0 by default.
    :param f_names: List of first names.
    :param l_names:List of last names.
    :param min_len: Minimum full name length.
    :return: Every possible combination of full name that its length is no lower then min_len value.
    """
    return [first + " " + last for first in f_names for last in l_names if len(first + last) + 1 >= min_len]


if __name__ == "__main__":
    print(full_names(input("please enter first names: ").split(" "), input("please enter last names: ").split(" ")))
