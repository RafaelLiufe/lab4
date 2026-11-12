import socket
import threading
import time

ip = "127.0.0.1"
prt = 5000

reg = {}
est = {}
lck = threading.Lock()

def chk():
    while True:
        time.sleep(1)
        atu = time.time()
        with lck:
            chv = list(reg.keys())
            for i in range(len(chv)):
                no = chv[i]
                if atu - reg[no] > 8 and est[no]:
                    print(f"[ALERTA] O Nó {no} está OFFLINE!")
                    est[no] = False

sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sck.bind((ip, prt))
thr = threading.Thread(target=chk, daemon=True)
thr.start()

print(f"Servidor ativo em {ip}:{prt}...")

while True:
    dad, end = sck.recvfrom(1024)
    msg = dad.decode("utf-8").strip()
    
    if msg.startswith("PING"):
        no = msg[4:].strip()
        with lck:
            reg[no] = time.time()
            est[no] = True
        print(f"Sinal recebido de {no}")