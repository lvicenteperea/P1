import mysql.connector
from mysql.connector import Error
from .db import Database
from .models.usuario import Usuario
from .schemas.usuario import cursor_a_lista_de_dict, dict_a_usuario

class MySQLDatabase(Database):
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def create_connection(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if connection.is_connected():
                return connection
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
        return None

    def call_procedure(self, procedure_name, *args):
        connection = self.create_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.callproc(procedure_name, args)
                results = []
                for result in cursor.stored_results():
                    results.append(result.fetchall())
                connection.commit()
                return results
            except Error as e:
                print(f"Error al llamar al procedimiento {procedure_name}: {e}")
            finally:
                cursor.close()
                connection.close()
        return None

    def validate_user(self, email, pwd):
        connection = self.create_connection()
        if connection:
            cursor = connection.cursor(dictionary=True)
            try:
                cursor.execute("CALL ValidarUsuario(%s, %s)", (email, pwd))
                result = cursor.fetchone()
                if result:
                    usuario = dict_a_usuario(result)
                    return {"codigo": 0, "mensaje": "Usuario conectado correctamente", "usuario": usuario_a_dict(usuario)}
                else:
                    return {"codigo": -1, "mensaje": "Usuario o contraseña incorrectos"}
            except Error as e:
                print(f"Error al validar usuario: {e}")
                return {"codigo": -2, "mensaje": "Error al conectar con la base de datos"}
            finally:
                cursor.close()
                connection.close()
        return {"codigo": -2, "mensaje": "Error al conectar con la base de datos"}
