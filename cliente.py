import socket
import sys
import time

ip = "127.0.0.1"
prt = 5000

if len(sys.argv) > 1:
    no = sys.argv[1]
else:
    no = input("ID do Nó: ").strip()

sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = "PING" + no
    sck.sendto(msg.encode("utf-8"), (ip, prt))
    print(f"Enviado: {msg}")
    time.sleep(3)