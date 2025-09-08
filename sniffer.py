from scapy.all import sniff, IP, TCP, UDP
from collections import defaultdict
import time
from database import init_db, log_packet
from alerts import send_alert

# Initialize DB
conn, cursor = init_db()

traffic = defaultdict(list)  # store timestamps
THRESHOLD_PACKETS = 50
TIME_WINDOW = 10

def detect_anomaly(src):
    now = time.time()
    traffic[src].append(now)
    traffic[src] = [t for t in traffic[src] if now - t < TIME_WINDOW]
    if len(traffic[src]) > THRESHOLD_PACKETS:
        return True
    return False

def packet_callback(packet):
    if IP in packet:
        src, dst = packet[IP].src, packet[IP].dst
        length = len(packet)
        proto, sport, dport = "Other", None, None

        if TCP in packet:
            proto, sport, dport = "TCP", packet[TCP].sport, packet[TCP].dport
        elif UDP in packet:
            proto, sport, dport = "UDP", packet[UDP].sport, packet[UDP].dport

        print(f"{src} -> {dst}, {proto}, {sport}->{dport}, len={length}")
        log_packet(cursor, conn, src, dst, proto, sport, dport, length)

        if detect_anomaly(src):
            print(f"[ALERT] Possible flooding from {src}")
            send_alert(src)

print("[*] Starting packet sniffer...")
sniff(prn=packet_callback, store=0)
