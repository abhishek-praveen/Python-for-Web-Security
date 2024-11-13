import socket

web_host = 'localhost'
web_port = 8081

print("Contacting %s on port %d..."%(web_host,web_port))
webclient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
webclient.connect((web_host,web_port))

webclient.send(bytes("GET / HTTP/1.1\r\nHOST:localhost\r\n\r\n".encode('utf-8')))
reply = webclient.recv(4096)
print("Response from %s:"%web_host)
print(reply.decode())
               