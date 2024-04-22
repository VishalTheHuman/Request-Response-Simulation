"""
########## JSON Format ##########

REQUEST:

1. GET
{
    "method" : "GET", 
    "name" : <NAME OF THE FILE> , 
    "type" : <FILE TYPE> 
}

2. POST
{
    "method" : "POST", 
    "name" : <NAME OF THE FILE> , 
    "content" : <CONTENT IN THE FILE> , 
    "type" : <FILE TYPE> 
}

3. PUT 
{
    "method" : "PUT", 
    "name" : <NAME OF THE FILE> , 
    "content" : <CONTENT IN THE FILE> , 
    "type" : <FILE TYPE>
}

4. DELETE 
{
    "method" : "DELETE", 
    "name" : <NAME OF THE FILE>, 
    "type" : <FILE TYPE> 
}

RESPONSE:

{
    "status" : <STATUS CODE> , 
    "content" : <CONTENT REQUESTED> , 
    "type" : <FILE TYPE>
}

"""
import socket
import json
import os

class Server:
    def __init__(self, host="127.0.0.1", port=65432):
        self.PATH = "files/"
        self.host = host
        self.port = port
        self.server()
    
    def handleRequest(self, data):
        data = json.loads(data)
        method = data["method"]
        if method == "GET":
            return self.handleGET(data)
        elif method == "PUT":
            return self.handlePUT(data)
        elif method == "POST":
            return self.handlePOST(data)
        elif method == "DELETE":
            return self.handleDELETE(data)
        else:
            print("Invalid Request!")
            return json.dumps({"status": None})
        
    def handleGET(self, json_received):
        json_response = {}
        file_path = f"{self.PATH}{json_received['name']}.{json_received['type']}"
        json_response["method"] = "GET"
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                content = f.read()
            json_response["status"] = 200 # OK
            json_response["content"] = content
            json_response["name"] = json_received["name"]
            json_response["type"] = json_received["type"]
        else:
            json_response["status"] = 404 # Not Found
            json_response["content"] = None
            json_response["name"] = None
            json_response["type"] = None
        return json.dumps(json_response)
            
    def handlePUT(self, json_received):
        json_response = {}
        file_path = f"{self.PATH}{json_received['name']}.{json_received['type']}"
        json_response["method"] = "PUT"
        if os.path.exists(file_path):
            json_response["status"] = 200 # OK
        else:
            json_response["status"] = 201 # Created
        with open(file_path, "w") as f:
            f.write(json_received["content"])
        return json.dumps(json_response)

    def handlePOST(self, json_received):
        json_response = {}
        file_path = f"{self.PATH}{json_received['name']}.{json_received['type']}"
        json_response["method"] = "POST"
        json_response["content"] = None
        json_response["name"] = None
        json_response["type"] = None
        if os.path.exists(file_path):
            json_response["status"] = 400 # Bad Request
        else:
            json_response["status"] = 201  # Created
            with open(file_path, "w") as f:
                f.write(json_received["content"])
        return json.dumps(json_response)

    def handleDELETE(self, json_received):
        json_response = {}
        file_path = f"{self.PATH}{json_received['name']}.{json_received['type']}"
        if os.path.exists(file_path):
            os.remove(file_path)
            json_response["status"] = 200 # OK
        else:
            json_response["status"] = 404 # Not Found
        json_response["method"] = "DELETE"
        json_response["content"] = None
        json_response["name"] = None
        json_response["type"] = None
        return json.dumps(json_response)

    def server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"Server listening on {self.host}:{self.port}")
            while True:
                conn, address = s.accept()
                with conn:
                    print(f"Connected by {address}")
                    while True:
                        data = conn.recv(1000000)
                        if not data:
                            print("Connection closed by client")
                            break
                        
                        print("\n***************************\nRequest Received\n")
                        print(data.decode())
                        conn.sendall(self.handleRequest(data.decode()).encode())

if __name__ == "__main__":
    Server()
