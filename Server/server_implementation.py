"""
Project: CPE 401 Assignment2
File: server_implementation.py
Author: Aarron Stewart
"""

# import desired libraries/modules
from socket import socket, AF_INET, SOCK_STREAM
from Server import server_supplemental as sup
# from uuid import getnode

# initialize variables
'''
registration_table: list of dictionaries
    format:
        device_id
        mac_address
        ip_address
        port_number

mailbox_container:
    device_id
    count
    mail format:
        from_id
        to_id
        message
        time - time is used when stored in the mailbox and sent with the pull request.
                Not used with the push request

mac: mac address for the current device
'''
registration_table = []
mailbox_container = []

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

    print(addr[0], addr[1])
    data = sock.recv(1024)
    data = data.decode()
    print(data.split())

    data1 = data.strip()
    data1 = data.split(',')
    print(data1[0], data1[1])
    reply = sup.message_received(registration_table, mailbox_container, data1, addr)
    print(registration_table)
    print(reply)
    sock.send(reply.encode())
