import requests
url="http://ptl-7547c0fa-03b0ff9b.libcurl.so/index.php?name=hacker"
konum=url.find("=")
sonuc=url[:konum+1]+"<h1>deneme</h1>"
icerik=requests.get(url=sonuc)
print icerik
if "<h1>deneme</h1>" in icerik.content:
    print "xss olma ihtimali vardir"