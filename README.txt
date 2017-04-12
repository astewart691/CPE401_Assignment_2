CPE 401: Assignment 3
Created by Aarron Stewart
Due March 27, 2017

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
The bulk of the code was moved to the client_one_supplemental.py file. The main issue is that the activity and error logging
has been taken away until I can finish fixing the menu setup for the program. Once that is completed I will incorporate the
logging for each of the sections. Also I was not able to get the threads to work properly.

Server_implementation.py
The general implementation for the server_implementation.py file is essectially the same as Assignment 2. The issue of not being
able to maintain a connection with a client has been fix. I created a function that should create a thread whenever a new client
creates a connection. I do believe that it cannot handle two connections at a time. I think that I made a mistake with the thread
in the program. I need to talk to the TA about it and get some advice.

Client_one_supplemental.py
Client_one_supplemental.py is where the functions that create the appropriate message are created. The main message creation
is used from the Assignment 2 code. I worked on developing a menu and more user friendly way of implementing the code. I was
not able to create all of the menu functions due to a limited amount of time that was available. The ability to send a message
via UDP was created but I am having trouble dealing with the receiving. I need to talk to the TA about how I am doing it and what
he thinks would be the most appropriate way to fix it. The function for sending the UDP datagram can send and receive a basic
message to itself on a local host. The send function does not currently have the timer built into the function yet for the 30
seconds of attempts.

Server_supplemental.py
I believe that I fixed the logic issue with the register function. I did create a function to handle the continious communication
with a client. The bulk of the server code was working correctly.

I spent most of the time trying to deal with the server client connection. I could not figure out why the connection was not
continuous. I could not get the threading to work properly. I created a thread for the main server but when I attempted to
use two connections it would only process one at a time. I am going to talk the TA about what I need to do to get it working.
I was not able to figure out how to get Traceroute and ping to work inside of the program so I started to work on the UDP
connection. On the client side I did not have a chance to get the Treads to work. I need to make a class for the thread but did
not have time to work on it. There was a lot of things that needed to be implemented on this project with little time. The code does
compile but it does have some issues.

