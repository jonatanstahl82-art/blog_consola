# Pedir al uysuario su nombre
# Luego pedir su apellido
# Luego pedir suu edad
# Imprimir "tu nombre es  {apellido}, {nombre}, Naciste en el año {fecha de nacimiento}"

nombre = input("Dame tu nombre: ")
apellido = input("Dame tu apellido: ")
edad = int(input("Dame tu edad: "))

fecha_de_nacimiento= 2026-edad

print(f"Tu nombre es: {apellido}, {nombre} y naciste en el año: {fecha_de_nacimiento}")