import pyshark
import pandas as pd
from joblib import load
import threading
import asyncio
import requests
import os
import time

# 🔐 Telegram Config (PUT YOUR NEW TOKEN HERE)
BOT_TOKEN = "8706116755:AAHuPYwCRtJD2nSGufYUiVcbnqGDAr-MM3E"
CHAT_ID = "1911931038"

# 🔥 TEST TELEGRAM ON START
def test_telegram():
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        response = requests.post(url, data={
            "chat_id": CHAT_ID,
            "text": "✅ Telegram Connected Successfully"
        })
        print("Telegram Test:", response.text)
    except Exception as e:
        print("Telegram Test Error:", e)

# 🔥 SEND ALERT FUNCTION (WITH DEBUG)
def send_alert(msg):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        response = requests.post(url, data={
            "chat_id": CHAT_ID,
            "text": msg
        })

        print("📨 Telegram Status:", response.status_code)
        print("📨 Telegram Response:", response.text)

    except Exception as e:
        print("❌ Telegram error:", e)

# Load model
model = load('models/anomaly_model.pkl')

running = False
stats = {"attack": 0, "normal": 0, "logs": []}

FEATURE_COLUMNS = ['packet_length', 'protocol', 'src_port', 'dst_port']

ip_activity = {}
last_alert_time = 0

def block_ip(ip):
    try:
        os.system(f'netsh advfirewall firewall add rule name="Block_{ip}" dir=in action=block remoteip={ip}')
    except:
        pass

def get_details(packet):
    try:
        return {
            "src_ip": packet.ip.src if hasattr(packet, 'ip') else "N/A",
            "dst_ip": packet.ip.dst if hasattr(packet, 'ip') else "N/A",
            "protocol": packet.transport_layer or "N/A",
            "src_port": packet[packet.transport_layer].srcport if packet.transport_layer else "N/A",
            "dst_port": packet[packet.transport_layer].dstport if packet.transport_layer else "N/A",
            "time": packet.sniff_time.strftime("%H:%M:%S")
        }
    except:
        return {}

def start_detection():
    global running, last_alert_time
    running = True

    # 🔥 TEST TELEGRAM FIRST
    test_telegram()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    print("🟢 IDS Started")

    capture = pyshark.LiveCapture(
        interface='Wi-Fi',
        bpf_filter='ip',
        tshark_path=r'D:\Wireshark\tshark.exe'
    )

    for packet in capture.sniff_continuously():
        if not running:
            break

        try:
            transport = packet.transport_layer
            if not transport:
                continue

            details = get_details(packet)
            src_ip = details.get("src_ip")

            features = {
                'packet_length': int(packet.length),
                'protocol': 1 if hasattr(packet, 'tcp') else 0,
                'src_port': int(packet[transport].srcport),
                'dst_port': int(packet[transport].dstport)
            }

            df = pd.DataFrame([features])[FEATURE_COLUMNS]

            # 🔥 Anomaly score
            score = model.decision_function(df)[0]
            anomaly = score < -0.2

            # Track behavior
            if src_ip not in ip_activity:
                ip_activity[src_ip] = {"count": 0, "ports": set()}

            ip_activity[src_ip]["count"] += 1
            ip_activity[src_ip]["ports"].add(details.get("dst_port"))

            dos = ip_activity[src_ip]["count"] > 200
            scan = len(ip_activity[src_ip]["ports"]) > 20

            if anomaly or dos or scan:

                attack_type = "Anomaly"
                if dos:
                    attack_type = "DoS"
                elif scan:
                    attack_type = "Port Scan"

                stats["attack"] += 1

                log = f"🚨 {attack_type} | {src_ip} → {details.get('dst_ip')}"
                stats["logs"].insert(0, log)

                if len(stats["logs"]) > 100:
                    stats["logs"].pop()

                print(log)

                # 🔥 SEND ALERT EVERY TIME (for testing)
                send_alert(log)

                # 🔒 Block only serious
                if dos or scan:
                    block_ip(src_ip)

            else:
                stats["normal"] += 1

        except Exception as e:
            print("Error:", e)

def stop_detection():
    global running
    running = False

def run_thread():
    threading.Thread(target=start_detection, daemon=True).start()
