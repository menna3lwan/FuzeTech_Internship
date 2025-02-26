from user import User

class Admin(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    def delete_message(self, user, message):
        if message in user.inbox:
            user.inbox.remove(message)
            print(f"Message from {message.sender.username} to {user.username} deleted.")
        else:
            print("Message not found in user's inbox.")

    def delete_user(self, chat_app, user):
        if user in chat_app.users:
            chat_app.users.remove(user)
            print(f"User {user.username} deleted.")
        else:
            print("User not found in the system.")