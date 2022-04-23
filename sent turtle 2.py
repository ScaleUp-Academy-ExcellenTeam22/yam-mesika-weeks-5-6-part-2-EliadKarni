
"""
The code is simulates a PostOffice which allows users to mail each other.
"""


class Message:
    def __init__(self, id, title, body, sender):
        """The ctor creates a new Message object.

        :param int id: The message id.
        :param str title: The message title.
        :param body: The message body.
        :param sender: The message title.
        """
        self.id = id
        self.title = title
        self.body = body
        self.sender = sender
        self.read = False

    def __str__(self):
        """The method returns the message content as a string in a readable syntax.

        :return str: The Message content.
        """
        return "Sent by: " + self.sender + "\nTitle: " + self.title + "\n\n" + self.body

    def __repr__(self):
        """The method returns the message content as a string in a readable syntax for print.

        :return str: The Message content.
        """
        return self.__str__()

    def __len__(self):
        """The method returns the message length.

        :return int: The message length.
        """
        return len(self.body)


class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.
    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, title: str, message_body, urgent=False):
        """Send a message to a recipient.
        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str title: The title of the message.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = Message(self.message_id, title, message_body, sender)
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, num_of_messages=None):
        """Gets a list of the first num_of_messages in the username box value,
         which wasn't marked as read, and marks them as read.
        :param str username: The user's username.
        :param num_of_messages: The amount of messages wants to be read.
        :return: A list of messages wanted to be read.
        :rtype: list.
        :raises KeyError: If the username does not exist.
        """
        ls = []
        counter = 0
        for message in self.boxes[username]:
            if num_of_messages is None or num_of_messages > counter:
                if not message.read:
                    message.read = True
                    counter += 1
                    ls.append(message)
            else:
                break
        return ls

    def search_inbox(self, username, text):
        """Return a list of all the messages in the usernames box which text value appears in its title or body.
        :param str username: Searching the username.
        :param str text: The searched value in the box.
        :return: A list of all the messages in username's inbox which text appears in its body or title.
        :rtype: list
        :raises KeyError: if the username does not exist.
        """
        return [message for message in self.boxes[username] if text in message.body or text in message.title]


if __name__ == "__main__":
    post_office = PostOffice(["Eliad", "Bob", "Michal", "Caspi"])
    post_office.send_message(sender="Eliad", recipient="Michal", title="How are you?",
                             message_body="Tell me how are you?")
    post_office.send_message(sender="Michal", recipient="Bob", title="Tell him to tell",
                             message_body="Tell Caspi to tell Eliad I'm fine.")
    post_office.send_message(sender="Bob", recipient="Caspi", title="Tell him to tell",
                             message_body="Tell tell Eliad that Michal is fine.")
    post_office.send_message(sender="Bob", recipient="Eliad", title="She is fine",
                             message_body="Michal is fine.")
    post_office.send_message(sender="Eliad", recipient="Michal", title="Why",
                             message_body="Why do Caspi need to tell me your fine?")
    post_office.send_message(sender="Eliad", recipient="Michal", title="Tell me!",
                             message_body="Tell me Now!")
    post_office.send_message(sender="Eliad", recipient="Michal", title="Tell me!",
                             message_body="Tell me Now!2")
    print(post_office.read_inbox("Michal", 1))
    post_office.send_message(sender="Eliad", recipient="Michal", title="Tell me!",
                             message_body="Tell me Now!3", urgent=True)
    print(post_office.read_inbox("Michal"))
    print(post_office.search_inbox('Michal', "Tel"))
    

