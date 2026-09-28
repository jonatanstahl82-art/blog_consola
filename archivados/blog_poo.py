class Post:
    def __init__(self, titulo, contenido, autor):
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.estado = "borrador"  # Estado inicial del post es "borrador"

    def publicar(self):
        self.estado = "publicado"  # Cambia el estado a "publicado"

    def mostrar_info(self):
        return f"Título: {self.titulo}\nContenido: {self.contenido}\nAutor: {self.autor}\nEstado: {self.estado}"

posts = []
while True:
    print("1. Crear un nuevo post")
    print("2. Publicar un post")
    print("3. Mostrar información de un post")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        titulo = input("Ingrese el título del post: ")
        contenido = input("Ingrese el contenido del post: ")
        autor = input("Ingrese el autor del post: ")
        nuevo_post = Post(titulo, contenido, autor)
        posts.append(nuevo_post)
        print("Post creado exitosamente.\n")

    elif opcion == "2":
        if not posts:
            print("No hay posts disponibles para publicar.\n")
            continue
        for i, post in enumerate(posts):
            print(f"{i + 1}. {post.titulo} (Estado: {post.estado})")

        try:
            indice = int(input("Seleccione el número del post que desea publicar: ")) - 1
            if 0 <= indice < len(posts):
                posts[indice].publicar()
                print(f"Post '{posts[indice].titulo}' publicado exitosamente.\n")
            else:
                print("Índice inválido.\n")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.\n")

    elif opcion == "3":
        if not posts:
            print("No hay posts disponibles para mostrar.\n")
            continue
        for i, post in enumerate(posts):
            print(f"{i + 1}. {post.titulo} (Estado: {post.estado})")
        try:
            indice = int(input("Seleccione el número del post que desea ver: ")) - 1
            if 0 <= indice < len(posts):
                print(posts[indice].mostrar_info() + "\n")
            else:
                print("Índice inválido.\n")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.\n")

    elif opcion == "4":
        print("Saliendo del programa.")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.\n")
