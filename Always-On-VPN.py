import subprocess
import time

vpn_name = "VPN connection name"  # Replace it with the name of your VPN connection
check_interval = 30  # Connection verification interval in seconds

def is_vpn_connected(vpn_name):
    try:
        result = subprocess.run(
            ["powershell", "-Command", f"Get-VpnConnection -Name '{vpn_name}' | ConvertTo-Json"],
            capture_output=True, text=True
        )
        import json
        vpn_info = json.loads(result.stdout)
        return vpn_info.get("ConnectionStatus", "").lower() == "connected"
    except Exception as e:
        print(f"[!] Error checking VPN: {e}")
        return False

def connect_vpn(vpn_name):
    try:
        result = subprocess.run(
            ["powershell", "-Command", f"rasdial '{vpn_name}'"],
            capture_output=True, text=True
        )
        print(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"[!] VPN connection error: {e}")

def main_loop():
    print(f"[i] Monitoring VPN '{vpn_name}' every {check_interval} seconds...")
    while True:
        if not is_vpn_connected(vpn_name):
            print("[!] VPN is disconnected. Connection attempt...")
            connect_vpn(vpn_name)
        else:
            print("[✓] VPN is connected.")
        time.sleep(check_interval)

if __name__ == "__main__":
    main_loop()