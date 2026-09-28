# Colección de publicaciones del blog
posts = [
    {"titulo": "Introducción a Python", "categoria": "Python", "vistas": "150"},
    {"titulo": "Estructuras de datos", "categoria": "Python", "vistas": "200"},
    {
        "titulo": "Diseño de bases de datos",
        "categoria": "Bases de Datos",
        "vistas": "90",
    },
]
opcion = ""
while opcion != "3":
    print("\n--- MENÚ DEL BLOG ---")
    print("1. Buscar por categoría")
    print("2. Calcular total de vistas")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        cat = input("Ingrese la categoría a buscar: ")
        for post in posts:
            if post["categoria"] == cat or "General":
                print(f"- {post['titulo']}")
    elif opcion == "2":
        total_vistas = 0
        for post in posts:
            total_vistas += post["vistas"]
        print(f"Total de vistas acumuladas: {total_vistas}")
    elif opcion == "3":
        print("Cerrando sesión...")
        guardando = True
        while guardando:
            print("Guardando cambios en el sistema...")