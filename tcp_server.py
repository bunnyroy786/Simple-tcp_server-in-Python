import socket
import threading

bind_ip='0.0.0.0'
bind_port=9999

print("Starting tcp Server..............")
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((bind_ip,bind_port))

print("Creating Server.........................")
s.listen(10)
print("[*]Listning to %s : %d" % (bind_ip, bind_port))


#handle response from client and send back acknowledgement of connection
def handle_client(client_socket):
    request=client_socket.recv(1024)
    print("[*]Recived at %s" % request)
    data="ACK!!!"
    client_socket.send(data.encode())
    client_socket.close()


while True:
    client,addr = s.accept()
    print("[*]Accepted connection on %s : %d " % (addr[0],addr[1]))
    client_handler=threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
