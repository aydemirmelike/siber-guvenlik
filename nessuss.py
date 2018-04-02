import requests
url="https://localhost:8834/session"
payload={"username":"melikeee","password":"rf3rfre"}
result=requests.post(url=url,data=payload,verify=False).json()
print result
cookie="token="+str(result['token'])
print cookie
header={"X-cookie":cookie}
url="https://localhost:8834/folders"
sonuc=requests.get(url=url,headers=header,verify=False).json()
print sonuc
for i in sonuc['folders']:
    print i['name']
url="https://localhost:8834/folders"