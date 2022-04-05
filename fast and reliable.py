import time
from typing import Iterable
"""
The code receive words from FILE_NAME file into set and list.
Then, it search for a word which is "zwitterion" 1000 times in each of them, and print each one's
the avg search time.
"""

FILE_NAME = "words.txt"


def get_words_set() -> set:
    """
    The function returns a set that contains all the word if FILE_NAME file.
    :return: Set that contains all the word if FILE_NAME file.
    """
    ans = set()
    with open(FILE_NAME, 'r') as reader:
        for line in reader:
            ans.add(line)
    return ans


def get_words_list() -> list:
    """
    The function returns a list that contains all the word if FILE_NAME file.
    :return: List that contains all the word if FILE_NAME file.
    """
    return [line for line in open(FILE_NAME, 'r')]


def average_runtime(words_list: list, words_set: set, runtimes: int = 1000, searched_word: str = "zwitterion") -> None:
    """
    The function searches runtimes' value times the searched_word in the received set and list,
    and prints each one's avg search time.
    :param words_list: List of words.
    :param words_set: Set of words.
    :param runtimes: The amount of searches.
    :param searched_word: The searched word.
    :return: None
    """
    set_times = []
    list_times = []
    for i in range(runtimes):
        set_times.append(finding_time(words_set, searched_word))
        list_times.append(finding_time(words_list, searched_word))

    print(f"list avg runtime: {sum(list_times) / runtimes}")
    print(f"set avg runtime: {sum(set_times) / runtimes}")


def finding_time(iterable: Iterable, searched_word: str) -> float:
    """
    The function searches the received searched_word at the received iterable, and returns the search time.
    :param iterable: Tested iterable.
    :param searched_word: The word needed to be searched in the iterable.
    :return: The search time.
    """
    start_time = time.time()
    searched_word in iterable
    return time.time() - start_time


if __name__ == "__main__":
    average_runtime(get_words_list(), get_words_set())
