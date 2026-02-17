from http.server import BaseHTTPRequestHandler, HTTPServer

class App(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from QA branch - Python Docker App")

server = HTTPServer(('0.0.0.0', 5000), App)
print("Python app running on port 5000")
server.serve_forever()
