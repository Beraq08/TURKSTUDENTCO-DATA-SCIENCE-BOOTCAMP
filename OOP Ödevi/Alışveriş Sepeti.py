class Urun:
    def __init__(self,ad,fiyat,miktar):
        self.ad = ad
        self.fiyat=fiyat
        self.miktar=miktar

    def __str__(self):
        return f"{self.miktar} adet {self.ad} fiyat: {self.miktar} * {self.fiyat} = {self.fiyat*self.miktar} TL"
class Sepet:
    def __init__(self):
        self.Sepet=[]
    def urun_sepettemi(self,ad):
        for urun in self.Sepet:
            if urun.ad==ad:
                return True
    def urun_ekle(self,Urun):
        if Urun.miktar <1 or Urun.fiyat <=0:
            return f"Ürünün fiyatını ve miktarını kontrol edin"
        elif self.urun_sepettemi(Urun.ad):
            return f"Sepetinizde {Urun.ad} ürününden var"
        else:
            self.Sepet.append(Urun)
            return f"{Urun.ad} ürünü sepetinize eklendi"
    def urun_cikar(self,ad):
        if self.urun_sepettemi(ad):
            a=self.urunu_bul(ad)
            self.Sepet.remove(a)
            return f"Sepetinizdeki {ad} ürünü tamamen silindi"
        else:
            return f"Sepetinizde {ad} ürünü bulunamadı"
    def urunu_bul(self,ad):
        for urun in self.Sepet:
            if urun.ad==ad:
                return urun
    
    def miktar_arttir(self,ad,miktar):
        if miktar<1:
            return f"Ekleyeceğiniz miktarı kontrol edin"
        elif self.urun_sepettemi(ad):
            a=self.urunu_bul(ad)
            a.miktar+=miktar
            return f"Sepetinizdeki {ad} ürünün miktarı {miktar} artırılarak {a.miktar} olarak güncellendi"
        else:
            return f"Sepetinizde {ad} ürünü bulunamadı"
    
    def miktar_azalt(self,ad,miktar):
        if miktar<1:
            return f"Çıkartacağınız miktarı kontrol edin"
        elif self.urun_sepettemi(ad):
            a=self.urunu_bul(ad)
            if a.miktar<miktar:
                return f"Sepetinizde {ad} ürününden {a.miktar} adet var.{miktar} adet çıkaramazsınız" 
            elif a.miktar==miktar:
                self.Sepet.remove(a)
                return f"Sepetinizden {ad} ürünü tamamen silindi"
            else:
                a.miktar-=miktar
                return f"Sepetinizdeki {ad} ürünün miktarı {miktar} azaltılarak {a.miktar} olarak güncellendi"
        else:
            return f"Sepetinizde {ad} ürünü bulunamadı"
    def sepet_liste(self):
        if self.Sepet:
            return f"Alışveriş Sepeti: {[str(urun) for urun in self.Sepet]}"
        else:
            return f"Sepetiniz boş"
    def toplam_tutar(self):
        if self.Sepet:
            toplam=0
            for urun in self.Sepet:
                toplam+=urun.fiyat*urun.miktar
            return f"Sepetinizin toplam tutarı: {toplam}"
        else:
            return f"Sepetiniz boş"
#Urun klasında ürün bilgilerini tutuyoruz,Sepet klasında ürün ekleme miktarını artırma,azaltma sepetteki ürünleri gösterme ve toplam tutarı gösterme işlemlerini içeriyor.
        
alisverisSepeti=Sepet()
bilgisayar=Urun("MSİ",27000,1)
klavye=Urun("Logitech",1000,1)
mouse=Urun("Rampage",2000,1)
mousepad=Urun("Rampage",200,1)
pil=Urun("Duracell",15,6)
print(alisverisSepeti.urun_ekle(bilgisayar))
print(alisverisSepeti.urun_ekle(klavye))
print(alisverisSepeti.urun_ekle(mouse))
print(alisverisSepeti.urun_ekle(mousepad))
print(alisverisSepeti.urun_ekle(pil))
print(alisverisSepeti.sepet_liste())
print(alisverisSepeti.toplam_tutar())
print(alisverisSepeti.urun_cikar("MSİ"))
print(alisverisSepeti.miktar_arttir("Rampage",1))
print(alisverisSepeti.miktar_azalt("Duracell",2))
print(alisverisSepeti.sepet_liste())
print(alisverisSepeti.toplam_tutar())


