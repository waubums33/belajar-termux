import os

FILE = "tugas.txt"

def tampilkan_tugas():
    if not os.path.exists(FILE):
        print("Belum ada tugas!")
        return
    with open(FILE, "r") as f:
        tugas = f.readlines()
    if not tugas:
        print("Belum ada tugas!")
    for i, t in enumerate(tugas, 1):
        print(f"{i}. {t.strip()}")

def tambah_tugas(teks):
    with open(FILE, "a") as f:
        f.write(teks + "\n")
    print("Tugas ditambahkan!")

print("=== TO-DO LIST WAHYU ===")
while True:
    print("\n1. Lihat tugas")
    print("2. Tambah tugas")
    print("3. Keluar")
    pilih = input("Pilih: ")

    if pilih == "1":
        tampilkan_tugas()
    elif pilih == "2":
        teks = input("Tugas baru: ")
        tambah_tugas(teks)
    elif pilih == "3":
        print("Sampai jumpa!")
        break
    else:
        print("Pilihan salah!")
