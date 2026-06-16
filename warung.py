harga = {
    "nasi goreng": 15000,
    "mie goreng": 12000,
    "kwetiaw": 13000,
}
pesan = input("Mau pesan apa? ").lower()

if pesan in harga:
    print(f"{pesan} = Rp {harga[pesan]}")
    print("Silahkan tunggu, makanan sedang di proses!!!")
else:
    print("MAAF MAKANAN TIDAK ADA!")

