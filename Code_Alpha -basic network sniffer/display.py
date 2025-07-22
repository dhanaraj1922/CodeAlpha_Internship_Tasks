def display_packet(parsed_data):
    print("="*50)
    print(f"Source IP      : {parsed_data['src_ip']}")
    print(f"Destination IP : {parsed_data['dst_ip']}")
    print(f"Protocol       : {parsed_data['protocol']}")
    print(f"Payload        : {parsed_data['payload'][:100]}")
