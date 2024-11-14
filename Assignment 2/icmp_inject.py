from scapy.all import IP, ICMP, send
import time


victim_ip = "192.168.56.102" 

# Message to embed in ICMP packets
message = "Covert Channel Using ICMP"

# Send ICMP packets with the message embedded in the payload
for i in range(5):  # Adjust the range for the number of packets
    packet = IP(dst=victim_ip) / ICMP(type="echo-request") / message
    send(packet)
    print(f"Sent covert ICMP packet {i+1} with message.")
    time.sleep(1)  # Add delay to avoid detection due to high packet rate
