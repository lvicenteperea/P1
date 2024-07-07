from pydantic import BaseModel, EmailStr

class Usuario(BaseModel):
    nombre: str
    apellido1: str
    apellido2: str
    email: EmailStr
    pwd: str
    telefono: str

    def __init__(self, nombre: str, apellido1: str, apellido2: str, email: EmailStr, pwd: str, telefono: str):
        super().__init__(nombre=nombre, apellido1=apellido1, apellido2=apellido2, email=email, pwd=pwd, telefono=telefono)

    # Getters
    def get_nombre(self) -> str:
        return self.nombre

    def get_apellido1(self) -> str:
        return self.apellido1

    def get_apellido2(self) -> str:
        return self.apellido2

    def get_email(self) -> EmailStr:
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

    def set_email(self, email: EmailStr) -> None:
        self.email = email

    def set_pwd(self, pwd: str) -> None:
        self.pwd = pwd

    def set_telefono(self, telefono: str) -> None:
        self.telefono = telefono

    # Método para obtener el nombre completo en letra capital
    def nombre_completo_capital(self) -> str:
        nombre_completo = f"{self.nombre} {self.apellido1} {self.apellido2}"
        return nombre_completo.title()
