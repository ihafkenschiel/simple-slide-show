#!/usr/bin/env python3
"""
PROTOTYPE runner — serves this folder as a gallery and opens it in your browser.

    python3 serve.py            # serves on :8000, opens the browser
    python3 serve.py 9000       # pick a different port

It just static-serves the current folder, plus one extra route, /__images,
that returns the list of image filenames as JSON so the page can auto-discover
every picture you dropped in here. Throwaway — see NOTES.md.
"""
import http.server, json, os, re, sys, webbrowser

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
IMG = re.compile(r"\.(jpe?g|png|gif|webp|avif|bmp|svg)$", re.I)


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.split("?")[0] == "/__images":
            names = sorted(f for f in os.listdir(".") if IMG.search(f))
            body = json.dumps(names).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()

    def log_message(self, *a):  # quieter terminal
        pass


if __name__ == "__main__":
    url = f"http://localhost:{PORT}"
    print(f"Gallery → {url}   (Ctrl-C to stop)")
    if os.environ.get("NO_OPEN") != "1":
        webbrowser.open(url)
    http.server.HTTPServer(("", PORT), Handler).serve_forever()
