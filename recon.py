import os
import datetime

def banner():
    print("="*40)
    print("   WAHYU RECON TOOL v1.0")
    print("   By: Muhammad Wahyu")
    print("="*40)
    print("")

def ping_target(target):
    print(f"\n[*] Ping ke {target}...")
    os.system(f"ping -c 4 {target}")

def scan_port(target):
    print(f"\n[*] Scanning port {target}...")
    os.system(f"nmap -p 22,80,443 {target}")

def cek_dns(domain):
    print(f"\n[*] Cek DNS {domain}...")
    os.system(f"nslookup {domain}")

def simpan_hasil(target):
    waktu = datetime.datetime.now()
    with open("hasil_recon.txt", "a") as f:
        f.write(f"\n[{waktu}] Target: {target}\n")
    print(f"\n[+] Hasil disimpan ke hasil_recon.txt")

# MAIN MENU
banner()

while True:
    print("\n[1] Ping Target")
    print("[2] Scan Port")
    print("[3] Cek DNS")
    print("[4] Simpan Hasil")
    print("[5] Keluar")
    print("")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        target = input("Masukkan IP/domain: ")
        ping_target(target)
    elif pilih == "2":
        target = input("Masukkan IP/domain: ")
        scan_port(target)
    elif pilih == "3":
        domain = input("Masukkan domain: ")
        cek_dns(domain)
    elif pilih == "4":
        target = input("Masukkan target yang mau disimpan: ")
        simpan_hasil(target)
    elif pilih == "5":
        print("\n[!] Keluar... Wassalamualaikum!")
        break
    else:
        print("\n[-] Pilihan tidak valid!")
