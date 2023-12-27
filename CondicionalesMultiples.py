print("Conversor")
print()
print("Menu de opciones")
print("Presiona 1 para convertir de numero a palabra")
print("Presiona 2 para convertir de palabra a numero")

eleccion=int(input("Cual es tu opcion: "))


if eleccion==1:
    print("Conversor de numero a palabra")
    numero=int(input("Cual es el numero a convertir a palabra: "))
    if numero==1:
         print("El numero es el uno")
    elif numero==2:
        print("El numero es el dos")
    elif numero==3:
        print("El numero es el tres")
    elif numero==4:
        print("El numero es el cuatro")
    else:
        print("El numero no esta registrado")
    
elif eleccion==2:
    print("Conversor de palabra a numero")
    numero=str(input("Cual es la palabra a convertir a numero: "))
    numero=numero.lower()
    if numero=="uno":
        print("El numero es el 1")
    elif numero=="dos":
        print("El numero es el 2")
    elif numero=="tres":
        print("El numero es el 3")
    elif numero=="cuatro":
        print("El numero es el 4")
    else:
        print("El numero no esta registrado")

else:
    print("Opcion incorrecta")