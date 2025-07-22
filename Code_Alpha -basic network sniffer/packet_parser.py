from scapy.all import IP, TCP, UDP, ICMP

def parse_packet(packet):
    parsed_data = {
        'src_ip': None,
        'dst_ip': None,
        'protocol': None,
        'payload': None
    }

    if IP in packet:
        ip_layer = packet[IP]
        parsed_data['src_ip'] = ip_layer.src
        parsed_data['dst_ip'] = ip_layer.dst

        if TCP in packet:
            parsed_data['protocol'] = 'TCP'
        elif UDP in packet:
            parsed_data['protocol'] = 'UDP'
        elif ICMP in packet:
            parsed_data['protocol'] = 'ICMP'
        else:
            parsed_data['protocol'] = 'Other'

        parsed_data['payload'] = bytes(packet.payload)
    
    return parsed_data
