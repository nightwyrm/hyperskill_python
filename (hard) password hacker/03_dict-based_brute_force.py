import itertools
import json
import socket
import string
import sys
from pathlib import Path


symbols = string.ascii_letters + string.digits


def send_rcv(sk, log, pwd):
    sk.send(json.dumps({'login': log, 'password': pwd}).encode())
    response = json.loads(sk.recv(1024).decode())
    return response['result']


def read_file(filename):
    return Path(f'hacking/{filename}').read_text().splitlines()


def find_login(sk):
    for item in read_file('logins.txt'):
        if send_rcv(sk, item, '') in ('Wrong password!', 'Exception happened during login'):
            return item


def find_pwd(sk, log, pwd):
    for val in (itertools.product([pwd], symbols)):
        attempt = ''.join(val)
        result = send_rcv(sk, log, attempt)
        if result == 'Exception happened during login':
            pwd = attempt
        elif result == 'Connection success!':
            return attempt
    return find_pwd(sk, log, pwd)


args = sys.argv
with socket.socket() as client_socket:
    client_socket.connect((args[1].strip(), int(args[2].strip())))
    login = find_login(client_socket)
    password = find_pwd(client_socket, login, '')
    print(json.dumps({"login": login, "password": password}, indent=2))
