#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
hostPort = 8000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Hello World</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><p>Hello World !</p>", "utf-8"))
        self.wfile.write(bytes("<p>This is the server time : <b>{}</b></p>".format(time.asctime()), "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()

print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
