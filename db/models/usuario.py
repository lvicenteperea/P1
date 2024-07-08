from pydantic import BaseModel  #, EmailStr
from typing import Union
import mysql.connector
import config as settings
from errors.error import UserValidationResponse


class Usuario(BaseModel):
    nombre: str
    apellido1: str
    apellido2: str
    email: str
    pwd: str
    telefono: str

    def __init__(self, nombre: str, apellido1: str, apellido2: str, email: str, pwd: str, telefono: str):
        super().__init__(nombre=nombre, apellido1=apellido1, apellido2=apellido2, email=email, pwd=pwd, telefono=telefono)

    # Getters
    def get_nombre(self) -> str:
        return self.nombre

    def get_apellido1(self) -> str:
        return self.apellido1

    def get_apellido2(self) -> str:
        return self.apellido2

    def get_email(self) -> str:
        return self.email

    def get_pwd(self) -> str:
        return self.pwd

    def get_telefono(self) -> str:
        return self.telefono

    # Setters
    def set_nombre(self, nombre: str) -> None:
        self.nombre = nombre

    def set_apellido1(self, apellido1: str) -> None:
        self.apellido1 = apellido1

    def set_apellido2(self, apellido2: str) -> None:
        self.apellido2 = apellido2

    def set_email(self, email: str) -> None:
        self.email = email

    def set_pwd(self, pwd: str) -> None:
        self.pwd = pwd

    def set_telefono(self, telefono: str) -> None:
        self.telefono = telefono

    # Método para obtener el nombre completo en letra capital
    def nombre_completo_capital(self) -> str:
        nombre_completo = f"{self.nombre} {self.apellido1} {self.apellido2}"
        return nombre_completo.title()

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------
class Usuarios(BaseModel):
    @staticmethod
    def validar_usuario(usuario: str, pwd: str) -> Union[UserValidationResponse, Usuario]:
        db_config = {
            'user': settings.USER,
            'password': settings.PWD,
            'host': settings.HOST,
            'database': settings.DATABASE,
        }

        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        retCode = 0
        retTxt = ""
        apel1 = None
        apel2 = None
        email = None
        telefono = None

        try:
            out_params = cursor.callproc('valida_usuario', [retCode, retTxt, usuario, pwd, apel1, apel2, email, telefono])
            
            # Asignar los valores de salida a las variables
            retCode = out_params[0]
            retTxt = out_params[1]
            apel1 = out_params[4]
            apel2 = out_params[5]
            email = out_params[6]
            telefono = out_params[7]

            return Usuario(usuario, apel1, apel2, email, pwd, telefono)
         
        except mysql.connector.Error as err:
            return UserValidationResponse(retCode=-1, retTxt=str(err))
        except Exception as err:
            return UserValidationResponse(retCode=-1, retTxt=str(err))
        
        finally:
            cursor.close()
            connection.close()

            