"""
The code simulate a file system management.
"""


class File:
    """
    The class is a file simulation.
    """
    def __init__(self, name: str, creator: str, content):
        """
        The ctor creates a file.
        :param name: The file name.
        :param creator: The file's creator's username.
        """
        self.name = name
        self.creator = creator
        self.content = content


class Directory(File):
    """
    The class simulates a directory file.
    """
    def __init__(self, name: str, creator: str, content: list):
        """
        ctor of the directory.
        :param name: The directory name.
        :param creator: The file creator's username.
        :param content: The directory content.
        """
        super().__init__(name, creator, content)

    def open_file(self, path: list, username: str, admin: bool = False) -> str:
        """
        The function returns the path's file's content.
        If no file exist in the path, or there is no  there is no return value.
        :param path: The path to the file.
        :param username: The user name.
        :param admin: If the reading user is an admin.
        :return: The file's content.
        """
        if path[0] == self.name:
            for file in self.content:
                if file.name == path[1]:
                    if len(path) == 2:
                        return file.read(username, admin)
                    else:
                        return file.openfile(path[1:], username, admin)


class ReadableFile(File):
    """
    The class simulates a file that contains content.
    """
    def __init__(self, name: str, creator: str, content: str):
        """
        Ctor of a Readable file.
        :param name: The file name.
        :param creator: The file creator.
        :param content: The file's content.
        """
        super().__init__(name, creator, content)
        self.size = len(self.content.encode('utf-8'))

    def read(self, username, admin=False) -> str:
        """
        The method returns the file's content if the reader has the permission for that.
        :param username: The reader username.
        :param admin: If the reader is an admin.
        :return: The file's content if the user had the reading permission, None else.
        """
        if username == self.creator or admin:
            return self.content


class BinaryFile(ReadableFile):
    """
    The class simulates a binary file.
    """
    def __init__(self, name, creator, content):
        super().__init__(name, creator, content)

    def get_dimensions(self) -> str:
        """
        The method simulates a dimensions prints of a picture file.
        :return: The picture dimensions.
        """
        if self.name[-4] == ".jpg":
            return "rows: y\ncols: x"


class TextualFile(ReadableFile):
    """
    The class simulates a text file.
    """
    def __init__(self, name, creator, content):
        super().__init__(name, creator, content)

    def count(self, text: str) -> int:
        """
        The method returns how many times the text appears in the file's content.
        :param text:
        :return:
        """
        return self.content.count(text)


class UserSystem:
    """
    The class simulates a users manager.
    """
    def __init__(self, users, files):
        self.users = users
        self.files = files

    def read(self, path, username, password) -> str:
        """
        The method returns the path's file content if exist, if the reader's user has the permissions to read the file
        and if the password parameter is the user's password.
        :param path: The file's path.
        :param username: The reader username.
        :param password: The user password.
        :return: The path's file content if exist, if the reader has the right permission as reader and if the
                 password parameter's value is equals to the username's password.
        """
        if self.users[username]["password"] == password:
            return self.files.open_file(path.split("/"), username, self.users[username]["admin"])


if __name__ == "__main__":
    system = UserSystem({
        "root": {"admin": True, "password": "I am root"},
        "Eliad": {"admin": True, "password": "Eliad"},
        "Ehud": {"admin": False, "password": ""},
        "Dvora": {"admin": False, "password": ""},
        "Dvir": {"admin": False, "password": ""},
        "Bob": {"admin": False, "password": ""}
    }, Directory(name="root", creator="root", content=[
        TextualFile(name="text.txt", creator="Ehud", content="This is Ehud file."),
        BinaryFile(name="idk.pnj", creator="Dvir", content="1011010100101011101010101010001010")
    ]))
    print(system.read("root/text.txt", "Ehud", "123"))
    print(system.read("root/text.txt", "Ehud", ""))
    print(system.read("root/text.txt", "Eliad", ""))
    print(system.read("root/text.txt", "Eliad", "Eliad"))
