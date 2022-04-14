"""
The code is a function which receive integer numbers from the user, and return all the received positive numbers.
"""


def get_positive_numbers() -> None:
    """
    The function receives from the user integer numbers and returns a list of that's positive values.
    :return: List of The user's positive numbers.
    """
    user_values = [int(x) for x in input("please enter integer numbers separated by commas: ").split(",")]
    return list(filter(lambda x: x > 0, user_values))


if __name__ == "__main__":
    print(get_positive_numbers())
