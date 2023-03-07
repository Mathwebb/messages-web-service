from Repository.MessagesRepository import MessagesRepository
from Repository.UsersRepository import UsersRepository

class MessageService:
    def __init__(self, message_repository, user_repository):
        self.message_repository: MessagesRepository = message_repository
        self.user_repository: UsersRepository = user_repository

    def get_messages(self):
        messages = self.message_repository.get_messages()
        return messages

    def get_message(self, id):
        message = self.message_repository.get_message(id)
        message = {'id': message[0], 'sender_email': self.user_repository.get_user(message[1])[1], 'recipient_email': self.user_repository.get_user(message[2])[1], 'subject': message[3], 'body': message[4]}
        return message
    
    def get_messages_by_sender(self, sender_id):
        messages = self.message_repository.get_messages_by_sender(sender_id)
        return messages
    
    def get_messages_by_sender_email(self, sender_email):
        sender = self.user_repository.get_user_by_email(sender_email)
        if sender is None:
            return None
        messages = self.message_repository.get_messages_by_sender(sender[0])
        messages = list(messages)
        for i in range(len(messages)):
            messages[i] = {'id': messages[i][0], 'sender_email': self.user_repository.get_user(messages[i][1])[1], 'recipient_email': self.user_repository.get_user(messages[i][2])[1], 'subject': messages[i][3], 'body': messages[i][4]}
        return messages
    
    def get_messages_by_recipient(self, recipient_id):
        messages = self.message_repository.get_messages_by_recipient(recipient_id)
        return messages
    
    def get_messages_by_recipient_email(self, recipient_email):
        recipient = self.user_repository.get_user_by_email(recipient_email)
        if recipient is None:
            return None
        messages = self.message_repository.get_messages_by_recipient(recipient[0])
        messages = list(messages)
        for i in range(len(messages)):
            messages[i] = {'id': messages[i][0], 'sender_email': self.user_repository.get_user(messages[i][1])[1], 'recipient_email': self.user_repository.get_user(messages[i][2])[1], 'subject': messages[i][3], 'body': messages[i][4]}
        return messages

    def send_message(self, sender_email, recipient_email, subject, body):
        sender = self.user_repository.get_user_by_email(sender_email)
        recipient = self.user_repository.get_user_by_email(recipient_email)
        print(sender, recipient)
        if sender is None or recipient is None:
            return None
        message = self.message_repository.insert_message(sender[0], recipient[0], subject, body)
        return message

    def delete_message(self, id):
        self.message_repository.delete_message(id)
