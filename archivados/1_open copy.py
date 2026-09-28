#archivo = open("2-test.txt", "w") as archivo
#archivo.write("Python\n")
#archivo.write("Django\n")
#archivo.close()

#try:
#    archivo = open("2-test.tx", "r")
 #   contenido = archivo.read()
  #  archivo.close()
   # print(contenido)
#except FileNotFoundError:
 #   print("el archivo no existe")

#try:
 #   archivo = open("2-test.tx", "r")
  #  contenido = archivo.write()
   # archivo.close()
    #print(contenido)
#except FileNotFoundError:
#    print("el archivo no existe")

try:
    with open("2-test.txt", "w") as archivo:
        archivo.write("Python\n")
        archivo.write("Django\n")
except Exception as error:
    print("Error: ", type(error))
try:
    with open("2-test.tx", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("- El archivo no existe.")
except Exception as error:
    print("Error: ", type(error))
else:
    print(contenido)

def escribir_archivo(nombre_archivo, contenido_lineas):
    try:
        with open(nombre_archivo, "w") as archivo:
            archivo.writelines(contenido_lineas)
    except Exception as error:
        print("Error al escribir el archivo:", type(error))

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            return archivo.read()
    except FileNotFoundError:
        print("- El archivo no existe.")
    except Exception as error:
        print("Error al leer el archivo:", type(error))
    return None

escribir_archivo("2-test.txt", ["Python\n", "Django\n"])

contenido = leer_archivo("2-test.tx")
if contenido:
    print(contenido)