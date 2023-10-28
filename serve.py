#!/usr/bin/env python3

"""
A non-caching version of `python3 -m http.server 8000`
"""

import sys
import socketserver
import http.server

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
  def end_headers(self):
    self.send_my_headers()
    http.server.SimpleHTTPRequestHandler.end_headers(self)

  def send_my_headers(self):
    self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
    self.send_header("Pragma", "no-cache")
    self.send_header("Expires", "0")

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
  print("Server started at localhost:" + str(PORT))
  httpd.serve_forever()

