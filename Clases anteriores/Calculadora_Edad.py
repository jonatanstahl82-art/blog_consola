from datetime import date, datetime
from dateutil.relativedelta import relativedelta

nombre = input("Dame tu nombre: ")
apellido = input("Dame tu apellido: ")
fecha_str = input("Dame tu fecha de nacimiento (dd/mm/yyyy): ")

nacimiento = datetime.strptime(fecha_str, "%d/%m/%Y").date()

hoy = date.today()
diferencia = relativedelta(hoy, nacimiento)

años = diferencia.years
meses = diferencia.months
dias = diferencia.days

print(f"Tu nombre es {apellido}, {nombre}, Tienes {años} años, {meses} meses y {dias} días.")

