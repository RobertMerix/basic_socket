#!/usr/bin/env python3

import socket
import time
# import sys

# means of communication will always be Internet.
via_internet = socket.AF_INET

tcp_protocol = socket.SOCK_STREAM

my_socket = socket.socket(via_internet, tcp_protocol)

# On a separate shell window you have to activate your server (raspberrypi) before executing this script 
# by entering the following command 'nc -l 1234' on the server side.
# 'nc' stands for NetCat, '-l' means listen, and '1234' its a random port
# we've given to the the server to listen to.

IP_HOST = "192.168.1.183"
PORT = 1234

my_socket.connect((IP_HOST, PORT))

# data = str(sys.argv[1])

#my_socket.sendall(b"sending info...")

while True:
    my_socket.sendall(b"sending coordinates: -95.23562, 84.25735\n")
    time.sleep(2.5)




