''' Soru 1

Hangisi encapsulation tanımıdır?

A. Bir sınıftan yeni eleman türetme işlemine denir
B. Ata sınıfın özelliklerini almaya denir
C. Bir nesnenin metot ve verilerini diğer nesnelerden saklayarak erişime engelleyerek yanlış kullanımı engel olmaktır

Doğru cevap: C
Encapsulation (kapsülleme) = verilerin gizlenmesi + sadece getter ve setter ile erişim.'''

''' Soru 2

Aşağıdaki koda göre doğru ifade nedir? '''
class A():
    def __init__(self,a):
        print("a sınıfı oluşturuldu")
    def ilk(self):
        print("ilk isimli metot")

class B(A):
    def __init__(self,j=10):
        self.j=j
'''A. A sınıfı B’den miras alır
B. B sınıfı A’dan miras alır
C. B sınıfı A’dan miras alır ama tüm özelliklerini almaz

Doğru cevap: C
Çünkü class B(A) yazıldığı için B, A’dan miras alıyor. Ama B kendi __init__ metodunu tanımladığı için A’nın __init__ içindeki "a sınıfı oluşturuldu" çıktısını override eder. Yani A’nın __init__ fonksiyonu çalışmaz.'''

''' Soru 3

Soyut sınıf (abstract class) tanımı hangisidir?

A. Bir sınıftan başka sınıf türetebilmek için oluşturulur
B. OOP’de nesnesi olmayan sınıflara verilen isimdir
C. Bir sınıfın üst sınıftan miras almasına denir

Doğru cevap: B
Sadece temel şablon sağlar.'''

''' Soru 4 '''
class Animal():
    def sesVer(self):
        print("ses çıkarırlar")

class kedi(Animal):
    def sesVer(self):  # ata sınıfı ezdi
        print("miyav")

a = Animal()
a.sesVer()

k = kedi()
k.sesVer()

