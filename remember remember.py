import cv2
import numpy as np
"""
The code receives a picture's path, and returns the encoded message in it.

The websites help I used:
To get the black pixels coordinates list:

"""


def decode_picture(file_path: str) -> str:
    """
    The function receives a picture's path, and return the encoded message in the picture.
    :param file_path: The picture's path.
    :return: The message encoded in the picture.
    """
    greyed_picture = cv2.cvtColor(cv2.imread(file_path), cv2.COLOR_BGR2GRAY)
    coordinates = sorted(np.column_stack(np.where(greyed_picture == 1)), key=lambda x: x[1])
    return "".join([chr(row) for row, col in coordinates])


if __name__ == "__main__":
    print(decode_picture("code.png"))
