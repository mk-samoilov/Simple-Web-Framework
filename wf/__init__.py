import socket
import threading
import os

def render_template(template_name, **context):
    try:
        with open(os.path.join("templates"), "r") as file:
            template_content = file.read()
            for key, value in context.items():
                template_content = template_content.replace("{{" + key + "}}", str(value))
            return template_content
    except FileNotFoundError:
        return f"Template '{template_name}' not found."

class WApp:
    def __init__(self, host: str = "localhost", port: int = 80):
        self.host = host
        self.port = port

        self.routes = {}

    def route(self, path, methods: list = ["GET"]):
        def decorator(func):
            self.routes[path] = {"handler": func, "methods": methods}
            return func

        return decorator

    def run(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.host, self.port))
        server_socket.listen(1)
        print(f"Server running on http://{self.host}:{self.port}")

        while True:
            client_socket, address = server_socket.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        request = client_socket.recv(1024).decode("utf-8")
        request_lines = request.split('\r\n')
        request_line = request_lines[0].split()

        if len(request_line) >= 2:
            method, path = request_line[0], request_line[1]

            headers = {}
            for line in request_lines[1:]:
                if ':' in line:
                    key, value = line.split(':', 1)
                    headers[key.strip()] = value.strip()

            body = request_lines[-1]

            if path in self.routes and method in self.routes[path]["methods"]:
                handler = self.routes[path]["handler"]
                response = handler(method, headers, body)
            else:
                response = "HTTP/1.1 404 Not Found\r\n\r\n404 Not Found"

        else:
            response = "HTTP/1.1 400 Bad Request\r\n\r\nBad Request"

        client_socket.sendall(response.encode("utf-8"))
        client_socket.close()
