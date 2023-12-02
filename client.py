import threading
import socket

try:
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[C]: Client socket created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()

# connect to the server on local machine
server_binding = ("localhost", 9999)
cs.connect(server_binding)

# recieve data from server: Welcome to Blueprint  
"""data_from_server=cs.recv(1024)
message = data_from_server.decode()
print("[C]: Data received from server: " + message)    
cs.send(input("Response here: ").encode())

# IN GROUPS
# receive data from server: How are you
data_from_server=cs.recv(1024)
message = data_from_server.decode()
print("[C]: Data received from server: " + message)    
cs.send(input("Response here: ").encode())
"""
count = 0
while(count < 2): # use loop to send 1, 2, 3, 4, 5 to client
    data_from_server=cs.recv(1024)
    message = data_from_server.decode()
    print("[C]: Data received from server: " + message)    
    cs.send(input("Response here: ").encode())
    count+=1

# close the client sockets
cs.close()
exit()