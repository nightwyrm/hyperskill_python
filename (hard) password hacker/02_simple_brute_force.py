import itertools
import socket
import string
import sys


symbols = string.ascii_lowercase + string.digits


def generate_password():
    for length in range(1, len(symbols) + 1):
        for item in itertools.product(symbols, repeat=length):
            yield ''.join(item)


args = sys.argv
with socket.socket() as client_socket:
    client_socket.connect((args[1], int(args[2])))
    poss_values = generate_password()
    for attempt in poss_values:
        password = ''.join(attempt)
        client_socket.send(password.encode())
        response = client_socket.recv(1024)
        if response.decode() == 'Connection success!':
            print(password)
            exit()
