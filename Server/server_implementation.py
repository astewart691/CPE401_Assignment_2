"""
Project: CPE 401 Assignment2
File: server_implementation.py
Author: Aarron Stewart
"""

# import desired libraries/modules
from socket import socket, AF_INET, SOCK_STREAM
from Server import server_supplemental as sup
# from uuid import getnode
import threading

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
index = -1
local_host = '127.0.0.1'
'''
Server design was implemented form the lecture on server implementations.
'''


# s is the socket variable for the listening port
s = socket(AF_INET, SOCK_STREAM)

# binds the socket to the local host and the designated port
s.bind((local_host, 10001))

# The socket listens for a client to try and connect
s.listen(5)  # max queued connections

# infinite loop for the server
while True:

    # socket is the new socket that is used to communicate with a client
    # address is a tuple with the IP address of the client
    sock, addr = s.accept()

    # create a thread to handle additional traffic
    client = threading.Thread(name = (index + 1), target = sup.process_client(sock,
                                                                              addr,
                                                                              registration_table,
                                                                              mailbox_container))
    client.setDaemon(True)
    client.start()


