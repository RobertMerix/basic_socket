#!/usr/bin/env python3

# THIS IS AN ACTING SERVER LISTENING FOR ANY CLIENT CONNECTIONS AT A GIVEN PORT


import socket


via_internet = socket.AF_INET
tcp_protocol = socket.SOCK_STREAM

my_socket = socket.socket(via_internet, tcp_protocol, 0)


# listening for any incoming IP Address.
unk_ip_add = None
# Which port?
random_port = 1234

add_info = socket.getaddrinfo(unk_ip_add, random_port)
print(add_info[2][4])

my_socket.bind(add_info[2][4])

# the number inside the 'listen' method is a 'backlog',
# it specifies the number of unaccepted connections (connections waiting in line)
# that the system will allow before refusing new connections.
my_socket.listen(5)


conn, addr = my_socket.accept()






