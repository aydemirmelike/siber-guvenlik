import requests
url="https://127.0.0.1:8834/session"
payload ={"username":"admin","password":"admin"}
sonuc=requests.post(url=url,data=payload,verify=False)
print  sonuc