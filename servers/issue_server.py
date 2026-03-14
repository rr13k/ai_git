from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json


HOST = "0.0.0.0"
PORT = 8089


class IssueHandler(BaseHTTPRequestHandler):
    def _send_text(self, status_code: int, body: str) -> None:
        encoded = body.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def do_GET(self) -> None:
        if self.path == "/ping":
            self._send_text(200, "pong")
            return

        self._send_text(404, "not found")

    def do_POST(self) -> None:
        if self.path != "/issue":
            self._send_text(404, "not found")
            return

        try:
            content_length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self._send_text(400, "invalid content length")
            return

        raw_body = self.rfile.read(content_length)

        try:
            payload = json.loads(raw_body.decode("utf-8") or "{}")
        except json.JSONDecodeError:
            self._send_text(400, "invalid json")
            return

        title = str(payload.get("title", ""))
        _text = str(payload.get("text", ""))
        self._send_text(200, f"recv {title}")

    def log_message(self, format: str, *args) -> None:
        return


def main() -> None:
    server = ThreadingHTTPServer((HOST, PORT), IssueHandler)
    print(f"Listening on http://{HOST}:{PORT}")
    server.serve_forever()


if __name__ == "__main__":
    main()
