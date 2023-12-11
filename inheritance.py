import math

# Kelas dasar untuk perhitungan luas
class PerhitunganLuas:
    def luas_persegi(self, p):
        luas = p * p
        return luas

    def luas_persegi_panjang(self, p, l):
        luas = p * l
        return luas

    def luas_segitiga(self, a, t):
        luas = 0.5 * a * t
        return luas

    def luas_lingkaran(self, r):
        luas = math.pi * r * r
        return luas

# Kelas turunan untuk menampilkan menu dan mengatur input pengguna
class KalkulatorLuas(PerhitunganLuas):
    def menu(self):
        print("Pilih operasi:")
        print("1. Luas Persegi")
        print("2. Luas Persegi Panjang")
        print("3. Luas Segitiga")
        print("4. Luas Lingkaran")

    def hitung(self):
        while True:
            self.menu()
            # Meminta pengguna untuk memasukkan pilihan
            pilihan = input("Masukkan pilihan (1/2/3/4): ")

            # Melakukan operasi sesuai pilihan pengguna
            if pilihan == '1':
                p = float(input("Masukkan Panjang Sisi Persegi: "))
                hasil = self.luas_persegi(p)
                print("Luas Persegi adalah:", hasil)
            elif pilihan == '2':
                p = float(input("Masukkan Panjang: "))
                l = float(input("Masukkan Lebar: "))
                hasil = self.luas_persegi_panjang(p, l)
                print("Luas Persegi Panjang adalah:", hasil)
            elif pilihan == '3':
                a = float(input("Masukkan Alas Segitiga: "))
                t = float(input("Masukkan Tinggi Segitiga: "))
                hasil = self.luas_segitiga(a, t)
                print("Luas Segitiga adalah:", hasil)
            elif pilihan == '4':
                r = float(input("Masukkan Jari-Jari Lingkaran: "))
                hasil = self.luas_lingkaran(r)
                print("Luas Lingkaran adalah:", hasil)
            else:
                print("Pilihan tidak valid")

            # Meminta pengguna apakah ingin menghitung lagi
            ulangi = input('Apakah Anda Ingin Mencoba Lagi? (Y/N): ')
            if ulangi.upper() != 'Y':2
                break  # Keluar dari loop jika pengguna tidak ingin menghitung lagi

if __name__ == "__main__":
    kalkulator = KalkulatorLuas()
    kalkulator.hitung()
