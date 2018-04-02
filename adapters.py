import requests
params = {'apikey': '277f54985d1ca8aaf85eea03d5dcecf29d0310677653137aebd71fa82d4aec09','url':'gazi.edu.tr'}
response = requests.post('https://www.virustotal.com/vtapi/v2/url/scan', data=params)
json_response = response.json()
analizRaporu=json_response['permalink']
print requests.get(url=str(analizRaporu)).content