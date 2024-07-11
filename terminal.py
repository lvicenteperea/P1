from db.models.usuario import Usuario, Usuarios
from errores.error import UserValidationResponse

result = Usuarios.validar_usuario("Usuawwrio", "www")

if isinstance(result, UserValidationResponse):
    if result.retCode < 0:
       print(400, result.retCode, result.retTxt)
    elif result.retCode > 1:
        print(500, "Unexpected error occurred", result.retCode, result.retTxt)
    else:
        print("Otro error", result.retCode, result.retTxt)
else:
    print(str(result))