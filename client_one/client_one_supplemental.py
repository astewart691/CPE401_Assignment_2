"""
Project: CPE 401 Assignment2
File: client_one_supplemental.py
Author: Aarron Stewart
"""

import datetime as datetime

def register_device(device_id, mac_add):
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
    msg = "REGISTER" + ',' + device + ',' + mac

    # get the length of the base message
    msg_length = len(msg)

    # type cast the message length string and assign it to complete message with the base message
    complete_message = str(msg_length) + ',' + msg

    # return the complete message
    return str(complete_message)


def deregister_device( device_id, mac_add):
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
    msg = "DEREGISTER" + ',' + device + ',' + mac

    # get the length of the base message
    msg_length = len(msg)

    # type cast the message length and assign it to the complete message concatenated with the base message
    complete_message = str(msg_length) + ',' + msg

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
    msg = 'MSG' + ',' + device_id + ',' + recipient_id + ',' + message

    # get the length of the base message
    msg_length = len(msg)

    # type cast the message length and assign it to the complete message concatenated with the base message
    complete_message = str(msg_length) + ',' + msg

    # return the complete message
    return complete_message


def query(code, device_id):

    # create the base message to be sent to the server
    msg = 'QUERY' + ',' + code + ',' + device_id

    # get the length of the base message
    msg_length = len(msg)

    # type cast the message length and assign it to the complete message concatenated with the base message
    complete_message = str(msg_length) + ',' + msg

    # return the complete message
    return complete_message


def quit_device(device_id):
    """

    :param device_id:
    :return:
    """

    # create the base message to be sent to the server
    msg = 'QUIT,' + device_id

    # get the message length and typecast it to string
    msg_len = str(len(msg))

    # return the message length concatenated with the base message
    return msg_len + ',' + msg

def log(file_dest, message):

    time_stamp = str(datetime.datetime.now())

    file = open(file_dest, 'a')

    file.write(str(message) + ',' + time_stamp + '\r\n')

    file.close()