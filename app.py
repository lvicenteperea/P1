from fastapi import FastAPI #, HTTPException
from routers import usuario
from pydantic import BaseModel, EmailStr
#from typing import Dict, Any


app = FastAPI()

# Incluimos el router
app.include_router(usuario.router, prefix="/")


class LoginData(BaseModel):
    email: EmailStr
    pwd: str


@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")

