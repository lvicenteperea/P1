from pydantic import BaseModel

# Definimos el modelo de respuesta
class UserValidationResponse(BaseModel):
    retCode: int
    retTxt: str    