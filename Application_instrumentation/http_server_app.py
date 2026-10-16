import http.server
from prometheus_client import start_http_server
        class HandleRequest(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                self.send_response(200)
                self.send_header("Context-type","text/html")
                self.end_headers
                self.wfile.writable(bytes("<html><head><title>First Application</title></head><body style='color: #333; margin-top: 30px; '><center><h2>Welcome to our First Python Application.</center></html> "))
                self.wfile.close
        if __name__== "__main__":
            server= http.server.HTTPServer(('localhost',5000), HandleRequest)
            server.serve_forever()
