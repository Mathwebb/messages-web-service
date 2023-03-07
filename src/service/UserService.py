from Repository.MessagesRepository import MessagesRepository
from Repository.UsersRepository import UsersRepository

class UserService:
    def __init__(self, message_repository, user_repository):
        self.message_repository: MessagesRepository = message_repository
        self.user_repository: UsersRepository = user_repository

    def get_users(self):
        users = self.user_repository.get_users()
        return users
    
    def get_user(self, id):
        user = self.user_repository.get_user(id)
        user = {'id': user[0], 'name': user[1], 'email': user[2]}
        return user
    
    def get_user_by_email(self, email):
        user = self.user_repository.get_user_by_email(email)
        user = {'id': user[0], 'name': user[1], 'email': user[2]}
        return user
    
    def add_user(self, name, email):
        user = self.user_repository.insert_user(name, email)
        return user
