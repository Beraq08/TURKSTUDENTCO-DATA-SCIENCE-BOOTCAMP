import os
class Urun:
    def __init__(self,ad,kategori,fiyat,stok):
        self.ad = ad
        self.kategori = kategori
        self.fiyat=fiyat
        self.stok=stok

    def __str__(self):
        return f"{self.ad},{self.kategori},{self.fiyat},{self.stok}"
class Market:
    def __init__(self):
        self.file = open("product.txt", "a+", encoding="utf-8")
        self.file.seek(0)
        self.urunler = self.file.read().splitlines()

    def ListProduct(self):
        self.file.seek(0)
        self.urunler = self.file.read().splitlines()
        if len(self.urunler) == 0:
            print("Ürün bulunamadı\n")
        else:
            print("Ürünler")
            print("--------")
            print(" Ad | Kategori | Fiyat | Stok ")
            for urun in self.urunler:
                print(urun)
            print("\n")

    def AddProduct(self, Urun):
        if self.isProductExist(Urun.ad):
            print ("Ürün zaten mevcut\n")
        elif (Urun.stok <1 or Urun.fiyat <=0):
            print ("Ürünün fiyatını ve miktarını kontrol edin\n")
        else:
            self.file.write(f"{Urun}\n")
    def isProductExist(self, ad):
        self.file.seek(0)
        self.urunler = self.file.read().splitlines()
        for urun in self.urunler:
            if urun.split(",")[0] == ad:
                return True
        return False
    def DeleteProduct(self, ad):
        if not self.isProductExist(ad):
            print("Ürün bulunamadı\n")
        else:
            self.file.seek(0)
            self.urunler = self.file.read().splitlines()
            new_urunler = []
            for urun in self.urunler:
                if urun.split(",")[0] != ad:
                    new_urunler.append(urun)
            with open("product.txt", "w", encoding="utf-8") as f:
                for urun in new_urunler:
                    f.write(f"{urun}\n")
            print("Ürün silindi\n")
            self.urunler = new_urunler
    def __del__(self):
        self.file.close()

def Menü():
    print("Menü")
    print("-----")
    print("1-Ürünleri Listele")
    print("2-Ürün Ekle")
    print("3-Ürün Sil")
    print("4-Çıkış\n")
    secim = input("Seçiminiz:")
    print("\n")
    if(secim == "1"):
        market.ListProduct()
    elif(secim == "2"):
        print("Ürün Ekleme")
        ad = input("Ürün Adı:")
        kategori = input("Kategori:")
        fiyat = float(input("Fiyat:"))
        stok = int(input("Stok:"))
        print("\n")
        urun = Urun(ad, kategori, fiyat, stok)
        market.AddProduct(urun)
    elif(secim == "3"):
        print("Ürün Silme")
        ad = input("Ürün Adı:")
        print("\n")
        market.DeleteProduct(ad)
    elif(secim == "4"):
        market.__del__()
        exit()
    else:
        print("Hatalı seçim\n")
        Menü()
market = Market()

while True:
    Menü()






