from fastapi import APIRouter, HTTPException, Query
from typing import Union
from pydantic import BaseModel
from db.models.usuario import Usuario, Usuarios
from errors.error import UserValidationResponse

# Definimos el router
router = APIRouter(prefix="/user", tags=["users"])


'''
Query(...): El uso de ... como argumento en Query indica que el parámetro es obligatorio. 
Si no se proporciona en la solicitud, FastAPI lanzará un error 422 (Unprocessable Entity).
'''
@router.get("/validate", response_model=Union[UserValidationResponse, Usuario])
def validate(usuario: str = Query(...), pwd: str = Query(...)):
    """
        Servicio GET para validar usuario y contraseña.
        
        Parámetros:
        - usuario: str (obligatorio) - El nombre de usuario.
        - pwd: str (obligatorio) - La contraseña del usuario.
        
        Retorna:
        - UserValidationResponse: Código de retorno y mensaje de texto en caso de error.
        - Usuario: Instancia del usuario validado en caso de éxito.
    """
    result = Usuarios.validar_usuario(usuario, pwd)

    if isinstance(result, UserValidationResponse):
        if result.retCode < 0:
            raise HTTPException(status_code=400, detail=result.retTxt)
        elif result.retCode > 1:
            raise HTTPException(status_code=500, detail="Unexpected error occurred")

    return result
