print(""" 
      ========HESAP MAKİNESİ========
      /      Toplama İşlemi : 1    / 
      /      Çıkarma İşlemi : 2    /
      /      Çarpma İşlemi  : 3    /
      /      Bölme İşlemi   : 4    /
      /============================/
      """)

def toplama():
    print("\n{} sayısı ile {} sayısının toplamı{} ' dır.".format(a,b,a+b))
    
def cikarma():
    print("\n{} sayısı {} sayısından çıkarılınca {} kalır".format(a,b,a-b))
    
def carpma():
    print("\n {} sayısının {} sayısına çarpımı {} 'dır.".format(a,b,a*b))

def bolme():
    try:
        print("\n {} sayısının {} sayısına bölümü {} 'dür.".format(a,b,a/b))
    except ZeroDivisionError:
        print("Bir sayı 0 ile bölünemez")

a=int(input("Birinci sayınızı giriniz: "))
b=int(input("İkinci sayınızı giriniz: "))
c=int(input("Hangi matematiksel işlemi yapmak istersiniz? "))

if c==1:
    toplama()
elif c==2:
    cikarma()
elif c==3:
    carpma()
elif c==4:
    bolme()
else:
    print("Matematiksel işlemler için 1 ile 4 arasında bir seçim yapınız!")
