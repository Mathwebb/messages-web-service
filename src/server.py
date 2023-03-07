import socketserver
from Repository.StandardRepository import StandardRepository
from api import RequestHandler

PORT = 8000

with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    StandardRepository()
    print("serving at port", PORT)
    httpd.serve_forever()
