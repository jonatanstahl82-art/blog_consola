lista = ['una cadena', 11, 1.23, True, "otra cadena"]
#indices      0         1   2     3         4           siempre empieza a contar desde cero!
lista_vacia = [[], [], []]
print(lista[])

lista.append ('manzana')
lista.append ('uvas')
lista.append ('sandia')
lista.insert (1 'frutilla') #inserta info indexada


#####


None #valor nulo

lista.pop()
lista.remove()

#####
#slicing

otra_lista = lista[:] #pasame los elementos del comienmzo : Fin
print(otra_lista)

otra_lista = lista(3:5) # Muestra lis indices desde 3 a 4 (no incluye 5)

otra_lista = lista(3:5:2) # Muestra lis indices desde 3 a 4 (salta de a 2)

lista_de_frutas = lista_copy()
