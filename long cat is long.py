"""
The code receives a sentence from the user, and returns a dictionary which contains each of the sentence's words as keys
and its lengths as values.
"""


def count_words(sentence: str) -> dict:
    """
    The function receives a sentence string, and returns a map which contains its
    the word as keys and their length as values.
    :param sentence: The values sentence
    :return: A dictionary which contains each of the sentence's words as keys and their length as a values.
    """
    return {word: len(word) for word in ["".join(c for c in x if c.isalnum()) for x in sentence.split(" ")]}


if __name__ == '__main__':
    print(count_words(input("please enter your sentence: ")))
