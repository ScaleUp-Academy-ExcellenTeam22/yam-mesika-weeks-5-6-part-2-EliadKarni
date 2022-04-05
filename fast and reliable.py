import time


FILE_NAME = "words.txt"


def get_words_set() -> set:
    ans = set()
    with open(FILE_NAME, 'r') as reader:
        for line in reader:
            ans.add(line)
    return ans


def get_words_list() -> list:
    return [line for line in open(FILE_NAME, 'r')]


def average_runtime(words_list: list, words_set: set, runtimes: int = 1000, searched_word: str = "zwitterion") -> None:
    set_times = []
    list_times = []
    for i in range(runtimes):
        set_times.append(finding_time(words_set, searched_word))
        list_times.append(finding_time(words_list, searched_word))

    print(f"list avg runtime: {sum(list_times) / runtimes}")
    print(f"set avg runtime: {sum(set_times) / runtimes}")


def finding_time(iterable, searched_word) -> float:
    start_time = time.time()
    searched_word in iterable
    return time.time() - start_time


if __name__ == "__main__":
    average_runtime(get_words_list(), get_words_set())
