from scapy.all import sniff
from packet_parser import parse_packet
from display import display_packet

def packet_callback(packet):
    parsed_data = parse_packet(packet)
    if parsed_data['src_ip']:
        display_packet(parsed_data)

def start_sniffing():
    print("[*] Starting packet capture... Press Ctrl+C to stop.")
    sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    start_sniffing()
