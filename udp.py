
import socket, time
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dst = ("127.0.0.1", 9999)
for i in range(80):   # adjust to trigger threshold
    s.sendto(b"test"+bytes(str(i),'utf-8'), dst)
    time.sleep(0.05)
print("done")
