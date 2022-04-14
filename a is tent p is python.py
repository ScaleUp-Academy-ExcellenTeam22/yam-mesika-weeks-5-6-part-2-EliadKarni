"""
The code calculates a list of all the characters between 'a' to 'z' and 'A' to 'Z'.
"""


def get_letters() -> list:
    """
    The function returns a list of all the characters between 'a' to 'z' and 'A' to 'Z'.
    :return: A list of all the characters between 'a' to 'z' and between 'A' to 'Z'.
    """
    return [chr(lower) for lower in range(ord('a'), ord('z') + 1)] \
        + [chr(higher) for higher in range(ord('A'), ord('Z')+1)]


if __name__ == "__main__":
    print(get_letters())
