#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import os


class SimpleHTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello from Effective Mobile!')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

    def log_message(self, format, *args):
        # Логирование в stdout для Docker
        print(f"[{self.address_string()}] {format % args}")


def run_server():
    port = 8080
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, SimpleHTTPHandler)
    print(f'Server running on port {port}')
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()