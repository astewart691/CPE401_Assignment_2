'''
Project: CPE 401 Assignment2
File: client_two_implementation.py
Author: Aarron Stewart
'''

# import desired libraries/modules
from socket import socket, AF_INET, SOCK_STREAM


def main():
    # assigns the ip address to SERVER and port number to PORT. Creates a tuple.
    (SERVER, PORT) = ('127.0.0.1', 10000)

    # creates a socket to communicate
    s = socket(AF_INET, SOCK_STREAM)

    # creates a connection between the server and itself
    s.connect((SERVER, PORT))

    msg = "Hello, world 2"

    # sends a message to the server
    s.send(msg.encode())

    # receives a message from the connection source
    data = s.recv(1024)

    # close the socket
    s.close()

    print('Received', data.decode())

main()