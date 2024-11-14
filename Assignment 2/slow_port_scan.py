import random
import time
from scapy.all import IP, TCP, sr1


victim_ip= "192.168.56.102"    # (victim machine)

ports = range(20, 30)    #  ( common ports 20-30)

# Perform a slow port scan with random delays
for port in ports:
    packet = IP(dst=victim_ip)/TCP(dport=port, flags="S")
    response = sr1(packet, timeout=1, verbose=0)
    
    # Check if the port is open based on the response
    if response is not None and response.haslayer(TCP):
        if response.getlayer(TCP).flags == 0x12:  # SYN-ACK received
            print(f"Port {port} is open on {victim_ip}")
        elif response.getlayer(TCP).flags == 0x14:  # RST received
            print(f"Port {port} is closed on {victim_ip}")
    else:
        print(f"Port {port} is filtered or closed on {victim_ip}")
    
    # Random delay between 1 and 5 seconds to avoid detection
    time.sleep(random.uniform(1, 5))
