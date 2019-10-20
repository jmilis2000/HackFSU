import socket

HOST = '35.196.213.53'
PORT = 6663
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print('Hi')