"""
The code receives a file path and row. Then, it prints the files content in the received line.
"""


class NotEnoughLines(Exception):
    """
    The exception raised if the wanted line is not exist in the file.
    """
    def __init__(self):
        pass


def get_line_from_file(file_path: str, line_number: int) -> str:
    """
    The function returns the line string in the path's file in the received line.
    If Exception raised, the function print it to the logs/txt file.
    :param file_path: The file's path.
    :param line_number: The wanted line in the file.
    :return: The path's file content in the wanted line.
    """
    try:
        with open(file_path, "r") as file:
            counter = 0
            for line in file:
                counter += 1
                if counter == line_number:
                    return line
        raise NotEnoughLines
    except FileNotFoundError:
        with open("log.txt", "a") as file:
            file.writelines("file not found\n")
    except NotEnoughLines:
        with open("log.txt", "a") as file:
            file.writelines("not enough lines\n")
    except NotEnoughLines:
        with open("log.txt", "a") as file:
            file.writelines("not enough lines\n")


if __name__ == "__main__":
    print(get_line_from_file("Hello.txt", 5))
