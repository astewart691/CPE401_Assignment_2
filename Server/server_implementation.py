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
"""
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
"""

registration_table = []
mailbox_container = []

'''
Server design was implemented form the lecture on server implementations.
'''


# s is the socket variable for the listening port
s = socket(AF_INET, SOCK_STREAM)

# binds the socket to the local host and the designated port
s.bind(('192.168.1.78', 10001))

# The socket listens for a client to try and connect
s.listen(5)  # max queued connections

# infinite loop for the server
while True:

    # socket is the new socket that is used to communicate with a client
    # address is a tuple with the IP address of the client
    sock, addr = s.accept()

    data = sock.recv(1024)

    # decode, strip and split the message to allow for message processing
    data = data.decode()

    data1 = data.strip()

    data1 = data.split(',')

    # process the message to perform the appropriate action and return the appropriate response for the client
    reply = sup.message_received(registration_table, mailbox_container, data1, addr)

    # print reply to console for easy debugging
    print(reply)

    # sent the reply that has been encoded to bytes to the client
    sock.send(reply.encode())
