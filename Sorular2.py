# İnsan Sınıfı
class Insan:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

    def konus(self):
        print(f"Adım {self.ad}, yaşım {self.yas}.")


# Hoca Sınıfı (İnsan’dan miras alıyor)
class Hoca(Insan):
    def __init__(self, ad, yas, sicil_no):
        super().__init__(ad, yas)
        self.sicil_no = sicil_no

    # konus metodunu ezdik
    def konus(self):
        print(f"Ben hocayım. Adım {self.ad}, yaşım {self.yas}, sicil numaram {self.sicil_no}.")

    def ders_ver(self):
        print(f"Hoca {self.ad} şu an ders veriyor.")


# Sekreter Sınıfı (İnsan’dan miras alıyor.)
class Sekreter(Insan):
    def __init__(self, ad, yas, departman):
        super().__init__(ad, yas)
        self.departman = departman

    def konus(self):
        print(f"Ben sekreterim. Adım {self.ad}, {self.departman} departmanında çalışıyorum.")

    def evrak_hazirla(self):
        print(f"Sekreter {self.ad} evrak hazırlıyor.")


# Öğrenci Sınıfı (İnsan’dan miras alıyor)
class Ogrenci(Insan):
    def __init__(self, ad, yas, ogrenci_no):
        super().__init__(ad, yas)
        self.ogrenci_no = ogrenci_no

    def konus(self):
        print(f"Ben öğrenciyim. Adım {self.ad}, numaram {self.ogrenci_no}.")

    def ders_calis(self):
        print(f"Öğrenci {self.ad} ders çalışıyor.")


# Kullanım Örnekleri
hoca = Hoca("Ahmet", 42, "H123")
sekreter = Sekreter("Selin", 28, "İdari İşler")
ogrenci = Ogrenci("Metin", 22, "O456")

hoca.konus()
hoca.ders_ver()

sekreter.konus()
sekreter.evrak_hazirla()

ogrenci.konus()
ogrenci.ders_calis()
