from message import Message

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.inbox = []

    def send_message(self, recipient, content):
        message = Message(self, recipient, content)
        recipient.receive_message(message)

    def receive_message(self, message):
        self.inbox.append(message)

    def view_inbox(self):
        for message in self.inbox:
            print(f"From: {message.sender.username}, Content: {message.content}, Timestamp: {message.timestamp}")