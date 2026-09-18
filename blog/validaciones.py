from .datos import estados_post


def validar_post(post):
    
    if not isinstance(post, dict):
        return False, "El post no es un diccionario"
    
    
    claves_requeridas = ['id', 'titulo', 'contenido', 'autor', 'tags', 'estado']
    for clave in claves_requeridas:
        if clave not in post:
            return False, f"Falta la clave '{clave}'"
            
    if not str(post.get('titulo', '')).strip():
        return False, "El título está vacío"
        
    if not str(post.get('contenido', '')).strip():
        return False, "El contenido está vacío"
        
    if not isinstance(post.get('autor'), dict) or 'nombre' not in post.get('autor', {}):
        return False, "El autor debe ser un diccionario con la clave 'nombre'"
        
    if not isinstance(post.get('tags'), list):
        return False, "Los tags deben ser una lista"
        
    if post.get('estado') not in estados_post:
        return False, f"Estado inválido: '{post.get('estado')}'"
        
    return True, "Válido"