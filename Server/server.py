import socket
import os
import threading
import Searchfile
import json

bind_ip = "localhost"
bind_port = 2525

print("Starting the server-----------------------------")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((bind_ip, bind_port))
print("************************************************")
s.listen(10)
print("[*]Listning to %s : %d" % (bind_ip, bind_port))

def handle_client(client_socket):
    req = client_socket.recv(1024).decode()
    parts = req.split(",")
    print("[*]Recived : %s" % parts)
    filename = parts[1].strip()
    Word = parts[2].strip()
    
    if not os.path.isfile(filename):
        client_socket.send("File not found".encode("utf-8"))
        client_socket.close()
        return
    
    search_instance = Searchfile.Search(filename)
    result = search_instance.getLine(Word)
    
    print(result)
    
    if len(result) < 2:
        client_socket.send("Word is not found".encode("utf-8"))
    else:
        json_data = {
            "word" : result[0],
            "Word contains on" : [
                {
                    "Line no" : line_info[0],
                    "Sentence" : line_info[1]
                }
                for line_info in result[1:]
            ]
        }
        json_result = json.dumps(json_data, indent=4)
        client_socket.send(json_result.encode("utf-8"))
        client_socket.close()
    
while True:
    client, addr = s.accept()
    print("[*]Accepted Connection on %s : %d -------------------------------" % (addr[0], addr[1]))
    client_handler = threading.Thread(target=handle_client, args=(client, ))    
    client_handler.start()