"""
The code received a sentence and returns a list of each sentence's word's length.
"""


def words_length(sentence: str) -> list:
    """
    The function receives a sentence and returns a list of each word's length by the sentence order.
    :param sentence: The sentence to calc its words length.
    :return: A list of sentence's words lengths.
    """
    return[len(x) for x in sentence.split(" ")]


if __name__ == "__main__":
    print(words_length(input("please enter your sentence: ")))
