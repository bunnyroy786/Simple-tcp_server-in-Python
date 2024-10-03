import socket
import json

host_ip = "localhost"
host_port = 2525

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((host_ip, host_port))

filename = input("Enter the file name: ")        
word = input("Enter a word: ")

data = f"SYN!! , {filename}, {word}"
c.send(data.encode())

response = c.recv(4096).decode()
print(response)
c.close()