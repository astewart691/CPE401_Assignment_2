'''
Project: CPE 401 Assignment2
File: server_implementation.py
Author: Aarron Stewart
'''

# import desired libraries/modules
from socket import socket, AF_INET, SOCK_STREAM

# s is the socket variable for the listening port
s = socket(AF_INET, SOCK_STREAM)

# binds the socket to the local host and the designated port
s.bind(('127.0.0.1', 10001))

# The socket listens for a client to try and connect
s.listen(5)  # max queued connections

# infinite loop for the server
while True:

    # socket is the new socket that is used to communicate with a client
    # address is a tuple with the IP address of the client
    sock, addr = s.accept()

    data = sock.recv(1024)

    sock.send(data)

    print(data.decode())