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
    "method" : <METHOD> , 
    "content" : <CONTENT REQUESTED> , 
    "name" : <FILE NAME>
    "type" : <FILE TYPE>
}

"""
import json
import socket
import time

class Client:
    def __init__(self, host="127.0.0.1", port=65432):
        self.host = host
        self.port = port
        self.client()

    def handleResponse(self, response):
        response = json.loads(response)
        status = response["status"]
        method = response["method"]
        content = response["content"] if "content" in response else None
        name = response["name"] if "name" in response else None
        file_type = response["type"] if "type" in response else None
        print("\n***************************\nResponse:")
        print(f"Status: {status}")
        print(f"Method: {method}")
        print(f"Content: {content}")
        print(f"Name: {name}")
        print(f"Type: {file_type}")
        print(f"***************************\n")
        
        if method == "GET":
            if status == 404:
                print("File not Found (404 Error)")
            else:
                print(f"Content : \n\n{content}\n")
                save_status = input("Want to save the file locally (Y/N) ? ").upper()
                if save_status == "Y":
                    with open(f"{name}.{file_type}","w") as f:
                        f.write(content)
                        f.close()
        elif method == "POST":
            if status == 201:
                print("A new file has been created.")
            else:
                print("Bad Request (400). File already exists. So changes can't be made. ")

        elif method == "PUT":
            if status == 201:
                print("New file has been created")
            else:
                print("Contents of the file has been modified")
        elif method == "DELETE":
            if status == 404:
                print("No such file exists (404 : File Not Found)")
            else:
                print("File has been removed.")
            
        time.sleep(1)

    def createRequest(self, mode):
        request = {}
        request["method"] = mode
        if mode == "GET":
            name = input("Enter the name of the file: ")
            request["name"], request["type"] = name.rsplit(".", 1)
        elif mode == "PUT" or mode == "POST":
            name = input("Enter the file path: ")
            request["name"], request["type"] = name.rsplit(".", 1)
            with open(name, "rb") as f:
                content = f.read()
            request["content"] = content.decode()
        elif mode == "DELETE":
            name = input("Enter the name of the file: ")
            request["name"], request["type"] = name.rsplit(".", 1)
        return json.dumps(request)

    def client(self):
        modes = {
            1:"GET", 
            2:"POST", 
            3:"PUT", 
            4:"DELETE"
        }
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            while True:
                try:
                    mode = int(input("\n::::::::::::::CLIENT::::::::::::::\n\nNOTE: **Enter Integer Only**\n1. GET\n2. POST\n3. PUT\n4. DELETE\n5. EXIT\nEnter: "))
                except ValueError:
                    print("***Enter Only Integer Inputs***\n")
                    continue
                if mode not in [1,2,3,4]:
                    break
                
                request = self.createRequest(modes[mode])
                s.sendall(request.encode())
                data = s.recv(1000000)
                self.handleResponse(data.decode())

if __name__ == "__main__":
    Client()