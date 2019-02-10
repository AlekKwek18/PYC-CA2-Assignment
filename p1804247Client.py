#!/usr/bin/env python3
# ==============================================================
# SINGAPORE POLYTECHNIC                                        |
# SCHOOL OF COMPUTING                                          |
# ST2411                                                       |
# PROGRAMMING IN PYTHON AND C                                  |
# NAME: ALEK KWEK                                              |
# CLASS: DISM/FT/1A/23                                         |
# ADMIN NO: 1804247                                            |
# YEAR: 2019                                                   |
# ==============================================================
# source file: p1804247Client.py
# ASSIGNMENT OUTLINE 
# This application is a continuation of the assignment 1
# and simulate the sales summary reporting in a networking mode.
# The application enables the users to request the sales summary of a city through a client to the server, 
# then print out an overall summary of the sales report for that city.
# The input data consists of city name
# The application enables the users view the sales data of a city.
# Note that the sales summary for each city is stored in this directory
# /home/st2411/Misc/reports/
# To compile the program
# STEP 1 : ./p1804247Server.py OR python3 p1804247Server.py
# STEP 2 : ./p1804247Client.py OR python3 p1804247Client.py
# supporting files
# p1804247Helper.py

import socket
import sys
# Create new socket for network connection
def getnewsocket():
	return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientsocket = getnewsocket() # activate the function
host = "localhost" # let host be the localhost, which is this machine
# Do a try except to catch any exceptions
try:
        # for clientsocket.connect, if the host is not switch on, connecting to the host will return a
        # ConnectionRefusedError
        clientsocket.connect((host, 8089)) # connect to server with port number 8089
except ConnectionRefusedError:
        # If the error exist, tell the client that the server is not avaliable
        print("Server is not avaliable. Please try again later")
        quit()

while True:
 if len(sys.argv) != 2: #check if command line arugment is equal to 2
          print("Usage => ./simClient \"CITY NAME\"")#tell client the instruction on how to use the program
          print("Bye Bye")
          break   
 else:
         msg = sys.argv[1]   #extract city from the second arugemnt
         obuf = msg.encode() # convert msg string to bytes
         clientsocket.send(obuf) # send to the server
         ibuf = clientsocket.recv(5000) #receive output with a buffer of 5000
         if len(ibuf) > 0: # check if there is data
            print(ibuf.decode()) #decode the packet and print the output
            clientsocket.close() #close the socket
            break  
         else:
            print("The connection has dropped")
            break
 print("Bye Bye")
 