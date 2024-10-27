import socket
import sys

def banner(ip,port):
    try:
        s = socket.socket()
        s.connect((ip,int(port)))
        s.settimeout(5)
        print(str(s.recv(1024)).strip('b'))
    except KeyboardInterrupt:
        print("\n Exiting...")
        sys.exit()
    except ConnectionRefusedError:
        print("\n Connection refused...")
    except TimeoutError:
        print("\n Connection timed out..." )



def main():
    ip = input("Enter IP address: ")
    port = str(input("Enter port number: "))
    banner(ip,port)

main()
