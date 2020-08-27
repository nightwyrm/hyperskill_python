import socket
import sys


args = sys.argv
with socket.socket() as client_socket:
    hostname = args[1]
    port = int(args[2])
    pwd = args[3].encode()
    client_socket.connect((hostname, port))
    client_socket.send(pwd)
    response = client_socket.recv(1024)
    print(response.decode())
