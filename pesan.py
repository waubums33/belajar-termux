menu = ["nasi goreng", "mie goreng", "kwetiaw"]
pesan = input("Mau pesan apa? ").lower()

if pesan in menu:
    print(f"{pesan} sedang di Proses!!!")
else:
    print("Ma'af tidak ada menu tersebut")

