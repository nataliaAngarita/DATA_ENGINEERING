##Extraccion de datos
import requests
import json
import psycopg2
from decouple import config

## es una API de conversión de moneda profesional y gratuita para obtener los últimos tipos de cambio
response = requests.get("https://v6.exchangerate-api.com/v6/ca5154d92bea03d7a10649f7/latest/USD")


if response.status_code == 200:
    data = response.json()
    i = 1
    for key, value in list(data.items())[:10]:
        print(f"Fila {i}: Clave: {key}, Valor: {value}")
        i += 1
else:
    print(f'Error al obtener los datos de la API. Código de estado: {response.status_code}')
    data = None

# conexión a Redshift
DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT')

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

cur = conn.cursor()



# Ejecuta la consulta para crear la tabla (si no existe)
cur.execute("CREATE TABLE IF NOT EXISTS CAMBIO_MONEDA (codigo_moneda VARCHAR(3), tasa_cambio NUMERIC(10, 6),fecha TIMESTAMP);")

