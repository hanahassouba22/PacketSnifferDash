import random
from collections import Counter

# Simulate network packet capture
protocols = ['TCP', 'UDP', 'HTTP', 'HTTPS', 'DNS', 'SSH']
ips = ['192.168.1.', '10.0.0.', '172.16.', '8.8.8.8']

def capture_packets(count=50):
    packets = []
    for _ in range(count):
        packets.append({
            'protocol': random.choice(protocols),
            'src_ip': random.choice(ips) + str(random.randint(1,255)),
            'dst_ip': random.choice(ips) + str(random.randint(1,255))
        })
    return packets

# Analyze + dashboard
packets = capture_packets()
proto_count = Counter(p['protocol'] for p in packets)
ip_count = Counter(p['src_ip'] for p in packets)

print("📊 NETWORK TRAFFIC DASHBOARD")
print("="*40)
print("Top Protocols:")
for proto, count in proto_count.most_common(5):
    print(f"  {proto}: {'█' * (count//2)} {count}")
print(f"\nTop IPs:")
for ip, count in ip_count.most_common(5):
    print(f"  {ip}: {count}")
