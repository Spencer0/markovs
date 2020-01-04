from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import datetime
import SentencePredictor
import json


sp = SentencePredictor.SentencePredictor()

class S(BaseHTTPRequestHandler):
    def set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()


    def do_GET(self):
        self.set_response()
        time = str(datetime.datetime.now())
        prediction = sp.predictPhrase(self.path[1:])
        logging.debug(prediction)
        self.wfile.write(str.encode(prediction))

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        BaseHTTPRequestHandler.end_headers(self)

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('SERVER STARTED: PREDICTION SERVICE\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('SERVER STARTED: PREDICTION SERVICE\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()