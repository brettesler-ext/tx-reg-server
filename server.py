from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def readfile(path):
        with open(path, 'rb') as f:
            return f.read()
        
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
       
        if self.path == "/metadata" or self.path == '/metadata?_summary=true':
            self.wfile.write(MyServer.readfile("metadata.json"))
        elif self.path == "/metadata?mode=terminology":
            self.wfile.write(MyServer.readfile("terminology.json"))
        else:
            self.wfile.write(MyServer.readfile("tx-reg.json"))
        # elif "common-languages-australia-1" in self.path or "unitsofmeasure.org" in self.path :
        #     self.wfile.write(MyServer.readfile("tx-reg.json"))
        # else:
        #     self.wfile.write(MyServer.readfile("tx-reg-csiro.json"))
            
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
    
        self.wfile.write(bytes("{}", "utf-8"))
    

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
    
    