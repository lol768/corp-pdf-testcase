#!/usr/bin/env python
import SimpleHTTPServer

class CorpHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_corp()
        SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)

    def send_corp(self):
        self.send_header("Cross-Origin-Resource-Policy", "same-origin")

if __name__ == '__main__':
    SimpleHTTPServer.test(HandlerClass=CorpHandler)
