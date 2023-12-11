from abc import ABC, abstractmethod
import math

# Kelas abstrak dasar
class BentukGeometri(ABC):
    @abstractmethod
    def hitung_luas(self):
        pass

# Kelas turunan untuk Persegi
class Persegi(BentukGeometri):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi * self.sisi

# Kelas turunan untuk Persegi Panjang
class PersegiPanjang(BentukGeometri):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

# Kelas turunan untuk Segitiga
class Segitiga(BentukGeometri):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi

# Kelas turunan untuk Ling
