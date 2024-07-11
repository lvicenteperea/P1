import cx_Oracle
from .db import Database
from .models.usuario import Usuario
from .schemas.usuario import cursor_a_lista_de_dict, dict_a_usuario, usuario_a_dict  # Asegúrate de que usuario_a_dict está definida

class OracleDatabase(Database):
    def __init__(self, dsn, user, password):
        self.dsn = dsn
        self.user = user
        self.password = password

    def create_connection(self):
        try:
            connection = cx_Oracle.connect(
                user=self.user,
                password=self.password,
                dsn=self.dsn
            )
            return connection
        except cx_Oracle.Error as e:
            print(f"Error al conectar a Oracle: {e}")
        return None

    def call_procedure(self, procedure_name, *args):
        connection = self.create_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.callproc(procedure_name, args)
                results = []
                for result in cursor:
                    results.append(result.fetchall())
                # No es necesario hacer commit aquí a menos que sea una transacción
                return results
            except cx_Oracle.Error as e:
                print(f"Error al llamar al procedimiento {procedure_name}: {e}")
            finally:
                cursor.close()
                connection.close()
        return None

    def validate_user(self, email, pwd):
        connection = self.create_connection()
        if connection:
            cursor = connection.cursor()
            try:
                out_cursor = connection.cursor()
                cursor.callproc("ValidarUsuario", [email, pwd, out_cursor])
                result = out_cursor.fetchone()
                if result:
                    usuario_data = {
                        "nombre": result[0],
                        "apellido1": result[1],
                        "apellido2": result[2],
                        "email": result[3],
                        "telefono": result[4]
                    }
                    usuario = dict_a_usuario(usuario_data)
                    return {"codigo": 0, "mensaje": "Usuario conectado correctamente", "usuario": usuario_a_dict(usuario)}
                else:
                    return {"codigo": -1, "mensaje": "Usuario o contraseña incorrectos"}
            except cx_Oracle.Error as e:
                print(f"Error al validar usuario: {e}")
                return {"codigo": -2, "mensaje": "Error al conectar con la base de datos"}
            finally:
                cursor.close()
                connection.close()
        return {"codigo": -2, "mensaje": "Error al conectar con la base de datos"}
