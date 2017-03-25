"""
Project: CPE 401 Assignment2
File: server_supplemental.py
Author: Aarron Stewart
"""
import datetime as datetime

SUCCESSFUL = 'activity.log'
ERROR = 'error.log'


def process_client(soc, address, registration, mailbox):
    run = True

    while run:

        data = soc.recv(1024)

        if data != '':

            # decode, strip and split the message to allow for message processing
            data = data.decode()

            data = data.strip()

            data = data.split(',')

            if data[1] == 'QUIT' or data[1] == 'DEREGISTER':

                run = False

            print(data)
            # process the message to perform the appropriate action and return the appropriate response for the client
            reply = message_received(registration, mailbox, data, address)

            # print reply to console for easy debugging
            print(reply)

            # sent the reply that has been encoded to bytes to the client
            soc.send(reply.encode())

    print('exiting function')
    soc.close()


def message_received(reg_table, mailbox_cont, msg, address):
    """

    :param reg_table:
    :param mailbox_cont:
    :param msg:
    :param address:
    :return:
    """

    # assign the message type to the variable msg_type
    msg_type = msg[1]

    # use if statements to test which message type is sent. If the message type is valid process the message.
    # If the message is invalid send a NACK
    if msg_type == 'REGISTER':

        return register_device(reg_table, mailbox_cont, msg[2], msg[3], address[0], address[1])

    elif msg_type == 'DEREGISTER':

        return deregister_device(reg_table, mailbox_cont, msg[2], msg[3])

    elif msg_type == 'MSG':

        return receive_msg(mailbox_cont, msg[2], msg[3], msg[4])

    elif msg_type == 'QUERY':

        return receive_query(reg_table, mailbox_cont, msg[2], msg[3])

    elif msg_type == 'QUIT':

        return quit_device(reg_table, msg[2])

    else:

        # build NACK message with appropriate type
        code = '0'

        msg = 'NACK' + ',' + code

        msg_length = len(msg)

        complete_message = str(msg_length) + ',' + msg

        log(ERROR, complete_message)

        return complete_message


def register_device(table, mailbox, device, mac, ip, port):
    """

    :param table:
    :param mailbox:
    :param device:
    :param mac:
    :param ip:
    :param port:
    :return:
    """

    # test to see if the table is empty
    if len(table) != 0:

        # loop across the registration table to see if the device_id or mac_address is registered already
        for index in range(0, len(table)):

            # test to see if the device_id is registered already
            if table[index]["device_id"] == device:

                # test to see if the device had quit previously
                if table[index]["ip_address"] == 0:

                    # assign the current IP address
                    table[index]["ip_address"] = ip

                    # assign the current port number
                    table[index]["port_number"] = str(port)

                    # get the current messages waiting to be delivered to the device
                    count = str(mailbox[index]["count"])

                    # build ACK message with appropriate type
                    code = '2'

                    msg = 'ACK' + ',' + code + ',' + device + ',' + count

                    msg_length = len(msg)

                    complete_message = str(msg_length) + ',' + msg

                    log(SUCCESSFUL, complete_message)

                    return complete_message

                else:

                    # build NACK message with appropriate type
                    code = '1'

                    msg = 'NACK' + ',' + code + ',' + device

                    msg_length = len(msg)

                    complete_message = str(msg_length) + ',' + msg

                    log(ERROR, complete_message)

                    return complete_message

            # test to see if the device is registered to the correct mac address
            elif table[index]["mac_address"] == mac:

                code = '2'

                # build NACK message with appropriate type
                msg = 'NACK' + ',' + code + ',' + table[index]["device_id"]

                msg_length = len(msg)

                complete_message = str(msg_length) + ',' + msg

                log(ERROR, complete_message)

                return complete_message

        # append the correct device information to the registration table
        table.append({"device_id": device, "mac_address": mac, "ip_address": ip, "port_number": port})

        # append the mailbox information to the mailbox with the correct device_id
        mailbox.append({"device_id": device, "count": 0, "message": []})

        # build ACK message with appropriate type
        code = '1'

        msg = 'ACK' + ',' + code + ',' + device

        msg_length = len(msg)

        complete_message = str(msg_length) + ',' + msg

        log(SUCCESSFUL, complete_message)

        return complete_message

    else:

        # append the correct device information to the registration table
        table.append({"device_id": device, "mac_address": mac, "ip_address": ip, "port_number": port})

        # append the mailbox information to the mailbox with the correct device_id
        mailbox.append({"device_id": device, "count": 0, "message": []})

        # build ACK message with appropriate type
        code = '1'

        msg = 'ACK' + ',' + code + ',' + device

        msg_length = len(msg)

        complete_message = str(msg_length) + ',' + msg

        log(SUCCESSFUL, complete_message)

        return complete_message


def deregister_device(table, mailbox, device, mac):
    """

    :param table:
    :param mailbox:
    :param device:
    :param mac:
    :return:
    """

    # initialize the index variable
    index = 0

    # test to see if the registration table is empty
    if len(table) != 0:

        # loop across the registration table to find the devices index location
        while table[index]["device_id"] != device:

            # increment the index
            index += 1

            # test to see if the end of the list has been reached
            if index >= len(table):

                # build NACK message with appropriate type
                code = '4'

                msg = 'NACK' + ',' + code + ',' + device

                msg_length = len(msg)

                complete_message = str(msg_length) + ',' + msg

                log(ERROR, complete_message)

                return complete_message

        # test to see if the correct mac address is assigned sent with the device_id
        if table[index]["mac_address"] == mac:

            # delete the table index found
            del table[index]

            # delete the mailbox location found
            del mailbox[index]

            # build ACK message with appropriate type
            code = '3'

            msg = 'ACK' + ',' + code + ',' + device

            msg_length = len(msg)

            complete_message = str(msg_length) + ',' + msg

            log(SUCCESSFUL, complete_message)

            return complete_message

        else:

            # build NACK message with appropriate type
            code = '3'

            msg = 'NACK' + ',' + code + ',' + table[index]["device_id"]

            msg_length = len(msg)

            complete_message = str(msg_length) + ',' + msg

            log(ERROR, complete_message)

            return complete_message

    else:

        # build ACK message with appropriate type
        code = '4'

        msg = 'ACK' + ',' + code + ',' + device

        msg_length = len(msg)

        complete_message = str(msg_length) + ',' + msg

        log(SUCCESSFUL, complete_message)

        return complete_message


def receive_msg(mailbox, sender_id, recipient_id, message):

    # initialize the index variable
    index = 0

    # get the current date and time values for the incoming message
    time_stamp = datetime.datetime.now()

    # convert the time_stamp variable to a string
    time_stamp = str(time_stamp)

    # test to see if the mailbox is empty
    if len(mailbox) == 0:

        # build NACK message with appropriate type
        code = '4'

        msg = 'NACK' + ',' + code + ',' + recipient_id

        msg_length = len(msg)

        complete_message = str(msg_length) + ',' + msg

        log(ERROR, complete_message)

        return complete_message

    # loop across the mailbox until the correct recipient is found.
    while mailbox[index]["device_id"] != recipient_id:

        # increment the index
        index += 1

        # test to see if the end of the list has been reached
        if index >= len(mailbox):

            # build NACK message with appropriate type
            code = '4'

            msg = 'NACK' + ',' + code + ',' + recipient_id

            msg_length = len(msg)

            complete_message = str(msg_length) + ',' + msg

            log(ERROR, complete_message)

            return complete_message

    # append the new message into the message section of the mailbox dictionary with the time_stamp variable.
    mailbox[index]['message'].append(sender_id + ',' + recipient_id + ',' + message + ',' + time_stamp)

    # increment the mailbox count to reflect the new message
    mailbox[index]['count'] += 1

    # build ACK message with appropriate type
    code = '5'

    msg = 'ACK' + ',' + code + ',' + sender_id + ',' + time_stamp

    msg_length = len(msg)

    complete_message = str(msg_length) + ',' + msg

    log(SUCCESSFUL, complete_message)

    return complete_message


def receive_query(table, mailbox, code, device_id):

    # initialize the index variable
    index = 0

    # test to see if the registration table is empty
    if len(table) == 0:

        # build NACK message with appropriate type
        code = '4'

        msg = 'NACK' + ',' + code + ',' + device_id

        msg_length = len(msg)

        complete_message = str(msg_length) + ',' + msg

        log(ERROR, complete_message)

        return complete_message

    else:

        # loop across the registration table until the device_id is found
        while table[index]["device_id"] != device_id:

            # increment index
            index += 1

            # test to see if the end of the table was found
            if index >= len(table):

                # build NACK message with appropriate type
                code = '4'

                msg = 'NACK' + ',' + code + ',' + device_id

                msg_length = len(msg)

                complete_message = str(msg_length) + ',' + msg

                log(ERROR, complete_message)

                return complete_message

    # test to see which kind of query needs to be processed
    if code == '1':

        # build ACK message with appropriate type
        return_code = '6'

        # return the device_id, ip_address and port number of the device
        msg = 'ACK' + ',' + return_code + ',' + device_id + ',' + table[index]['ip_address'] + ',' + str(table[index]["port_number"])

        msg_length = len(msg)

        complete_message = str(msg_length) + ',' + msg

        log(SUCCESSFUL, complete_message)

        return complete_message

    # test to see which kind of query needs to be processed
    elif code == '2':

        # build ACK message with appropriate type
        return_code = '7'

        # return the device_id and the mailbox count
        msg = 'ACK' + ',' + return_code + ',' + device_id + ',' + str(mailbox[index]["count"])

        msg_length = len(msg)

        complete_message = str(msg_length) + ',' + msg

        log(SUCCESSFUL, complete_message)

        return complete_message

    # return a nack due to the code not being valid
    else:

        # build NACK message with appropriate type
        code = '4'

        msg = 'NACK' + ',' + code + ',' + device_id

        msg_length = len(msg)

        complete_message = str(msg_length) + ',' + msg

        log(ERROR, complete_message)

        return complete_message


def quit_device(table, device):
    """

    :param table:
    :param device:
    :return:
    """

    # initialize variables
    index = 0

    # test to see if the registration table is empty
    if len(table) == 0:

        # build NACK message with appropriate type
        code = '4'

        msg = 'NACK' + ',' + code + ',' + device

        msg_length = len(msg)

        complete_message = str(msg_length) + ',' + msg

        log(ERROR, complete_message)

        return complete_message

    else:

        # loop across the registration table until the device_id is found
        while table[index]["device_id"] != device:

            # increment the index
            index += 1

            # test to see if the end of the table has been found
            if index >= len(table):

                # build NACK message with appropriate type
                code = '4'

                msg = 'NACK' + ',' + code + ',' + device

                msg_length = len(msg)

                complete_message = str(msg_length) + ',' + msg

                log(ERROR, complete_message)

                return complete_message

        # replace the ip_address of the device_id to zero
        table[index]["ip_address"] = 0

        # build ACK message with appropriate type
        code = '8'

        msg = 'ACK' + ',' + code + ',' + device

        msg_length = len(msg)

        complete_message = str(msg_length) + ',' + msg

        log(SUCCESSFUL, complete_message)

        return complete_message


def log(file_dest, message):

    time_stamp = str(datetime.datetime.now())

    file = open(file_dest, 'a')

    file.write(message + ',' + time_stamp + '\r\n')

    file.close()
