import socket

#Here '0.0.0.0' reffers as LocalHost which is your own ip addrs 
host_ip='0.0.0.0'
host_port=9999


c=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((host_ip,host_port))


#Now we allocate a byte type data and send it to a server 
data="SYN!!!"
c.send(data.encode())


#Capturing a response from a server
response=c.recv(1024).decode()
print(response)

