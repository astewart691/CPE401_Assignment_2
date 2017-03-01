"""
Project: CPE 401 Assignment2
File: client_one_supplemental.py
Author: Aarron Stewart
"""

'''
def register_device(device_id, mac_add, ip_add, port_num):
    device = str(device_id)
    mac = str(mac_add)
    ip = str(ip_add)
    port = str(port_num)

    msg = (device, mac, ip, port)

    msg_length = len(msg)

    return zip(msg_length, msg)
'''


def register_device(device_id, mac_add):

    device = str(device_id)

    mac = str(mac_add)

    msg = "REGISTER" + ',' + device + ',' + mac

    msg_length = len(msg)

    complete_message = str(msg_length) + ',' + msg

    return str(complete_message)


def deregister_device( device_id, mac_add):

    device = str(device_id)

    mac = str(mac_add)

    msg = "DEREGISTER" + ',' + device + ',' + mac

    msg_length = len(msg)

    complete_message = str(msg_length) + ',' + msg

    return complete_message


def quit_device(device_id):

    msg = 'QUIT,' + device_id

    msg_len = str(len(msg))

    return msg_len + ',' + msg
