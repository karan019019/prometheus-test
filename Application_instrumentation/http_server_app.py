import http.server
from prometheus_client import start_http_server

class HandleRequest(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(
            "<html><head><title>First Application</title></head>"
            "<body style='color: #333; margin-top: 30px;'>"
            "<center><h2>Welcome to our First Python Application.</h2></center>"
            "</body></html>", "utf-8"
        ))

if __name__ == "__main__":
    # Start Prometheus metrics server on port 8000
    start_http_server(8000)

    # Start HTTP server on port 5000
    server = http.server.HTTPServer(('34.93.208.54', 5000), HandleRequest)
    server.serve_forever()
