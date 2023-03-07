import DAO.UsersDAO as UsersDAO
import service.UserService as UserService
import json

class UserController:
    def __init__(self) -> None:
        self.users_dao = UsersDAO.UsersDAO()
        self.user_service = UserService.UserService(self.users_dao)

    def set_headers(self, request_handler) -> None:
        request_handler.send_header('Access-Control-Allow-Origin', '*')
        request_handler.send_header('Access-Control-Allow-Methods', '*')
        request_handler.send_header('Access-Control-Allow-Headers', '*')
        request_handler.send_header('Content-Type', 'application/json')
        request_handler.end_headers()

    def get_user(self, request_handler, user_id:int) -> None:
        user = self.user_service.get_user(user_id)
        if user is None:
            request_handler.send_error(404, "User not found")
        else:
            request_handler.send_response(200)
            self.set_headers(request_handler)
            request_handler.wfile.write(bytes(json.dumps(user), 'utf-8'))

    def get_user_by_email(self, request_handler, email_address:str) -> None:
        user = self.user_service.get_user_by_email(email_address)
        if user is None:
            request_handler.send_error(404, "User not found")
        else:
            request_handler.send_response(200)
            self.set_headers(request_handler)
            request_handler.wfile.write(bytes(json.dumps(user), 'utf-8'))

    def get_users(self, request_handler) -> None:
        users = self.user_service.get_users()
        request_handler.send_response(200)
        self.set_headers(request_handler)
        request_handler.wfile.write(bytes(json.dumps(users), 'utf-8'))
    
    def add_user(self, request_handler, user_name:str, email_address:str) -> None:
        user = self.user_service.add_user(user_name, email_address)
        if user is None:
            request_handler.send_error(400, "User already exists")
        else:
            request_handler.send_response(201)
            self.set_headers(request_handler)
            request_handler.wfile.write(bytes(json.dumps(user), 'utf-8'))
