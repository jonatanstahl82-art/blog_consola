from .datos import posts

from .operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag

from .validaciones import validar_post

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

def iniciar_menu():
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
            for post in posts:
                valido, mensaje = validar_post(post)
                print(f"Post ID {post.get('id')}: {mensaje}")
                
        elif opcion == 5:
            print("Saliendo del menú...")
            break
            
        else:
            print("Opción inválida. Por favor, ingresá un número del 1 al 5.")