from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import requests


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        with open('src/contacts.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
        self.wfile.write(html_content.encode('utf-8'))


    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        parsed_data = urllib.parse.parse_qs(post_data)

        print("Получены данные от пользователя:")
        for key, value in parsed_data.items():
            print(f"{key}: {value[0]}")

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        with open('src/contacts.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
        self.wfile.write(html_content.encode('utf-8'))


def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Сервер запущен на порту 8000...")
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()
