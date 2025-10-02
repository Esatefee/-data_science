''' Soru 1
Araba sınıfı iki özellik (marka, model) alıyor.

bilgileri_yazdir() metodu bu bilgileri ekrana yazdırıyor.

Çıktı: Marka: Toyota, Model: Corolla '''

''' Soru 2 '''

class Dikdortgen:
    def __init__(self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik

    def alan_hesapla(self):
        alan = self.genislik * self.yukseklik
        return alan   # alanı hesaplayıp döndürüyor

# Kullanım
dikdortgen1 = Dikdortgen(5, 10)
sonuc = dikdortgen1.alan_hesapla()
print("Dikdörtgenin alanı:", sonuc)

''' Çıktı: Dikdörtgenin alanı: 50 (kod içerisinde return komutu olduğu için fonksiyon tekrardan döndü.) '''

''' Soru 3 '''
class Kare:
    def __init__(self, kenar):
        self.kenar = kenar

    def kareyi_yazdir(self):
        for i in range(self.kenar):
            print("* " * self.kenar)

# Kullanım
kare1 = Kare(6)
kare1.kareyi_yazdir()

''' Çıktı: 
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * *  '''

''' Soru 4 '''
class HesapMakinesi:
    def topla(self, sayi1, sayi2, sayi3=None):
        if sayi3 is not None:
            return sayi1 + sayi2 + sayi3
        else:
            return sayi1 + sayi2

# Kullanım
hesap = HesapMakinesi()
print("İki sayının toplamı:", hesap.topla(10, 20))
print("Üç sayının toplamı:", hesap.topla(10, 20, 30))

''' Çıktı: 
İki sayının toplamı: 30
Üç sayının toplamı: 60 '''

''' Soru 5 '''
class Merhaba:
    def selam_ver(self):
        print("Merhaba Dünya")


# Kullanım
a = Merhaba()
a.selam_ver()

''' Çıktı: Merhaba Dünya '''


