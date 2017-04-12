"""
Project: CPE 401 Assignment2
File: client_one_supplemental.py
Author: Aarron Stewart
"""
import boto3
import datetime as datetime
import subprocess
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
    print('\r')
    print('Server Communication:')
    print('Select Option using Integer value')
    print('Register Device: 1')
    print('DeRegister Device: 2')
    print('Send Message: 3')
    print('Query Server: 4')
    print('Quit Device: 5')
    print('\r')
    print('Application Level:')
    print('TraceRoute: 6')
    print('Send TraceRoute: 7')
    print('\r')


def process_request(tcp_sock, udp_sock, mac_add, device_name, udp_tab):
    """
    Get the option from the user and process the request

    :return:
    """

    return_val = True
    bucket_name = 'cpe401'
    obj_path = 'client' + '/' + device_name + '/'
    message = ''

    # initialize function/variables
    option = raw_input('Enter your selection: ')

    if option == '1':

        message = return_msg = register_device(tcp_sock, device_name, mac_add)
        print(return_msg)
    elif option == '2':
        print('DeRegister device')
        message = return_msg = deregister_device(tcp_sock, mac_add)
        print(return_msg)
        return_val = False
    elif option == '3':
        # need to create the full setup for the menu.
        print('Send message')
    elif option == '4':
        message = query(tcp_sock, udp_tab)
        print('Query Server')
    elif option == '5':
        # need to create the full setup for the menu.
        print('Quit Device')
        message = quit_device(tcp_sock, device_name)
        return_val = False

    elif option == '6':

        # need to create the full setup for the menu.
        print('TraceRoute requested')
        option = app_task()

        if option == '1':

            file_name = 'Ping.txt'

            cloud_message(bucket_name, file_name, obj_path)

        elif option == '2':

            file_name = 'Traceroute.txt'

            cloud_message(bucket_name, file_name, obj_path)

        cloud_notify(tcp_sock, device_name, option)

    elif option == '7':
        print('Send TraceRoute to IoT Device')
        message = send_udp(udp_sock, device_name, udp_tab)
    else:
        print('error message')

    print(message)

    if message != '':

        file_path = 'client' + '/' + device_name + '/'

        if message[1] == 'ACK':

            log('activity.log', message)

            cloud_message(bucket_name, 'activity.log', file_path)

        elif message[1] == 'NACK':

            log('error.log', message)

            cloud_message(bucket_name, 'error.log', file_path)

    return return_val


def register_device(tcp_sock, device_name, mac_address):

    # create the message to send to server
    msg_value = register_device_msg(device_name, mac_address)

    # send the register message to the server and return message
    return_val = send_data_tcp(tcp_sock, msg_value)

    # return the message to client
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

    # get device name that you wish to deregister
    device_name = raw_input('Please enter device ID requested: ')

    # create deregister message for the server
    msg_value = deregister_device_msg(device_name, mac_address)

    # send the deregister message to the server and return the response
    return_val = send_data_tcp(tcp_sock, msg_value)

    # return the message from the server
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

    # request the type of query that is needed
    msg_code = raw_input("Enter 1 to get udp port number or 2 for mailbox count: ")

    # request the device name to message
    device_name = raw_input('Enter device name to message: ')

    # create query message to send to the server
    message = query_msg(msg_code, device_name)

    # send the message to the server and receive the replay from the server
    return_val = send_data_tcp(tcp_sock, message)

    # test to see which message was sent to process reply from the server
    if msg_code == '1':

        # test to see if the reply from the server is was valid
        if return_val[1] == 'ACK':

            udp_table.append({"device_id": device_name, "address": (return_val[4], int(return_val[5]))})

            return return_val
        else:

            # handle what would happen if the message from the server was invalid
            return return_val

    # test to see if the message request was for mailbox count
    elif msg_code == '2':

        # test to see if the reply from the server was valid
        if return_val[1] == 'ACK':

            # display message with counts from the server
            return return_val

        else:

            # handle what would happen if the message from the server was invalid
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


def quit_device(soc, device_id):

    message = quit_device_msg(device_id)

    return_val = send_data_tcp(soc, message)

    return return_val


def quit_device_msg(device_id):
    """

    :param device_id:
    :return:
    """

    # create the base message to be sent to the server
    msg_value = 'QUIT' + ',' + device_id

    # get the message length and typecast it to string
    msg_len = str(len(msg_value))

    # return the message length concatenated with the base message
    return msg_len + ',' + msg_value


def log(file_dest, message):

    # generate a time stamp for the log event
    time_stamp = str(datetime.datetime.now())

    # open the file to append the event to the log file
    file_name = open(file_dest, 'a')

    # write the log event to the file
    file_name.write(str(message) + ',' + time_stamp + '\r\n')

    # close the file
    file_name.close()


def send_data_tcp(socket_val, msg_value):

    # encode the message that needs to be transmitted
    data = msg_value.encode()

    # send the data to the server
    socket_val.send(data)

    # receive reply from the server
    data = socket_val.recv(1024)

    # decode the reply from the server
    data_val = data.decode()

    # strip the data message to be processed
    data_val = data_val.strip()

    # break the message into array elements and return an array
    return data_val.split(',')


def cloud_notify(soc, device_id, notification_type):

    message = cloud_notify_msg(device_id, notification_type)

    return_val = send_data_tcp(soc, message)

    return return_val


def cloud_notify_msg(device_id, notif_type):
    """

    :param device_id:
    :return:
    """

    # create the base message to be sent to the server
    msg_value = 'CLOUD' + ',' + device_id + ',' + notif_type

    # get the message length and typecast it to string
    msg_len = str(len(msg_value))

    # return the message length concatenated with the base message
    return msg_len + ',' + msg_value

########################################################################################################################


def send_udp(udp_sock, device_id, udp_table):

    # initialize variables
    not_valid = True
    index = 0

    # retrieve the device id to send message too
    receiver = raw_input('What client would you like to message: ')

    # loop until a valid device is found
    while not_valid:

        # test to see if the device is found at the current index
        if udp_table[index]['device_id'] != receiver:

            # test to see if the index is the end of the list
            if index >= len(udp_table):

                # prompt user to give a valid device id to message
                receiver = raw_input('invalid device id. Please reenter: ')

                # reset index to zero and search the list again
                index = 0

        else:

            # terminate the loop
            not_valid = False

    # prompt the user for a message to send. This is temporary until I can figure out how to run traceroute
    data = raw_input('Enter message you would like to send to client: ')

    # get the address for the client as a tuple ( IP Address, Port Number )
    receiver_address = udp_table[index]['address']

    # generate message to send to the client. Should resemble the actual message when pin and traceroute works
    message = 'DATA' + ',' + device_id + ',' + 'PING' + ',' + data

    # send the udp data and return the reply from the client
    return_value = send_data_udp(udp_sock, message, receiver_address)

    # send_data_udp(udp_sock, message, receiver_address)
    # return_value = recv_data_udp(udp_sock, device_id)
    print(return_value)

    # return the message from the server
    return return_value


def send_data_udp(sock, msg_value, to_address):

    # send the udp message using the udp socket and the to_address.
    sock.sendto(msg_value, to_address)

    # receive the data and the address from the
    data, recv_from = sock.recvfrom(1024)

    '''
    run = True

    while run:

        data = sock.recvfrom(1024)

        if data != '':

            data, recv_from_address = sock.recvfrom(1024)

            data = data.strip()

            data = data.split(',')

            if data[0] == 'DATA':

                print(data)

                msg_val = 'ACK' + ',' + device_id

                sock.sendto(msg_val, recv_from_address)

                return data

            else:

                print('ACK received')
    '''
    return data

'''
def recv_data_udp(sock, device_id):

    run = True

    while run:

        data = sock.recvfrom(1024)

        if data != '':

            data, recv_from_address = sock.recvfrom(1024)

            data = data.strip()

            data = data.split(',')

            if data[0] == 'DATA':

                print(data)

                msg_val = 'ACK' + ',' + device_id

                sock.sendto(msg_val, recv_from_address)

                return data

            else:

                print('ACK received')
'''


def app_task():

    file_dest = ''

    option = raw_input('Enter 1 for Ping or 2 for Traceroute: ')

    host_name = raw_input('Enter web address: ')

    if option == '1':

        #cloud_receive('cpe401clientone', 'Ping.txt')

        ping_command = subprocess.Popen(['Ping', '-c 2', host_name], stdout = subprocess.PIPE)

        data = ping_command.communicate()[0]

        file_dest = 'Ping.txt'

    elif option == '2':

        cloud_receive('cpe401clientone', 'Traceroute.txt')
        ping_command = subprocess.Popen(['traceroute', host_name], stdout = subprocess.PIPE)

        data = ping_command.communicate()[0]

        file_dest = 'Traceroute.txt'

    file_act = open(file_dest, 'a')

    file_act.write(data + '\r')

    file_act.close()

    print(option)
    return option


def cloud_receive(bucket_loc, filename):

    # create connection for AWS S3 service
    s3 = boto3.resource('s3')

    # download file that will be updated
    s3.Object('cpe401clientone', 'Ping.txt').download_file('Ping.txt')

    # erase message in case it is read on accident
    cloud_message_blank(bucket_loc, filename)


def cloud_message_blank(bucket_loc, filename):

    # create connection for AWS S3 service
    s3 = boto3.resource('s3')

    # uploads a blank document to clear file
    s3.Object(bucket_loc, filename).upload_file('blank.txt')


def cloud_message(bucket_loc, filename, file_path):

    # create connection for AWS S3 service
    s3 = boto3.resource('s3')

    path = file_path + filename

    # updoad file to S3 bucket
    s3.Object(bucket_loc, path).upload_file(filename)
