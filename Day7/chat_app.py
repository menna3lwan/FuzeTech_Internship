from user import User
from admin import Admin

class ChatApp:
    def __init__(self):
        self.users = []

    def register_user(self, username, email=None, role='user'):
        if role == 'admin':
            user = Admin(username, email)
        else:
            user = User(username, email)
        self.users.append(user)
        return user

    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None