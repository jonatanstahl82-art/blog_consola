def guardar_archivo(nombre_archivo: str) -> bool:
    """Guarda un archivo"""
    try:
        with open(nombre_archivo, "w") as archivo:
            archivo.write("Python\n")
            archivo.write("Django\n")
            return True
    except Exception as error:
        print("Error: ", type(error))
        return False

def leer_archivo(nombre_archivo: str) -> str | None:
    """Lee un archivo"""
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print("- El archivo no existe.")
    except Exception as error:
        print("Error: ", type(error))
    else:
        return contenido


def mostrar_contenido_terminal(contenido: str) -> None:
    print(contenido)

def main():
    NOMBRE_ARCHIVO = "3-test.txt"
    if not guardar_archivo(NOMBRE_ARCHIVO):
        print("Error al crear el archivo. Sale del programa")
        return
    contenido = leer_archivo(NOMBRE_ARCHIVO)
    if contenido:
        mostrar_contenido_terminal(contenido)

main()