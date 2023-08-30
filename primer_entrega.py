##Extraccion de datos 
import requests

url = 'https://api.jikan.moe/v4/top/anime' 
response = requests.get(url)

if response.status_code == 200:  
    data = response.json()  
    for e in data['data']:
     print(e['type'])
     print(e['title'])
else:
    print("Error en la solicitud:", response.status_code)

