from datetime import datetime
"""
The code receives a file path and row. Then, it returns the file's content in the received line.
If exception raised, The code write it on the logs file with time stamp.
"""


class NotEnoughLines(Exception):
    """
    The exception raised if the wanted line is not exist in the file.
    """
    def __init__(self):
        pass

    def __str__(self):
        return "Not enough lines in the file."


def print_error_to_logs(error: Exception) -> None:
    """
    The function prints the received error to the logs file with time stamp
    :param error: The raised exception.
    :return: None.
    """
    with open("logs.txt", "a") as file:
        file.write(f"Time: {datetime.now()}, Error: {str(error)}\n")


def get_line_from_file(file_path: str, line_number: int) -> str:
    """
    The function returns the line string in the path's file in the received line.
    If Exception raised, the function print it to the logs/txt file.
    :param file_path: The file's path.
    :param line_number: The wanted line in the file.
    :return: The path's file content in the wanted line.
    """
    try:
        if type(line_number) != int:
            raise TypeError("Line number type is not str.")
        if line_number <= 0:
            raise ValueError("Illegal line number value.")
        with open(file_path, "r") as file:
            counter = 0
            for line in file:
                counter += 1
                if counter == line_number:
                    return line
        raise NotEnoughLines
    except (FileNotFoundError, NotEnoughLines, ValueError, TypeError) as error:
        print_error_to_logs(error)


if __name__ == "__main__":
    print(get_line_from_file("Hello.txt", 1))
