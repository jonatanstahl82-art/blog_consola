# Pedir al uysuario su nombre
# Luego pedir su apellido
# Luego pedir suu edad
# Imprimir "tu n ombre es  {apellido}, {nombre}, Naciste en el año {fecha de nacimiento}"
from datetime import date
from dateutil.relativedelta import relativedelta

nombre = input("Dame tu nombre: ")
apellido = input("Dame tu apellido: ")
dia = int(input("Dame tu dia de nacimiento: "))
mes = int(input("Dame tu mes de nacimiento: "))
año = int(input("Dame tu año de nacimiento: "))
nacimiento= date(año, mes, dia)
# Fecha actual
hoy = date.today()
#Calcula la diferencia entre la fecha actual y la de nacimiento
diferencia= relativedelta(hoy, nacimiento)
x= diferencia.years
y= diferencia.months
z= diferencia.days
# Fecha de nacimiento
print(f"Tu nombre es {apellido}, {nombre}, Tienes {x} años, {y} meses y {z} días.")
