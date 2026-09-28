"""

Docstring para clase_2.ejerc

Actividad: Desafío de Listas

Consigna:

 

Crea dos listas lista_1 y lista_2, con cualquier elemento que quieras.

Realiza los siguientes puntos usando las funciones integradas ya vistas y

 el método slice [ : ] Imprime la lista correspondiente luego de cada punto.

- Añade a la lista_1 el 456789 y luego el "Hola Mundo"

- Luego añade a la lista_2 el "Hola y adiós", y luego el 5555

- Genera una lista_3 con todos los elementos de la lista_1 sin considerar el último elemento [:]

- Genera una lista_4 con todos los elementos de la lista_2 menos el primero y el último elemento [:]

- Finalmente, genera una lista_5 con los elementos de la lista_4 y de la lista_3

"""

lista_1 = ['Hola', 26, 'buen día', True]
print (lista_1[:])
lista_2 = [1, 2, 56, 46, 77, 5, ]
print (lista_2 [:])
lista_1.append (456789)
lista_1.append ('hola mundo')
print (lista_1[:])
lista_2.append ('Hola y adios')
lista_2.append (5555)
print (lista_2[:])
lista_3 = lista_1 [:len(lista_1)-1] # O lista_3 = lista_1 [:-1]
print (lista_3)
lista_4 = lista_2 [1:-1]
print(lista_4)
