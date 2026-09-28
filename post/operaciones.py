def listar_posts(lista):
    print("\n=== LISTA DE POSTS ===")
    for post in lista:
        autor_info = post.get('autor')
        nombre_autor = autor_info.get('nombre') if isinstance(autor_info, dict) else "Desconocido"
        print(f"ID: {post.get('id')} | Título: {post.get('titulo', 'Sin Título')} | Autor: {nombre_autor}")

def buscar_por_titulo(lista, termino):
    if not termino:
        return []
    
    termino_lower = termino.strip().lower()
    return [post for post in lista if termino_lower in post.get('titulo', '').lower()]

def filtrar_por_tag(lista, tag):
    if not tag:
        return []
    tag_lower = tag.strip().lower()
    return [
        post for post in lista 
        if isinstance(post.get('tags'), list) and tag_lower in [t.lower() for t in post.get('tags')]
    ]