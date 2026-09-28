perfil_autor = {
        'nombre': 'Ricardo Gutierrez.',
        'bio': 'Analista de datos y creador de contenido sobre programación.',
        'bspecialidad': 'Python, Django y PoweBi',
        'redes_sociales': ['@richard_data', '@richard_python', '@richard_aps']
}
estados_post = ('Borrador', 'Publicado', 'Archivado')
etiquetas_blog = {'Python', 'Django', 'Frontend', 'Backend', 'Data Analytics','Frontend','Python'}
posts = [
        {
                'id': 1,
                'titulo': 'Iniciando Python',
                'autor': perfil_autor,
                'categoria': 'Programación',
                'tags': ['Python', 'Principiantes', 'Inicial'],
                'estado': 'Publicado'   
        },
        {
                'id': 2,
                'titulo': 'El Analisis de Datos',
                'autor': perfil_autor,
                'categoria': 'Data',
                'tags': ['Python', 'Avanzados', 'Analista'],
                'estado': 'Borrador'   
        },
        {
                'id': 3,
                'titulo': '¡Hacelo mas lindo con PowerBi!',
                'autor':  perfil_autor,
                'categoria': 'Visualizacion',
                'tags': ['Python', 'Avanzados', 'Interfaz'],
                'estado': 'Archivado'
        }
]


while True:
    print('--- MENU DEL BLOG ---')
    print('1. Ver todos los posts')
    print('2. Buscar por titulo')
    print('3. Filtrar por tag')
    print('4. Salir')
    opcion = input('Elegí la opción del menú: ')

    if opcion == '1':
        print('\nEstos son los posts disponibles:')
        for post in posts:
            print(f"- {post['titulo']} | Autor: {post['autor']['nombre']}")

    elif opcion == '2':
        busqueda = input("Buscar por título: ").lower()
        print('\nResultados encontrados:')
        for post in posts:
            if busqueda in post["titulo"].lower():
                print(f"- {post['titulo']} | Autor: {post['autor']['nombre']}")

    elif opcion == '3':
        
        tag_buscado = input("Ingresá el tag: ").lower()
        print(f"\nPosts con el tag '{tag_buscado}':")
        
        
        for post in posts:
           
            tags_lower = [tag.lower() for tag in post["tags"]]
            
          
            if tag_buscado in tags_lower:
                print(f"- {post['titulo']}")

    elif opcion == '4':
        print("Gracias por usar el buscador del blog. ¡Hasta luego!")
        break

    else:
        print("Opción inválida, intenta de nuevo")           
