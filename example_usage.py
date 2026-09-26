import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import CovertDataExfiltrationFirewallClient

def main():
    client = CovertDataExfiltrationFirewallClient()
    res = client.inspect_egress_payload()
    print("=== Covert Data Exfiltration Firewall Output ===")
    print(f"Destination: {res['destination_url']} | Size: {res['payload_size_bytes']} bytes")
    print(f"Exfiltration Detected: {res['exfiltration_detected']} (Verdict: {res['firewall_verdict']})")
    print(f"Action: {res['recommended_action']}")
    if res['flagged_leak_details']:
        print("\nLeaks Intercepted:")
        for l in res['flagged_leak_details']:
            print(f"  * [{l['type']}] ({l['encoding']})")

if __name__ == '__main__':
    main()
