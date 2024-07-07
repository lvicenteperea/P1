from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Dict, Any
from db.mysql_db import MySQLDatabase
from db.oracle_db import OracleDatabase

app = FastAPI()

# Configuración de la base de datos
db_type = 'mysql'  # Cambia esto a 'oracle' para usar Oracle

if db_type == 'mysql':
    db = MySQLDatabase(host='localhost', database='tu_base_de_datos', user='tu_usuario', password='tu_contraseña')
elif db_type == 'oracle':
    db = OracleDatabase(dsn='tu_dsn', user='tu_usuario', password='tu_contraseña')
else:
    raise ValueError("Tipo de base de datos no soportado")

class LoginData(BaseModel):
    email: EmailStr
    pwd: str

@app.post("/login")
def login(data: LoginData):
    resultado = db.validate_user(data.email, data.pwd)
    if resultado["codigo"] == 0:
        return resultado
    else:
        raise HTTPException(status_code=400, detail=resultado["mensaje"])

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")

