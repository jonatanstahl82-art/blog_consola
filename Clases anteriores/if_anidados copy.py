edad = int(input("Ingrese su edad: "))
if edad < 13:  
    print("eres niño")
elif edad <= 17:
    print("eres adolescente")
elif edad < 65:
    print("eres adulto aportante")
elif edad < 80:
    print("eres adulto mayor")
elif edad >= 80:
    print("eres anciano")
    