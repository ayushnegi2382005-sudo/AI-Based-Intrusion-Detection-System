from scapy.all import sniff, TCP
import pandas as pd
import os
from datetime import datetime

# Create data folder automatically
os.makedirs("data", exist_ok=True)

data = []

def process_packet(packet):
    try:
        row = {
            'packet_length': len(packet),
            'protocol': 1 if TCP in packet else 0,
            'src_port': packet[TCP].sport if TCP in packet else 0,
            'dst_port': packet[TCP].dport if TCP in packet else 0,
            'timestamp': datetime.now().isoformat()
        }
        data.append(row)
    except:
        pass

print("🔴 Capturing 100 packets...")

# Capture only IP packets
sniff(prn=process_packet, count=100, filter="ip")

df = pd.DataFrame(data)
df['label'] = 0

file_path = 'data/live_captured_data.csv'

# Save file
df.to_csv(file_path, index=False)

print(f"✅ Data saved: {len(df)} packets")
