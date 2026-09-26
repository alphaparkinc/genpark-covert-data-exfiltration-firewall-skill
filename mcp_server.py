import json, sys
from client import CovertDataExfiltrationFirewallClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "covert-data-exfiltration-firewall", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "inspect_egress_payload", "description": "Inspects outbound agent egress requests for leaked secrets, API keys, and obfuscated data exfiltration."}]}}
    elif method == "tools/call":
        client = CovertDataExfiltrationFirewallClient()
        res = client.inspect_egress_payload()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = CovertDataExfiltrationFirewallClient()
        print(json.dumps(client.inspect_egress_payload(), indent=2))
