import json
import os

RUTA_JSON = "posts.json"



def guardar_posts(lista_posts, ruta=RUTA_JSON):
    """Guarda la lista de posts (objetos o dicts) en el archivo JSON."""
    datos_a_guardar = []
    for p in lista_posts:
        if hasattr(p, "to_dict"):
            datos_a_guardar.append(p.to_dict())
        elif isinstance(p, dict):
            datos_a_guardar.append(p)

    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos_a_guardar, f, ensure_ascii=False, indent=4)


def cargar_posts(ruta=RUTA_JSON):
    """Carga los posts desde el JSON. Si no existe, devuelve lista vacía."""
    if not os.path.exists(ruta):
        return []
    
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []




def listar_posts(lista):
    print("\n=== LISTA DE POSTS ===")
    if not lista:
        print("No hay posts registrados.")
        return

    for post in lista:
        
        if hasattr(post, "id"):
            autor = post.autor.get("nombre") if isinstance(post.autor, dict) else post.autor
            print(f"ID: {post.id} | Título: {post.titulo or 'Sin Título'} | Autor: {autor}")
        
        else:
            autor_info = post.get("autor")
            nombre_autor = autor_info.get("nombre") if isinstance(autor_info, dict) else "Desconocido"
            print(f"ID: {post.get('id')} | Título: {post.get('titulo', 'Sin Título')} | Autor: {nombre_autor}")


def buscar_por_titulo(lista, termino):
    if not termino:
        return []
    termino_lower = termino.strip().lower()
    
    resultado = []
    for post in lista:
        titulo = post.titulo if hasattr(post, "titulo") else post.get("titulo", "")
        if termino_lower in (titulo or "").lower():
            resultado.append(post)
    return resultado


def filtrar_por_tag(lista, tag):
    if not tag:
        return []
    tag_lower = tag.strip().lower()
    
    resultado = []
    for post in lista:
        tags = post.tags if hasattr(post, "tags") else post.get("tags", [])
        if isinstance(tags, list) and tag_lower in [t.lower() for t in tags]:
            resultado.append(post)
    return resultado
