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
# source file: p1804247Server.py
# This is the server program that repsonds to client's request
# import all data from p1804247Helper.py
from p1804247Helper import * 

while True:
    print("waiting a new call at accept()")
    connection, address = serversocket.accept()# accpet incoming request from client
    if handler(connection) == 'x': #if client press 'x', the server will close
        break; 
serversocket.close()
print("Server stops")
