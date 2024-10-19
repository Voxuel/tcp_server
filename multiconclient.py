import sys
import socket
from types import SimpleNamespace
from selectors import EVENT_READ, EVENT_WRITE, DefaultSelector

sel = DefaultSelector()
byte_message_array = [b"Message 1 from client", b"Message 2 from client"]
host, port, num_conns = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])


def start_connection(host, port, num_conns):
    server_addr = (host, port)
    for i in range(0, num_conns):
        connid = i + 1
        print(f"Starting connection {connid} to {server_addr}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addr)
        events = EVENT_WRITE | EVENT_READ
        data = SimpleNamespace(
            connid=connid,
            msg_total=sum(len(m) for m in byte_message_array),
            recv_total=0,
            messages=byte_message_array.copy(),
            outb=b""
        )
        sel.register(sock, events=events, data=data)
        
if __name__ == "__main__":
    start_connection(host=host, port=port, num_conns=num_conns)