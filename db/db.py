from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def create_connection(self):
        pass

    @abstractmethod
    def call_procedure(self, procedure_name, *args):
        pass

    @abstractmethod
    def validate_user(self, email, pwd):
        pass

class DatabaseFactory:
    @staticmethod
    def get_database(db_type, **kwargs):
        if db_type == "mysql":
            from .mysql_db import MySQLDatabase
            return MySQLDatabase(**kwargs)
        elif db_type == "oracle":
            from .oracle_db import OracleDatabase
            return OracleDatabase(**kwargs)
        else:
            raise ValueError(f"Unsupported database type: {db_type}")

'''
EJEMPLO DE LLAMADA:
from db import DatabaseFactory

# Parámetros de conexión
mysql_params = {
    'host': 'localhost',
    'database': 'mi_base_datos',
    'user': 'mi_usuario',
    'password': 'mi_contraseña'
}

oracle_params = {
    'dsn': 'mi_dsn',
    'user': 'mi_usuario',
    'password': 'mi_contraseña'
}

# Selecciona la base de datos a usar
db_type = 'mysql'  # o 'oracle'

if db_type == 'mysql':
    db = DatabaseFactory.get_database('mysql', **mysql_params)
elif db_type == 'oracle':
    db = DatabaseFactory.get_database('oracle', **oracle_params)
else:
    raise ValueError("Tipo de base de datos no soportado")

# Usa la instancia de la base de datos
result = db.validate_user('email@example.com', 'password123')
print(result)


'''