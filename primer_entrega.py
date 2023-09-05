##Extraccion de datos
import requests
import json
import psycopg2

response = requests.get("https://data.covid19india.org/state_district_wise.json")

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Error al obtener los datos de la API. Código de estado: {response.status_code}')
    data = None

# conexión a Redshift
dbname = 'data-engineer-database'
user = 'buitragonatalia778_coderhouse'
password = 'kDWUk04BR0'
host = 'data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com'
port = '5439'  

conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
)

cur = conn.cursor()

create_table_sql = """
CREATE TABLE IF NOT EXISTS COVID (
    notes varchar(20),
    active int,
    confirmed int,
    migratedother int,
    deceased int,
    recovered int

);
"""

# Ejecuta la consulta para crear la tabla (si no existe)
cur.execute(create_table_sql)

