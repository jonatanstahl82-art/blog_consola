perfil_autor = {
    'nombre': 'Ricardo Gutierrez.',
    'bio': 'Analista de datos y creador de contenido sobre programación.',
    'bspecialidad': 'Python, Django y PowerBi',
    'redes_sociales': ['@richard_data', '@richard_python', '@richard_aps']
}

estados_post = ('Borrador', 'Publicado', 'Archivado')
etiquetas_blog = {'Python', 'Django', 'Frontend', 'Backend', 'Data Analytics'}

posts = [
    {
        'id': 1,
        'titulo': 'Iniciando Python',
        'contenido': 'Aprende las bases de Python desde cero.',
        'autor': perfil_autor,
        'categoria': 'Programación',
        'tags': ['Python', 'Principiantes', 'Inicial'],
        'estado': 'Publicado'   
    },
    {
        'id': 2,
        'titulo': 'El Análisis de Datos',
        'contenido': 'Estrategias clave para ser analista.',
        'autor': perfil_autor,
        'categoria': 'Data',
        'tags': ['Python', 'Avanzados', 'Analista'],
        'estado': 'Borrador'   
    },
    {
        'id': 3,
        'titulo': '¡Hacelo más lindo con PowerBi!',
        'contenido': 'Dashboards interactivos en pocos pasos.',
        'autor': perfil_autor,
        'categoria': 'Visualización',
        'tags': ['Python', 'Avanzados', 'Interfaz'],
        'estado': 'Archivado'
    },
    {
        'id': 4,
        'titulo': '', # Título vacío
        'autor': 'Ricardo', # No es un diccionario
        'tags': 'Python', # Debería ser lista
        'estado': 'Inexistente' # Estado no válido
    }
]


def mostrar_menu():
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")
    
    try:
        opcion = int(input("Seleccioná una opción (1-5): "))
        return opcion
    except ValueError:
        return None

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


if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()
        
        if opcion is None:
            print("Error: Por favor, ingresá un número entero válido.")
            continue
            
        if opcion == 1:
            listar_posts(posts)
            
        elif opcion == 2:
            termino = input("Ingresá el título a buscar: ")
            if not termino.strip():
                print("El término de búsqueda no puede estar vacío.")
            else:
                resultados = buscar_por_titulo(posts, termino)
                if resultados:
                    for post in resultados:
                        print(f"Post -> ID: {post.get('id')}, Título: {post.get('titulo')}")
                else:
                    print("No se encontraron publicaciones con ese título.")
                    
        elif opcion == 3:
            tag = input("Ingresá el tag a filtrar: ")
            if not tag.strip():
                print("El tag a buscar no puede estar vacío.")
            else:
                resultados = filtrar_por_tag(posts, tag)
                if resultados:
                    for post in resultados:
                        print(f"Post -> ID: {post.get('id')}, Título: {post.get('titulo')}, Tags: {post.get('tags')}")
                else:
                    print("No se encontraron posts con ese tag.")
                    
        elif opcion == 4:
            print("\n=== VALIDACIÓN DE POSTS ===")
            for post in posts:
                es_valido, mensaje = validar_post(post)
                post_id = post.get('id', 'Desconocido')
                if es_valido:
                    print(f"Post {post_id}: Válido")
                else:
                    print(f"Post {post_id}: Error - {mensaje}")
                    
        elif opcion == 5:
            print("¡Hasta luego! Saliendo del sistema...")
            break
            
        else:
            print("Opción fuera de rango. Por favor ingresá un número del 1 al 5.")