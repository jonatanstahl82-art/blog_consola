archivo = open("2-test.txt", "w")
archivo.write("Python\n")
archivo.write("Django\n")
archivo.close()

archivo = open("2-test.tx", "r")
contenido = archivo.read()
archivo.close()
print(contenido)