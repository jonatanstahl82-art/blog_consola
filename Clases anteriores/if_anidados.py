edad = int(input("Ingrese su edad: "))
if edad <= 12:  
    print("eres niño")
else:
    if edad <= 17:
        print("eres adolescente")
    else:
        if edad <= 65:

            print("eres adulto aportante")
        else:
            if edad <= 79:

                print("eres adulto mayor")
            else:

                if edad >= 80:
                    print("eres anciano")