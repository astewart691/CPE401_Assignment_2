CPE 401: Assignment 2
Created by Aarron Stewart
Due March 1, 2017

Included files:
server_implementation.py
    The implementation the the base server functionality which is where the socket is created and data is received.
server_supplemental.py
    The supplemental file is where the actual functionality of the server found. The functions are located in this file.
client_one_implementation.py
    The implementation is where the client side creates a socket and uses an API like function to generate the appropriate message.
client_one_supplemental.py
    The supplemental file is where the API like functions are located. These functions generate the appropriate message for the server.

The initial design and implementation of the implementation of the server and clients is from the python lectures in class.

Client_one_implementation.py
I created this file and forgot that I closed the socket after each run. I do not have time to figure out the blocking for the
the receive. There will be a function created to handle the appropraite response from the server. Like closing the connection
will occur after the device is deregistered and after quiting. I need to speak with Dr. Gunes or the TA about how to handle the
blocking till a response is created. Thus I also do not have the three 10 second delays created for waiting for an ack from the
server

Server_implementation.py
I believe that full functionality of the server implementation has been achieved. The main issue that I currently will need to
deal with will be figuring out the ability to deal with the sockets once they have been left open. I did not notice that I
closed the socket after each message in the client.

Client_one_supplemental.py
Client_one_supplemental.py is where the functions that create the appropriate message are created. Each message is created
using a specific set of parameters for each type of message. The log function was created with a typecast list to string.
I will fix the function to eliminate the list specification when printed. A new function will be created to handle the
closing of sockets and other functionality using the ack messages from the server.

Server_supplemental.py
Server_supplemental.py is almost complete. I need to do more testing of some of the functions. I believe that Register
and Deregister maybe have some logic issues but needs to be tested to verify. Once I have the client side fixed I will
run multiple clients and test the logic for wrong mac addresses and other items that is difficult to produce individually.
In terms of functions, there are a few items that can be put into functions like finding the index of a device and
creating the response for the client and logging. Moving the message generation and logging into one function will make
the code more readable.

Unfortunately, I wasted a large amount of time when trying to figure out how to get the mac address from the data link layer.
The professor gave some requirement without actually knowing if we could implement the requirement. Another large amount of time
 was trying to figure out how to turn a string into a bytes. There were multiple options and I believe the encoding and
 decoding will be a good option but it limits the ability to have anything other than strings. I would like to discuss
 possible options with Dr. Gunes or the TA during the meeting. Also I have been stumped in terms of figuring out how to
 handle the read block for the client side. I have not had time to try implementing this on an actual raspberry pi 3
 like I wanted.

