import requests
dosya=open("isim.txt","r")
dosyaIcerik=dosya.readlines()
dosya.close()
for i in dosyaIcerik:
    print i.split("\n")[0]
    url="http://192.168.199.130/"+str(i.split("\n")[0])
    sonuc=requests.get(url=url)
    if int(sonuc.status_code)==404:
        print "dosya yok"
    elif int(sonuc.status_code)==200:
        print "dosya bulundu"