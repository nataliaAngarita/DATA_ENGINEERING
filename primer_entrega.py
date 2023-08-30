import requests

url = "https://dark-sky.p.rapidapi.com/%7Blatitude%7D,%7Blongitude%7D"  
response = requests.get(url)

if response.status_code == 200:  # Verificar si la solicitud fue exitosa
    data = response.json()  # Convertir la respuesta JSON en un diccionario de Python
    print(data)
else:
    print("Error en la solicitud:", response.status_code)
