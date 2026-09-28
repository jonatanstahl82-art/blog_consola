def saludo_nocturno():       #sienmpre en minuscula y _
    '''
    esta funcion se encarga de imprimir un saludo en pantalla.

    return: no devuelve nada
    '''                 #doc-string

    print('hola, buenas noches')
    # return 10
print(saludo_nocturno())

#print(mi_funcion())
saludo_nocturno ()

####################3

#argumenentos y parametros

def sumar(un_numero_entero, otro_numero_entero, numero_3):
    '''parametros:
    -un_numero_entero int(): numero entero
    -otro_numero_entero int(): numero entero
    
    funcionalidad
    suma dos numeros

    return: 
    devuelve la suma de los numenros enteros
    
    '''
    suma = un_numero_entero - otro_numero_entero  + numero_3
    return suma
    return un_numero_entero+otro_numero_entero
suma = sumar (10, 20, 30) #argumentos 10 (un_numero_entero) 20 (otro_numero_entero) son ordinales
suma_2 = sumar (otro_numero_entero=50, un_numero_entero=100, numero_3=30)
print(suma_2)
