import http.server
import json
from DAO.Users_DAO import Users_DAO
from DAO.Messages_DAO import Messages_DAO
import sqlite3

def split_query(query:str) -> dict:
    query = query.split('&')
    query_dict = {}
    for item in query:
        item = item.split('=')
        query_dict[item[0]] = item[1]
    return query_dict

def split_path(path:str) -> list:
    path = path.split('?')
    if len(path) == 1:
        return [path[0], None]
    else:
        query = split_query(path[1])
        return [path[0], query]

class RequestHandler(http.server.BaseHTTPRequestHandler):
    messages_dao = Messages_DAO()
    users_dao = Users_DAO()

    def do_GET(self):
        request_path = split_path(self.path)
        path = request_path[0]
        params = request_path[1]
        if path == '/':
            users = self.users_dao.get_all_users()
            json_data = json.dumps(users)
            print(users)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(bytes(json_data, 'utf-8'))
        elif path == '/message':
            if params == None:
                get_messages(self)
            elif 'message_id' in params:
                get_message(self, params['message_id'])
            elif 'sender_id' in params:
                get_messages_by_sender(self, params['sender_id'])
            elif 'sender_email' in params:
                get_messages_by_sender_email(self, params['sender_email'])
        else:
            self.send_error(404, "Route unavailable")
    
    def do_POST(self):
        if self.path == '/':
            with open('data.json', 'a') as f:
                json_data = self.rfile.read(int(self.headers['Content-Length'])).decode('utf-8')
                f.write(json_data)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(bytes(json_data, 'utf-8'))
        elif self.path == '/user':
            json_data:str = self.rfile.read(int(self.headers['Content-Length'])).decode('utf-8')
            json_data:dict = json.loads(json_data)
            print(json_data['name'], json_data['email_address'])
            self.users_dao.insert_user(json_data['name'], json_data['email_address'])
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            json_data = json.dumps(json_data)
            self.wfile.write(bytes(json_data, 'utf-8'))
        elif self.path == '/email':
            json_data:str = self.rfile.read(int(self.headers['Content-Length'])).decode('utf-8')
            json_data:dict = json.loads(json_data)
            self.messages_dao.insert_message(json_data['sender_id'], json_data['recipient_id'], json_data['subject'], json_data['body'])
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            json_data = json.dumps(json_data)
            self.wfile.write(bytes(json_data, 'utf-8'))
        else:
            self.send_error(404, "Route unavailable")

def get_message(request:RequestHandler, message_id:int):
    try:
        message = request.messages_dao.get_message_by_id(message_id)
        json_data = json.dumps(message)
        request.send_response(200)
        request.send_header('Content-type', 'application/json')
        request.end_headers()
        request.wfile.write(bytes(json_data, 'utf-8'))
    except(sqlite3.OperationalError, TypeError):
        request.send_error(400, "Bad Request")

def get_messages(request:RequestHandler):
    try:
        messages = request.messages_dao.get_all_messages()
        json_data = json.dumps(messages)
        print(json_data)
        request.send_response(200)
        request.send_header('Content-type', 'application/json')
        request.end_headers()
        request.wfile.write(bytes(json_data, 'utf-8'))
    except(sqlite3.OperationalError, TypeError):
        request.send_error(400, "Bad Request")

def get_messages_by_sender(request:RequestHandler, sender_id:int):
    try:
        messages = request.messages_dao.get_messages_by_sender(sender_id)
        json_data = json.dumps(messages)
        request.send_response(200)
        request.send_header('Content-type', 'application/json')
        request.end_headers()
        request.wfile.write(bytes(json_data, 'utf-8'))
    except(sqlite3.OperationalError, TypeError):
        request.send_error(400, "Bad Request")

def get_messages_by_sender_email(request:RequestHandler, sender_email:str):
    try:
        sender = request.users_dao.get_user_by_email(sender_email)
        messages = request.messages_dao.get_messages_by_sender(sender[0])
        json_data = json.dumps(messages)
        request.send_response(200)
        request.send_header('Content-type', 'application/json')
        request.end_headers()
        request.wfile.write(bytes(json_data, 'utf-8'))
    except(TypeError):
        request.send_error(400, "Bad Request")

def delete_message(request:RequestHandler, message_id:int):
    try:
        request.messages_dao.delete_message(message_id)
        request.send_response(200)
        request.send_header('Content-type', 'application/json')
        request.end_headers()
        request.wfile.write(bytes("Message deleted", 'utf-8'))
    except(sqlite3.OperationalError, TypeError):
        request.send_error(400, "Bad Request")

def get_user(request:RequestHandler, user_email:str):
    try:
        user = request.users_dao.get_user_by_email(user_email)
        json_data = json.dumps(user)
        request.send_response(200)
        request.send_header('Content-type', 'application/json')
        request.end_headers()
        request.wfile.write(bytes(json_data, 'utf-8'))
    except(sqlite3.OperationalError, TypeError):
        request.send_error(400, "Bad Request")

def get_users(request:RequestHandler):
    try:
        users = request.users_dao.get_all_users()
        json_data = json.dumps(users)
        request.send_response(200)
        request.send_header('Content-type', 'application/json')
        request.end_headers()
        request.wfile.write(bytes(json_data, 'utf-8'))
    except(sqlite3.OperationalError, TypeError):
        request.send_error(400, "Bad Request")
