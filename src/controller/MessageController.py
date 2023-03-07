import DAO.MessagesDAO as MessagesDAO
import DAO.UsersDAO as UsersDAO
from service.MessageService import MessageService
import json

class MessageController:
    def __init__(self) -> None:
        self.messages_dao = MessagesDAO.MessagesDAO()
        self.users_dao = UsersDAO.UsersDAO()
        self.messages_service = MessageService(self.messages_dao, self.users_dao)
        
    def set_headers(self, request_handler) -> None:
        request_handler.send_header('Access-Control-Allow-Origin', '*')
        request_handler.send_header('Access-Control-Allow-Methods', '*')
        request_handler.send_header('Access-Control-Allow-Headers', '*')
        request_handler.send_header('Content-Type', 'application/json')
        request_handler.end_headers()

    def get_message(self, request_handler, message_id:int) -> None:
        message = self.messages_service.get_message(message_id)
        if message is None:
            request_handler.send_error(404, "Message not found")
        else:
            request_handler.send_response(200)
            self.set_headers(request_handler)
            request_handler.wfile.write(bytes(json.dumps(message), 'utf-8'))
    
    def get_messages(self, request_handler) -> None:
        messages = self.messages_service.get_messages()
        request_handler.send_response(200)
        self.set_headers(request_handler)
        request_handler.wfile.write(bytes(json.dumps(messages), 'utf-8'))
    
    def get_messages_by_sender(self, request_handler, sender_id:int) -> None:
        messages = self.messages_service.get_messages_by_sender(sender_id)
        request_handler.send_response(200)
        self.set_headers(request_handler)
        request_handler.wfile.write(bytes(json.dumps(messages), 'utf-8'))

    def get_messages_by_user_email(self, request_handler, user_email:str) -> None:
        messages = self.messages_service.get_messages_by_sender_email(user_email)
        messages.extend(self.messages_service.get_messages_by_recipient_email(user_email))
        request_handler.send_response(200)
        self.set_headers(request_handler)
        request_handler.wfile.write(bytes(json.dumps(messages), 'utf-8'))
    
    def get_messages_by_sender_email(self, request_handler, sender_email:str) -> None:
        messages = self.messages_service.get_messages_by_sender_email(sender_email)
        request_handler.send_response(200)
        self.set_headers(request_handler)
        request_handler.wfile.write(bytes(json.dumps(messages), 'utf-8'))

    def get_messages_by_recipient_email(self, request_handler, sender_email:str) -> None:
        messages = self.messages_service.get_messages_by_recipient_email(sender_email)
        request_handler.send_response(200)
        self.set_headers(request_handler)
        request_handler.wfile.write(bytes(json.dumps(messages), 'utf-8'))

    def send_message(self, request_handler, sender_id:int, receiver_id:int, subject:str, body:str) -> None:
        message = self.messages_service.send_message(sender_id, receiver_id, subject, body)
        if message is None:
            request_handler.send_error(404, "Sender or receiver not found")
        else:
            request_handler.send_response(201)
            self.set_headers(request_handler)
            request_handler.wfile.write(bytes(json.dumps(message), 'utf-8'))
    
    def delete_message(self, request_handler, message_id:int) -> None:
        self.messages_service.delete_message(message_id)
        request_handler.send_response(204)
        self.set_headers(request_handler)
        request_handler.wfile.write(bytes("Message Deleted", 'utf-8'))
