import socket
import sys

def banner(ip,port):
    try:
        s = socket.socket()
        s.connect((ip,int(port)))
        s.settimeout(5)
        print((s.recv(1024)).decode('utf-8').strip())
        s.close()
    except KeyboardInterrupt:
        print("\n Exiting...")
        sys.exit()
    except ValueError:
        print("\nInvalid Port number. Enter port number as integer. ")
    except ConnectionRefusedError:
        print("\n Connection refused...")
    except TimeoutError:
        print("\n Connection timed out..." )
    except Exception as e:
        print(f"\nAn error occurred:{e}")



def main():
    ip = input("Enter IP address: ")
    port = str(input("Enter port number: "))
    banner(ip,port)

main()
