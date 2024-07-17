from pydantic import BaseModel  #, EmailStr
from typing import Union
import db.db as db
import config as settings
from errores.error import UserValidationResponse


class Usuario(BaseModel):
    nombre: str
    apellido1: str
    apellido2: str
    email: str
    pwd: str
    telefono: str

    def __init__(self, nombre: str, apellido1: str, apellido2: str, email: str, pwd: str, telefono: str):
         super().__init__(nombre=nombre, apellido1=apellido1, apellido2=apellido2, email=email, pwd=pwd, telefono=telefono)
    '''
    def __init__(self, *args) -> None:

        # self.nombre:str
        # self.apellido1 = None
        # self.apellido2 = None
        # self.email = None
        # self.pwd = None
        # self.telefono = None

        for indice, valor in args[0].items():
            print(indice, valor )
            if hasattr(self, indice):
                setattr(self, indice, valor)
                print(getattr(self, indice))
            else:
                print("no tiene")

        # set_nombre(self.nombre)
        # print(self.apellido1)
        # set_apellido2(self.apellido2)
        # set_email(self.email)
        # set_pwd(self.pwd)
        # set_telefono(self.telefono)
    '''

    def __str__(self):
        return f"{self.nombre} {self.apellido1} {self.apellido2}\n{self.email}\n{self.pwd}\n{self.telefono}"

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
        return nombre_completo.capitalize()

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------
class Usuarios(BaseModel):
    @staticmethod
    def validar_usuario(usuario: str, pwd: str) -> Union[UserValidationResponse, Usuario]:
        mitxtCtr = 'Inicio'
        try:
            mi_db = db.DatabaseFactory.get_database('mysql', **settings.DB_CONFIG)

            '''
            # Definir las variables iniciales
            retCode = 0
            retTxt = ""
            usuario = None
            pwd = None
            apel1 = None
            apel2 = None
            email = None
            telefono = None

            # Crear la tupla de parámetros
            out_params = [retCode, retTxt, usuario, pwd, apel1, apel2, email, telefono]

            # Código adicional que modifica out_params de alguna manera
            # out_params = mi_db.call_procedure('valida_usuario', out_params)

            # Lista de nombres de las variables
            var_names = ['retCode', 'retTxt', 'usuario', 'pwd', 'apel1', 'apel2', 'email', 'telefono']

            # Asignar los valores de la tupla a las variables dinámicamente
            for i, var_name in enumerate(var_names):
                locals()[var_name] = out_params[i]

            # Verificar los valores asignados
            print(retCode)
            print(retTxt)
            print(usuario)
            print(pwd)
            print(apel1)
            print(apel2)
            print(email)
            print(telefono)

            '''


            mitxtCtr = 'Asigno Var'
            retCode = 0
            retTxt = ""
            apel1 = None
            apel2 = None
            email = None
            telefono = None

            mitxtCtr = 'llama a CallProc'
            out_params = mi_db.call_procedure('valida_usuario', [retCode, retTxt, usuario, pwd, apel1, apel2, email, telefono])
            # print(type(out_params))
            # Asignar los valores de salida a las variables
            mitxtCtr = 'Asgina'
            retCode = out_params[0]
            retTxt = out_params[1]
            apel1 = out_params[4]
            apel2 = out_params[5]
            email = out_params[6]
            telefono = out_params[7]

            if retCode != 0:
                mitxtCtr = 'return Ko'
                return UserValidationResponse(retCode=retCode, retTxt=retTxt)
            else:
                mitxtCtr = 'return Ok'
                return Usuario(usuario, apel1, apel2, email, pwd, telefono)
         
        except Exception as err:
            return UserValidationResponse(retCode=-1, retTxt=f"({mitxtCtr}): {str(err)}", retTxt2="esta es otra")
            