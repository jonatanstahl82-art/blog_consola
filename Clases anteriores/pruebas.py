import math

radio = float(input('Ingreses el radio del circulo: '))

area = math.ceil(math.pi*radio**2)

bolsa = math.ceil(area/10)

costo = 50*bolsa

print(f'El area a cubrir es de {area} m2, se requieren {bolsa} bolsas de fertilizante, y el costo es de ${costo} ')

