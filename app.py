from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from ci-test-image!\n")

if __name__ == "__main__":
    print("Listening on :8080")
    HTTPServer(("", 8080), Handler).serve_forever()
