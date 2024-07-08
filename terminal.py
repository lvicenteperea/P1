from db.models.usuario import Usuario, Usuarios
from errors.error import UserValidationResponse

result = Usuarios.validar_usuario("Usuawwrio", "www")

if isinstance(result, UserValidationResponse):
    if result.retCode < 0:
       print(400, result.retTxt)
    elif result.retCode > 1:
        print(500, "Unexpected error occurred")
    else:
        print("Otro error")
else:
    print(result.get_apellido1())