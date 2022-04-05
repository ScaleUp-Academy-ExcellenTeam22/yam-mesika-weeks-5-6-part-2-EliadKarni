import re
from os.path import exists
from os import rename
"""
The code finds in each file its chapter name and chapter number.
Then its changes the file's name into it it the syntax of three zfill of the chapter number, and the chapter name.


files exist check: https://www.pythontutorial.net/python-basics/python-check-if-file-exists/ 
files rename: https://stackoverflow.com/questions/2491222/how-to-rename-a-file-using-python
clean special characters from string: https://stackoverflow.com/questions/5843518/remove-all-special-characters-punctuation-and-spaces-from-string
"""

NUM_OF_FILES = 122


def rename_files() -> None:
    """
    The function renames each html file into the syntax: chapter name in three zfill syntax and the chapter name.
    :return: None
    """
    for i in range(NUM_OF_FILES):
        if exists(f"{i}.html"):
            name = get_name(f"{i}.html")
            rename(f"{i}.html", f"{name}.html")


def get_name(file_name: str) -> str:
    """
    The function finds the received file's chapter number and name.
    Then it returns string of the chapter in syntax of: three zfill chapter number and then the chapter name.
    :param file_name: The tested file name.
    :return: The chapter in syntax of: three zfill chapter number and then the chapter name.
    """
    with open(file_name, 'r') as reader:
        for line in reader:
            if re.search("<title>.*</title>", line):
                chapter_no = re.findall("Chapter [^:]*:", line)[0][len("Chapter "): -1].zfill(3)
                chapter_name = re.findall(": .*</title>", line)[0][len(": "): -len("</title>")]
                return re.sub(r'\W+', " ", chapter_no + " " + chapter_name)


if __name__ == '__main__':
    rename_files()
