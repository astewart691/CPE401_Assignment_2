"""
Project: CPE 401 Assignment2
File: client_one_implementation.py
Author: Aarron Stewart
"""

# import desired libraries/modules
from socket import socket, AF_INET, SOCK_STREAM
from client_one import client_one_supplemental as sup
from uuid import getnode

# initialize variables
# mac = hex(getnode() + 2)
mac = hex(getnode())
current_device = 'device_one'
to_device = 'device_two'
message = 'I hope this works'
SUCCESSFUL = 'activity.log'
ERROR = 'error.log'

def main():

    '''
    The client socket design and layout was implemented from class presentation on how to design a client implementation.
    '''

    # assigns the ip address to SERVER and port number to PORT. Creates a tuple.
    (SERVER, PORT) = ('127.0.0.1', 10001)

    # creates a socket to communicate
    s = socket(AF_INET, SOCK_STREAM)
    # creates a connection between the server and itself
    s.connect((SERVER, PORT))

    # generate a message to be sent to the server
    msg = sup.register_device("device_one", mac)
    # msg = sup.quit_device("device_one")
    # msg = sup.deregister_device("device_one", mac)
    # msg = sup.msg(current_device, current_device, message)
    # msg = sup.query('1', current_device)
    # msg = sup.query('2', current_device)

    # sends a message to the server
    s.send(msg.encode())

    # receives a message from the connection source
    data = s.recv(1024)

    # decode, strip, and split the data received from the server to record the records
    data = data.decode()

    data = data.strip()

    data = data.split(',')

    # test to see if the message contains an ack or nack
    if data[1] == 'ACK':

        # log the message response showing success in the activity.log file
        sup.log(SUCCESSFUL, data[1:])

    elif data[1] == 'NACK':

        # log the message response showing an error in the error.log file
        sup.log(ERROR, data[1:])

    # print to console for easy debugging
    print(data)

    # close the socket
    s.close()

main()
