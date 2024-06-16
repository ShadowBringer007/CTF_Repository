import socket

host = "mercury.picoctf.net"
port = 22902

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    data = s.recv(1024).decode().split()

    #print(data)


for i in data:
    print(f'{chr(int(i))}', end="")
input()
