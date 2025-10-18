import subprocess
import time

vpn_name = "VPN connection name"  # Замените на имя вашего VPN-подключения
check_interval = 30  # Интервал проверки в секундах

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
        print(f"[!] Ошибка при проверке VPN: {e}")
        return False

def connect_vpn(vpn_name):
    try:
        result = subprocess.run(
            ["powershell", "-Command", f"rasdial '{vpn_name}'"],
            capture_output=True, text=True
        )
        print(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"[!] Ошибка подключения VPN: {e}")

def main_loop():
    print(f"[i] Мониторинг VPN '{vpn_name}' каждые {check_interval} секунд...")
    while True:
        if not is_vpn_connected(vpn_name):
            print("[!] VPN отключен. Пытаюсь подключиться...")
            connect_vpn(vpn_name)
        else:
            print("[✓] VPN подключен.")
        time.sleep(check_interval)

if __name__ == "__main__":
    main_loop()