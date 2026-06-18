menu = {
    "nasi goreng": 15000,
    "mie goreng djawa": 15000,
    "mie dok dok": 15000,
    "kwetiaw goreng": 15000,
    "kwetiaw rebus": 15000
}

total = 0
jumlah_item = 0

while True:
    print(f"\nMenu: {list(menu.keys())}")
    pesan = input("Mau pesan apa? (atau 'selesai'): ").lower()
    
    if pesan == "selesai":
        break
    
    if pesan in menu:
        total += menu[pesan]
        jumlah_item += 1
        print(f"{pesan} ditambahkan!")
    else:
        print("Menu tidak ada!")

# Diskon kalau beli 3+ item
if jumlah_item >= 3:
    diskon = total * 0.1
    total_akhir = total - diskon
    print(f"\nSubtotal: Rp {total}")
    print(f"Diskon 10%: -Rp {diskon}")
    print(f"Total Bayar: Rp {total_akhir}")
else:
    print(f"\nTotal Bayar: Rp {total}")
