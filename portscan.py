import socket

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    hasil = sock.connect_ex((ip, port))
    sock.close()
    if hasil == 0:
        return True
    else:
        return False

print("=== SIMPLE PORT SCANNER ===")
target = input("Masukkan IP target: ")
ports = [21, 22, 23, 80, 443, 3306]

print(f"\nScanning {target}...\n")
for port in ports:
    if scan_port(target, port):
        print(f"Port {port} : OPEN")
    else:
        print(f"Port {port} : closed")
