# GIROS-UPM 2024-12-05
# REMOTE DRIVER 
#
# pip install requests

import requests
import json
import examples

# URL de la API de Route Scheduler. Cambiar localhost y 8000 por la IP y puerto donde se ejecuta el servidor
URL_GET_ROUTE = "http://localhost:8000/getroute"


# Función principal
def main():

    # La petición está definida en el fichero example.py (vehículo, origen y final). 
    payload = examples.peticion
    response = requests.post(URL_GET_ROUTE, json=payload)
    result = response.json()
    print(f"Route: {result}")

if __name__ == "__main__":
    main()
