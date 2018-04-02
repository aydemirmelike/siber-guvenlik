import requests
import json
url="https://www.btcturk.com/api/ticker"
btcturkSonuc=requests.get(url=url,verify=False).json()
print btcturkSonuc[0]['last']
if int (btcturkSonuc[0]['last']) > 50000:
    print "50 milyardan buyuk"
    "https://rest.nexmo.com/sms/json"
    payload={"api_key" = "ddcef16b","api_secret" = "deabb37ecec7ef08","to":"905078789459","from":"BTCTURK","text":"50 milyar uzerinde alma""}
    requests.post(url=url,data=payload,verify=False)
else:
    print "50 milyardan kucuk"


