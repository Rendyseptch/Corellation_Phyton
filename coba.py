# Fungsi untuk penambahan
def tambah(a, b):
    return a + b

# Fungsi untuk pengurangan
def kurang(a, b):
    return a - b

# Fungsi untuk perkalian
def kali(a, b):
    return a * b

# Fungsi untuk pembagian
def bagi(a, b):
    if b == 0:
        return "Error: Pembagian oleh nol!"
    return a / b

# Menampilkan menu operasi
print("Pilih operasi:")
print("1. Penambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

# Meminta pengguna untuk memasukkan pilihan
pilihan = input("Masukkan pilihan (1/2/3/4): ")

# Meminta pengguna untuk memasukkan dua angka
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Melakukan operasi sesuai pilihan pengguna
if pilihan == '1':
    print("Hasil penambahan:", tambah(angka1, angka2))
elif pilihan == '2':
    print("Hasil pengurangan:", kurang(angka1, angka2))
elif pilihan == '3':
    print("Hasil perkalian:", kali(angka1, angka2))
elif pilihan == '4':
    print("Hasil pembagian:", bagi(angka1, angka2))
else:
    print("Pilihan tidak valid")
