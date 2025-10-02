
# Python Giriş

''' 1. Print Fonksiyonu '''
print("merhaba")
print("merhaba","python","dersi",sep="-")

''' 2. Değişkenler ve Veri Tipleri '''
x = 10         # integer
y = 4.5        # float
z = "python"   # string
t = True       # boolean
print(type(x), type(y), type(z), type(t))

''' 3. Veri Yapıları (list, tuple, dict, set)'''
# Liste (mutable)
liste = [10, 20, 30, "veri", "bilim"]
liste.append(99)
liste[0] = 100
print(liste)

# Tuple (immutable)
demet = ("a", "b", "c")
print(demet[1])

# Dictionary
sozluk = {"ad":"Ali", "yas":25}
sozluk["yas"] = 26
print(sozluk)

# Set (tekrarlı değer almaz)
kume = {1, 2, 2, 3, 4}
print(kume)

''' 4. Fonksiyonlar '''
def merhaba(isim):
    print("Merhaba", isim)

def kup_al(sayi):
    return sayi ** 3

merhaba("Selim")
print(kup_al(5))

''' Lambda Fonksiyon '''
karesi = lambda x: x*x
toplama = lambda a,b: a+b
print(karesi(6))
print(toplama(4,7))

''' 6. Basit Sınıf (Class) '''
class Ogrenci:
    ad = "Mehmet"
    yas = 21
    def bilgi(self):
        print("Ad:", self.ad, "Yaş:", self.yas)

o1 = Ogrenci()
o1.bilgi()

''' 7. Yapıcı Metot (Constructor) '''
class Kitap:
    def __init__(self, ad, yazar):
        self.ad = ad
        self.yazar = yazar

    def bilgi(self):
        return f"{self.ad} - {self.yazar}"

k1 = Kitap("Kürk Mantolu Madonna","Sabahattin Ali")
print(k1.bilgi())

''' 8. Kapsülleme (Encapsulation) '''
class Hesap:
    def __init__(self, bakiye):
        self.__bakiye = bakiye   # private değişken

    def getBakiye(self):
        return self.__bakiye

    def paraYatir(self, miktar):
        self.__bakiye += miktar

h1 = Hesap(500)
print("Başlangıç:", h1.getBakiye())
h1.paraYatir(200)
print("Yeni bakiye:", h1.getBakiye())

''' 9. Kalıtım (Inheritance) '''
class Hayvan:
    def ses(self):
        print("Ses çıkarır")

class Kopek(Hayvan):
    def ses(self):
        print("Hav hav")

class Kus(Hayvan):
    def ses(self):
        print("Cik cik")

k1 = Kopek()
k2 = Kus()
k1.ses()
k2.ses()
