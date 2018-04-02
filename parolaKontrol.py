# _*_ coding: utf-8 _*_
dosya=open("parolalar.txt","r")
dosyaIcerik=dosya.readlines()
dosya.close()
print dosyaIcerik
buyukHarfler=["Q","W","R"]
kucukHarfler=["q","t","a","d","m","i","n","z","s","x"]
sayilar=["1","2","3","4","5","6"]
sayilarSayici=0
buyukHarflerSayici=0
kucukHarflerSayici=0
toplamHarf=0
for i in dosyaIcerik:
    print i
    for buyukHarf in buyukHarfler:
        toplamHarf+=1
        if buyukHarf in i:
            buyukHarflerSayici +=1
print "toplam büyük harf sayisi :" ,str(buyukHarflerSayici)
