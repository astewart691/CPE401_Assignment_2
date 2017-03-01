"""
Project: CPE 401 Assignment2
File: server_supplemental.py
Author: Aarron Stewart
"""


def message_received(reg_table, mailbox_cont, msg, address):

    msg_type = msg[1]

    if msg_type == 'REGISTER':

        return register_device(reg_table, mailbox_cont, msg[2], msg[3], address[0], address[1])

    elif msg_type == 'DEREGISTER':

        return deregister_device( reg_table, mailbox_cont, msg[2], msg[3])

    elif msg_type == 'MSG':

        return

    elif msg_type == 'QUERY':

        return

    elif msg_type == 'QUIT':

        return quit_device(reg_table, msg[2])

    else:

        return


def register_device( table, mailbox, device, mac, ip, port):

    if len(table) != 0:

        for index in range(0, len(table)):

            if table[index]["device_id"] == device:

                if table[index]["ip_address"] == 0:

                    table[index]["ip_address"] = ip

                    table[index]["port_number"] = port

                    return "ack, device reentered"

                else:

                    return "nack, device name registered already"

            elif table[index]["mac_address"] == mac:

                if table[index]["ip_address"] == 0:

                    table[index]["ip_address"] = ip

                    table[index]["port_number"] = port

                    return "ack"

                else:

                    return "nack"

            else:
                table.append({"device_id": device, "mac_address": mac, "ip_address": ip, "port_number": port})
                mailbox.append({"device_id": device, "count": 0, "message": [], "time": None})
                return "ack"

    else:

        table.append({"device_id": device, "mac_address": mac, "ip_address": ip, "port_number": port})
        mailbox.append({"device_id": device, "count": 0, "message": [], "time": None})
        return "ack, device registered"


def deregister_device(table, mailbox, device, mac):

    index = 0

    if len(table) != 0:

        while table[index]["device_id"] != device:

            index += 1

            if index + 1 == len(table):

                return "nack"

        if table[index]["mac_address"] == mac:

            del table[index]
            del mailbox[index]
            return "ack, device removed"

        else:
            return "nack"

    else:
        return 'nack'

def quit_device(table, device):

    index = 0

    if len(table) == 0:

        return 'nack'

    else:
        while table[index]["device_id"] != device:

            index += 1

            if index > len(table):

                return 'nack'

        table[index]["ip_address"] = 0

        return 'ack, device quit properly'
