from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db.models.usuario import Usuario

# Definimos el router
router = APIRouter(prefix="/user", tags=["users"])

# Definimos el modelo de entrada
class UserValidationRequest(BaseModel):
    usuario: str
    pwd: str

# Definimos el modelo de respuesta
class UserValidationResponse(BaseModel):
    retCode: int
    retTxt: str


@router.post("/validate", response_model=UserValidationResponse)
def validate(request: UserValidationRequest):
    retCode, retTxt = Usuario.validar_usuario(request.usuario, request.pwd)

    if retCode < 0:
        raise HTTPException(status_code=400, detail=retTxt)
    elif retCode > 1:
        raise HTTPException(status_code=500, detail="Unexpected error occurred")

    return UserValidationResponse(retCode=retCode, retTxt=retTxt)

