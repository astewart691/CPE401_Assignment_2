"""
Project: CPE 401 Assignment2
File: client_one_implementation.py
Author: Aarron Stewart
"""

# import desired libraries/modules
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from client_one import client_one_supplemental as sup
from uuid import getnode
# from threading import Thread

# initialize variables
mac = hex(getnode())
SUCCESSFUL = 'activity.log'
ERROR = 'error.log'
udp_transfer_table = []


def main():

    # initialize variables and the sockets
    current_device = 'Aarron'
    run = True
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    # assign the server address and port to the variables
    (SERVER, PORT) = ('127.0.0.1', 10001)

    # create the tcp connection with the server
    tcp_socket.connect((SERVER, PORT))

    # qprint('tcp_port: ' + '%s') % tcp_socket.getsockname()[1]

    # get the tcp socket port number to create the udp socket correctly
    udp_socket.bind(('127.0.0.1', tcp_socket.getsockname()[1]))

    '''
    receive_udp = Thread(target = sup.recv_data_udp(udp_socket, current_device))
    receive_udp.setDaemon(True)
    receive_udp.start()
    '''

    # run while the program is running
    while run:

        # display the menu for the program
        sup.display_menu()

        # get the users response and perform the appropriate action
        run = sup.process_request(tcp_socket, udp_socket, mac, current_device, udp_transfer_table)

    # close the TCP and UDP Sockets
    tcp_socket.close()
    udp_socket.close()

# run the actual program
main()
