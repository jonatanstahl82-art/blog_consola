from .datos import posts as posts_iniciales, perfil_autor
from .modelos import Post
from .operaciones import (
    listar_posts, 
    buscar_por_titulo, 
    filtrar_por_tag, 
    cargar_posts, 
    guardar_posts
)
from .validaciones import validar_post

def cargar_datos_iniciales():
    """Carga desde JSON o inicializa con datos.py si está vacío."""
    datos = cargar_posts()
    if not datos:
        
        guardar_posts(posts_iniciales)
        datos = posts_iniciales
    
    
    lista_objetos = []
    for d in datos:
        nuevo_post = Post(
            id=d.get("id"),
            titulo=d.get("titulo", ""),
            contenido=d.get("contenido", ""),
            autor=d.get("autor"),
            categoria=d.get("categoria", "General"),
            tags=d.get("tags", []),
            estado=d.get("estado", "Borrador")
        )
        lista_objetos.append(nuevo_post)
    return lista_objetos


def crear_nuevo_post(lista_posts):
    """Pide datos por consola, crea una instancia de Post y persiste."""
    print("\n--- NUEVO POST ---")
    nuevo_id = max([p.id for p in lista_posts if hasattr(p, 'id') and p.id is not None], default=0) + 1
    titulo = input("Título: ").strip()
    contenido = input("Contenido: ").strip()
    categoria = input("Categoría: ").strip()
    tags_str = input("Tags (separados por coma): ")
    tags = [t.strip() for t in tags_str.split(",") if t.strip()]

    post_obj = Post(
        id=nuevo_id,
        titulo=titulo,
        contenido=contenido,
        autor=perfil_autor,
        categoria=categoria,
        tags=tags,
        estado="Publicado"
    )

    lista_posts.append(post_obj)
    guardar_posts(lista_posts)
    print(f"¡Post '{titulo}' creado y guardado con éxito (ID: {nuevo_id})!")


def mostrar_menu():
    print("\n--- MENÚ DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por título")
    print("3. Filtrar por tag")
    print("4. Crear nuevo post")
    print("5. Validar posts")
    print("6. Salir")
    
    try:
        return int(input("Seleccioná una opción (1-6): "))
    except ValueError:
        return None


def iniciar_menu():
    
    posts = cargar_datos_iniciales()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == 1:
            listar_posts(posts)
            
        elif opcion == 2:
            termino = input("Ingresá el término de búsqueda: ")
            resultados = buscar_por_titulo(posts, termino)
            listar_posts(resultados)
            
        elif opcion == 3:
            tag = input("Ingresá el tag para filtrar: ")
            resultados = filtrar_por_tag(posts, tag)
            listar_posts(resultados)

        elif opcion == 4:
            crear_nuevo_post(posts)
            
        elif opcion == 5:
            for post in posts:
                # Si es objeto, validamos su representación en dict
                p_dict = post.to_dict() if hasattr(post, "to_dict") else post
                valido, mensaje = validar_post(p_dict)
                print(f"Post ID {p_dict.get('id')}: {mensaje}")
                
        elif opcion == 6:
            print("Saliendo del blog. ¡Hasta luego!")
            break
            
        else:
            print("Opción inválida. Por favor, ingresá un número del 1 al 6.")
