import json
import http.server
from Repository.UsersRepository import UsersRepository
from Repository.MessagesRepository import MessagesRepository
from service.MessageService import MessageService
from service.UserService import UserService


class RequestHandler(http.server.BaseHTTPRequestHandler):
    messages_repository = MessagesRepository()
    users_repository = UsersRepository()
    messages_service = MessageService(messages_repository, users_repository)
    user_service = UserService(messages_repository, users_repository)

    def set_headers(self) -> None:
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', '*')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def do_GET(self):
        request_path: list = split_path(self.path)
        path: list = request_path[0]
        params: dict = request_path[1]
        path = ['/' + p for p in path]
        if path[0] == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            with open('frontend/pages/home/index.html', 'rb') as file:
                html = file.read()

            self.wfile.write(html)
        elif path[0] == '/index.css':
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()

            with open('frontend/pages/home/index.css', 'rb') as file:
                css = file.read()
            
            self.wfile.write(css)
        elif path[0] == '/index.js':
            self.send_response(200)
            self.send_header('Content-type', 'text/javascript')
            self.end_headers()

            with open('frontend/pages/home/index.js', 'rb') as file:
                js = file.read()
            
            self.wfile.write(js)
        elif path[0] == '/login':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            with open('frontend/pages/login/login.html', 'rb') as file:
                html = file.read()

            self.wfile.write(html)
        elif path[0] == '/login.css':
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()

            with open('frontend/pages/login/login.css', 'rb') as file:
                css = file.read()
            
            self.wfile.write(css)
        elif path[0] == '/login.js':
            self.send_response(200)
            self.send_header('Content-type', 'text/javascript')
            self.end_headers()

            with open('frontend/pages/login/login.js', 'rb') as file:
                js = file.read()
            
            self.wfile.write(js)    
        elif path[0] == '/new_message':
            if params is None:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                with open('frontend/pages/new_message/new_message.html', 'rb') as file:
                    html = file.read()

                self.wfile.write(html)
            else:
                self.send_error(404)
        elif path[0] == '/new_message.css':
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()

            with open('frontend/pages/new_message/new_message.css', 'rb') as file:
                css = file.read()
            
            self.wfile.write(css)
        elif path[0] == '/new_message.js':
            self.send_response(200)
            self.send_header('Content-type', 'text/javascript')
            self.end_headers()

            with open('frontend/pages/new_message/new_message.js', 'rb') as file:
                js = file.read()
            
            self.wfile.write(js)
        elif path[0] == '/message':
            if len(path) == 1:
                if params is None:
                    messages = self.messages_service.get_messages()
                    self.send_response(200)
                    self.set_headers()
                    self.wfile.write(bytes(json.dumps(messages), 'utf-8'))
                elif 'message_id' in params:
                    message = self.messages_service.get_message(params['message_id'])
                    if message is None:
                        self.send_error(404, "Message not found")
                    else:
                        self.send_response(200)
                        self.set_headers()
                        self.wfile.write(bytes(json.dumps(message), 'utf-8'))
                elif 'sender_email' in params:
                    messages = self.messages_service.get_messages_by_sender_email(params['sender_email'])
                    self.send_response(200)
                    self.set_headers()
                    self.wfile.write(bytes(json.dumps(messages), 'utf-8'))
                elif 'recipient_email' in params:
                    messages = self.messages_service.get_messages_by_recipient_email(params['recipient_email'])
                    self.send_response(200)
                    self.set_headers()
                    self.wfile.write(bytes(json.dumps(messages), 'utf-8'))
            elif len(path) == 2:
                if path[1][1:].isdecimal():
                    message = self.messages_service.get_message(path[1][1:])
                    with open('frontend/pages/message/message.html', 'rb') as file:
                        html = file.read()
                    html = html.decode('utf-8')
                    html = html.replace('<h2>From: <span id="sender-email"></span></h2>', f'<h2>From: <span id="sender-email">{message["sender_email"]}</span></h2>')
                    html = html.replace('<h3>To: <span id="recipient-email"></span></h3>', f'<h2>To: <span id="recipient-email">{message["recipient_email"]}</span></h2>')
                    html = html.replace('<h3>Subject: <span id="subject"></span></h3>', f'<h2>Subject: <span id="subject">{message["subject"]}</span></h2>')
                    html = html.replace('<p id="body"></p>', f'<p id="body">{message["body"]}</p>')
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(bytes(html, 'utf-8'))
                elif path[1] == '/message.css':
                    self.send_response(200)
                    self.send_header('Content-type', 'text/css')
                    self.end_headers()

                    with open('frontend/pages/message/message.css', 'rb') as file:
                        css = file.read()
                    
                    self.wfile.write(css)
                elif path[1] == '/message.js':
                    self.send_response(200)
                    self.send_header('Content-type', 'text/javascript')
                    self.end_headers()

                    with open('frontend/pages/message/message.js', 'rb') as file:
                        js = file.read()
                    
                    self.wfile.write(js)
                else:
                    self.send_error(404, "Message not found")
            elif len(path) == 3:
                if path[1][1:].isdigit():
                    if path[2] == '/forward':
                        self.send_response(200)
                        self.send_header('Content-type', 'text/html')
                        self.end_headers()

                        with open('frontend/pages/message/forward/forward.html', 'rb') as file:
                            html = file.read()

                        self.wfile.write(html)
                    elif path[2] == '/forward.css':
                        self.send_response(200)
                        self.send_header('Content-type', 'text/css')
                        self.end_headers()

                        with open('frontend/pages/message/forward/forward.css', 'rb') as file:
                            css = file.read()
                        
                        self.wfile.write(css)
                    elif path[2] == '/forward.js':
                        self.send_response(200)
                        self.send_header('Content-type', 'text/javascript')
                        self.end_headers()

                        with open('frontend/pages/message/forward/forward.js', 'rb') as file:
                            js = file.read()
                        
                        self.wfile.write(js)
                    elif path[2] == '/reply':
                        self.send_response(200)
                        self.send_header('Content-type', 'text/html')
                        self.end_headers()

                        with open('frontend/pages/message/reply/reply.html', 'rb') as file:
                            html = file.read()

                        self.wfile.write(html)
                    elif path[2] == '/reply.css':
                        self.send_response(200)
                        self.send_header('Content-type', 'text/css')
                        self.end_headers()

                        with open('frontend/pages/message/reply/reply.css', 'rb') as file:
                            css = file.read()
                        
                        self.wfile.write(css)
                    elif path[2] == '/reply.js':
                        self.send_response(200)
                        self.send_header('Content-type', 'text/javascript')
                        self.end_headers()

                        with open('frontend/pages/message/reply/reply.js', 'rb') as file:
                            js = file.read()
                        
                        self.wfile.write(js)
                    else:
                        self.send_error(404, "Message not found")
                else:
                    self.send_error(404, "Message not found")
        elif path[0] == '/user':
            if params is None:
                users = self.user_service.get_users()
                self.send_response(200)
                self.set_headers()
                self.wfile.write(bytes(json.dumps(users), 'utf-8'))
            elif 'user_id' in params:
                user = self.user_service.get_user(params['user_id'])
                if user is None:
                    self.send_error(404, "User not found")
                else:
                    self.send_response(200)
                    self.set_headers()
                    self.wfile.write(bytes(json.dumps(user), 'utf-8'))
            elif 'email_address' in params:
                user = self.user_service.get_user_by_email(params['email_address'])
                if user is None:
                    self.send_error(404, "User not found")
                else:
                    self.send_response(200)
                    self.set_headers()
                    self.wfile.write(bytes(json.dumps(user), 'utf-8'))
        else:
            self.send_error(404, "Route unavailable")

    def do_POST(self):
        request_path: list = split_path(self.path)
        path: list = request_path[0]
        path = ['/' + p for p in path]
        json_data: str = self.rfile.read(int(self.headers['Content-Length'])).decode('utf-8')
        json_data: dict = json.loads(json_data)
        if path[0] == '/user':
            if 'name' and 'email_address' in json_data:
                user = self.user_service.add_user(json_data['name'], json_data['email_address'])
                if user is None:
                    self.send_error(400, "User already exists")
                else:
                    self.send_response(201)
                    self.set_headers()
                    self.wfile.write(bytes(json.dumps(user), 'utf-8'))
        elif path[0] == '/message':
            if 'sender_email' and 'recipient_email' and 'subject' and 'body' in json_data:
                message = self.messages_service.send_message(json_data['sender_email'], json_data['recipient_email'], json_data['subject'], json_data['body'])
                if message is None:
                    self.send_error(404, "Sender or receiver not found")
                else:
                    self.send_response(201)
                    self.set_headers()
                    self.wfile.write(bytes(json.dumps(message), 'utf-8'))
        else:
            self.send_error(404, "Route unavailable")
    
    def do_DELETE(self):
        request_path: list = split_path(self.path)
        path: list = request_path[0]
        params: dict = request_path[1]
        path = ['/' + p for p in path]
        if path[0] == '/':
            pass
        elif path[0] == '/message':
            if 'message_id' in params:
                self.messages_service.delete_message(params['message_id'])
                self.send_response(204)
                self.set_headers()
                self.wfile.write(bytes("Message Deleted", 'utf-8'))
        elif path[0] == '/user':
            if 'user_id' in params:
                self.user_controller.delete_user(self, params['user_id'])
        else:
            self.send_error(404, "Route unavailable")
        


def split_query(query: str) -> dict:
    query = query.split('&')
    query_dict = {}
    for item in query:
        item = item.split('=')
        query_dict[item[0]] = item[1]
    return query_dict


def split_path(path: str) -> list:
    path = path.split('?')
    path[0] = path[0][1:].split('/')

    if len(path) == 1:
        return [path[0], None]
    else:
        query = split_query(path[1])
        return [path[0], query]
