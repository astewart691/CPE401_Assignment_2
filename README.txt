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
I was not able to get the threading working on the client side still. Currently the code for client_one_implementation
is the same as previous submitted. There was not enough time to figure out the aws and the multithreading.

Server_implementation.py
The threading has not yet been fixed on for the project. There was not enough time to figure out the aws and
multithreading components. The code for the server_implementation has remained somewhat the same.

Client_one_supplemental.py
Client_one_supplemental has the ability to push a message to the S3 bucket CPE401. The client will push the file update to
a folder named as the device name. Once the file has been update the client will send a tcp message to the server using CLOUD.
The server will pull from the file using the device name as the path.

Server_supplemental.py
Server_supplemental.py is altered to accomodate the cloud computing component required for assignment 4. The tcp message
section was altered to accommodate the push notification from the clients. The clients will use CLOUD to notify the server
of a new update to either a ping or traceroute file. The client will include a 1 for ping and 2 for the traceroute. Having
the type of message will stop any unnecessary requests. The server will also erase the file that it pulls from. Thus stopping
redundent data from being pulled.

I was not able to get the multithreading from assignment 3 working. I figured it was more important to work out the
issues with the AWS system. I was not able to figure out how to setup tokens and there was going to be an issue with
tokens timing out from what I found. It was simpler to figure out how to set up the credentials for AWS using the command
line interface. The server does not establish the files for the clients. The setup of the files is self explanitory with how I
set the files up. Everything else was setup according to how Dr. Gunes stated in class. I was not able to figure out how to
delete the files from the server and client after uploading to the cloud. I am going to look into how to do this after the
semester is over.

