# Fungsi menghitung luas persegi
def luas_persegi(p):
    luas = p * p
    return luas

# Fungsi menghitung luas persegi panjang
def luas_persegi_panjang(p, l):
    luas = p * l
    return luas

# Fungsi menghitung luas segitiga
def luas_segitiga(a, t):
    luas = 0.5 * a * t
    return luas

# Fungsi menghitung luas lingkaran
def luas_lingkaran(r):
    import math
    luas = math.pi * r * r
    return luas

# Menampilkan menu operasi
def menu():
    print("Pilih operasi:")
    print("1. Luas Persegi")
    print("2. Luas Persegi Panjang")
    print("3. Luas Segitiga")
    print("4. Luas Lingkaran")

# Loop utama
while True:
    # Meminta pengguna untuk memasukkan pilihan
    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    # Melakukan operasi sesuai pilihan pengguna
    if pilihan == '1':
        p = float(input("Masukkan Panjang Sisi Persegi: "))
        hasil = luas_persegi(p)
        print("Luas Persegi adalah:", hasil)
    elif pilihan == '2':
        p = float(input("Masukkan Panjang: "))
        l = float(input("Masukkan Lebar: "))
        hasil = luas_persegi_panjang(p, l)
        print("Luas Persegi Panjang adalah:", hasil)
    elif pilihan == '3':
        a = float(input("Masukkan Alas Segitiga: "))
        t = float(input("Masukkan Tinggi Segitiga: "))
        hasil = luas_segitiga(a, t)
        print("Luas Segitiga adalah:", hasil)
    elif pilihan == '4':
        r = float(input("Masukkan Jari-Jari Lingkaran: "))
        hasil = luas_lingkaran(r)
        print("Luas Lingkaran adalah:", hasil)
    else:
        print("Pilihan tidak valid")

    # Meminta pengguna apakah ingin menghitung lagi
    ulangi = input('Apakah Anda Ingin Mencoba Lagi? (Y/N): ')
    if ulangi.upper() != 'Y':
        break  # Keluar dari loop jika pengguna tidak ingin menghitung lagi
