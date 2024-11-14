from scapy.all import sniff, IP, ICMP

# Function to process and extract payload from ICMP packets
def extract_icmp_payload(packet):
    if packet.haslayer(ICMP):
        if packet[ICMP].type == 8:  # ICMP Echo Request
            payload = bytes(packet[ICMP].payload).decode(errors="ignore")
            print(f"Received covert message: {payload}")

# Sniff ICMP packets and apply the extraction function
print("Listening for covert ICMP messages...")
sniff(filter="icmp", prn=extract_icmp_payload, store=0)
