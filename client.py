import sys
import socket

HOST = sys.argv[1]
PORT = sys.argv[2]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
    soc.connect((HOST, PORT))
    soc.sendall(b'Hello')
    data = soc.recv(1024)

print(f"Recived data: {data!r}")