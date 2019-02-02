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
#source file: simClient.py
import socket
import time as t
import datetime as d
import sys
start_time = t.time()
def getnewsocket():
	return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientsocket = getnewsocket()
host = "localhost"
clientsocket.connect((host, 8089))	


while True:
 if len(sys.argv) != 2:
          print("Usage => ./simClient \"CITY NAME\"")
          print("Bye Bye")
          break   
 else:
         msg = sys.argv[1]   
         obuf = msg.encode() # convert msg string to bytes
         clientsocket.send(obuf)
         ibuf = clientsocket.recv(5000)
         if len(ibuf) > 0:
            ti = d.datetime.now()
            print("\n")
            print(ti.strftime("%a %b %d %H:%M:%S"))
            print(ibuf.decode())
            td = d.datetime.now()
            print(td.strftime("%a %b %d %H:%M:%S"))
            print("See You Again")
            clientsocket.close()
            break  
         else:
            print("The connection has dropped")
            break
 print("Bye Bye")
 

