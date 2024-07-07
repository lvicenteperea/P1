
from typing import List, Dict, Any
from ..models.usuario import Usuario

def usuario_a_dict(usuario: Usuario) -> Dict[str, Any]:
    return usuario.dict()

def cursor_a_lista_de_dict(cursor) -> List[Dict[str, Any]]:
    columns = [col[0] for col in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    return results

def dict_a_usuario(data: Dict[str, Any]) -> Usuario:
    return Usuario(**data)
