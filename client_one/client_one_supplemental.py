"""
Project: CPE 401 Assignment2
File: client_one_supplemental.py
Author: Aarron Stewart
"""

import datetime as datetime
# from threading import Thread

# class UdpThread(Thread):
#    def __init__(self):


def display_menu():
    """
    The display for the user to determine how to select an option

    :return:
    """
    # display title
    print('Client Menu')
    print('Select Option using Integer value')
    print('Register Device: 1')
    print('DeRegister Device: 2')
    print('Send Message: 3')
    print('Query Server: 4')
    print('Quit Device: 5')
    print('TraceRoute: 6')
    print('Send TraceRoute: 7')
    print('\n')


def process_request(tcp_sock, udp_sock, mac_add, udp_tab):
    """
    Get the option from the user and process the request

    :return:
    """

    return_val = True

    # initialize function/variables
    option = raw_input('Enter your selection: ')

    if option == '1':

        return_msg = register_device(tcp_sock, mac_add)
        print(return_msg)
    elif option == '2':
        print('DeRegister device')
        return_msg = deregister_device(tcp_sock, mac_add)
        print(return_msg)
        return_val = False

    elif option == '3':
        print('Send message')
    elif option == '4':
        query(tcp_sock, udp_tab)
        print('Query Server')
    elif option == '5':
        print('Quit Device')
    elif option == '6':
        print('TraceRoute requested')
    elif option == '7':
        print('Send TraceRoute to IoT Device')
        send_udp(udp_sock, udp_tab)
    else:
        print('error message')

    return return_val


def register_device(tcp_sock, mac_address):
    """

    :param tcp_sock:
    :param mac_address:
    :return:
    """
    device_name = raw_input('Please enter device ID requested: ')

    msg_value = register_device_msg(device_name, mac_address)

    return_val = send_data_tcp(tcp_sock, msg_value)

    return return_val


def register_device_msg(device_id, mac_add):
    """

    :param device_id:
    :param mac_add:
    :return:
    """

    # type cast the device_id as a string
    device = str(device_id)

    # type cast the mac_add as a string
    mac = str(mac_add)

    # create the base message to be transmitted
    msg_current = "REGISTER" + ',' + device + ',' + mac + ',' + '\r\n'

    # get the length of the base message
    msg_length = len(msg_current)

    # type cast the message length string and assign it to complete message with the base message
    complete_message = str(msg_length) + ',' + msg_current

    # return the complete message
    return str(complete_message)


def deregister_device(tcp_sock, mac_address):
    """

    :param tcp_sock:
    :param mac_address:
    :return:
    """
    device_name = raw_input('Please enter device ID requested: ')

    msg_value = deregister_device_msg(device_name, mac_address)

    return_val = send_data_tcp(tcp_sock, msg_value)

    return return_val


def deregister_device_msg(device_id, mac_add):
    """

    :param device_id:
    :param mac_add:
    :return:
    """

    # type cast the device_id as a string
    device = str(device_id)

    # type cast the mac_add as a string
    mac = str(mac_add)

    # create the base message to be sent to the server
    msg_value = "DEREGISTER" + ',' + device + ',' + mac + ',' + '\r\n'

    # get the length of the base message
    msg_length = len(msg_value)

    # type cast the message length and assign it to the complete message concatenated with the base message
    complete_message = str(msg_length) + ',' + msg_value

    # return the complete message
    return complete_message


def msg(device_id, recipient_id, message):
    """

    :param device_id:
    :param recipient_id:
    :param message:
    :return:
    """
    # create the base message to be sent to the server
    msg_value = 'MSG' + ',' + device_id + ',' + recipient_id + ',' + message

    # get the length of the base message
    msg_length = len(msg_value)

    # type cast the message length and assign it to the complete message concatenated with the base message
    complete_message = str(msg_length) + ',' + msg_value

    # return the complete message
    return complete_message


def query(tcp_sock, udp_table):

    msg_code = raw_input("Enter 1 to get udp port number or 2 for mailbox count: ")

    device_name = raw_input('Enter device name to message: ')

    message = query_msg(msg_code, device_name)

    return_val = send_data_tcp(tcp_sock, message)
    if msg_code == '1':

        if return_val[1] == 'ACK':

            udp_table.append({"device_id": device_name, "address": (return_val[4], int(return_val[5]))})

    return return_val


def query_msg(code, device_id):

    # create the base message to be sent to the server
    msg_value = 'QUERY' + ',' + code + ',' + device_id

    # get the length of the base message
    msg_length = len(msg_value)

    # type cast the message length and assign it to the complete message concatenated with the base message
    complete_message = str(msg_length) + ',' + msg_value

    # return the complete message
    return complete_message


def quit_device(device_id):
    """

    :param device_id:
    :return:
    """

    # create the base message to be sent to the server
    msg_value = 'QUIT,' + device_id

    # get the message length and typecast it to string
    msg_len = str(len(msg_value))

    # return the message length concatenated with the base message
    return msg_len + ',' + msg_value


def log(file_dest, message):

    time_stamp = str(datetime.datetime.now())

    file_name = open(file_dest, 'a')

    file_name.write(str(message) + ',' + time_stamp + '\r\n')

    file_name.close()


def send_data_tcp(socket_val, msg_value):

    data = msg_value.encode()

    socket_val.send(data)

    data = socket_val.recv(1024)

    data_val = data.decode()

    data_val = data_val.strip()

    return data_val.split(',')


def send_udp(udp_sock, udp_table):

    not_valid = True

    index = 0

    receiver = raw_input('What client would you like to message: ')

    while not_valid:

        if udp_table[index]['device_id'] != receiver:

            if index >= len(udp_table):

                receiver = raw_input('invalid device id. Please reenter: ')

                index = 0

        else:

            not_valid = False

    data = raw_input('Enter message you would like to send to client: ')

    receiver_address = udp_table[index]['address']

    return_value = send_data_udp(udp_sock, data, receiver_address)
    print(return_value)
    return return_value


def send_data_udp(sock, msg_value, to_address):

    sock.sendto(msg_value, to_address)

    data, recv_from = sock.recvfrom(1024)

    return data
