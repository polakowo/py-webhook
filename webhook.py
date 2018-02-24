#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = ""
hostPort = 8555


def execute():
    print("Script is being executed")
    import subprocess
    subprocess.call(['sh', './script.sh'])


class MyServer(BaseHTTPRequestHandler):
    def do_POST(self):
        print("Request received")
        self.send_response(200)
        self.end_headers()
        # Redeploy
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode("utf-8")
        import json
        payload = json.loads(post_data)
        # Add logic here
        execute()


def run():
    host_address = (hostName, hostPort)
    myServer = HTTPServer(host_address, MyServer)
    print("Webhook listening - %s:%s" % host_address)
    try:
        myServer.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        myServer.server_close()
        print("Webhook stopped - %s:%s" % host_address)


if __name__ == "__main__":
    run()
