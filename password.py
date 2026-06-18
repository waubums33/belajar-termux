import random
import string

def buat_password(panjang):
    karakter = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(panjang):
        password += random.choice(karakter)
    return password

print("=== PASSWORD GENERATOR ===")
panjang = int(input("Mau berapa karakter? "))
hasil = buat_password(panjang)
print(f"\nPassword kamu: {hasil}")
