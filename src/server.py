import socketserver
from DAO.Standard_DAO import StandardDAO
from api import RequestHandler

PORT = 8000

with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    StandardDAO()
    print("serving at port", PORT)
    httpd.serve_forever()