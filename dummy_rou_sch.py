# GIROS-UPM 2024-12-05
# REMOTE DRIVER
# 
# pip install "fastapi[standard]"

from fastapi import FastAPI, HTTPException
import uvicorn
import logging
from pydantic import BaseModel
from typing import List
import dummy_route

logging.basicConfig(level=logging.INFO)

# Modelo de la peticion
class RouteRequest(BaseModel):
    veh_ID: str
    priority: str
    start: List[float]
    end: List[float]

#Código del servidor REST
app = FastAPI()

@app.post("/getroute")
async def getroute(request: RouteRequest):
    try:
        logging.info(f"Received request: {request}")
        
        #INSERTAR EN EL FICHERO dummy_route.py LA RUTA A DEVOLVER
        response = dummy_route.route
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Ejecución del servidor REST. Cambiar localhost y 8000 por la IP y puerto donde debe escuchar el servidor.
uvicorn.run(app, host="localhost",port=8000)