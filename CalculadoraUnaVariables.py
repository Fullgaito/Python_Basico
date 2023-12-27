print("calculadora con una sola variable")
print()

print("menu de opciones")
print()

print("1.Suma \n2.Resta \n3.Multiplicacion \n4.Division \n5.Division Entera \n6.Exponente \n7.Modulo")
print()

eleccion=int(input("Introduce una opcion: "))

if eleccion==1:
    print("Elegiste suma")
    sum=float(input("Introduce un numero a sumar: "))
    sum+=float(input("Introduce un segundo numero a sumar: "))
    print(f"El resultado es: {sum}")
elif eleccion==2:
    print("Elegiste resta ")
    res=float(input("Introduce el primer numero a restar: "))
    res-=float(input("Introduce el segundo numero a restar: "))
    print(f"El resultado de la resta es: {res}")
elif eleccion==3:
    print("Elegiste multiplicacion ")
    mult=float(input("Introduce el primer numero a multiplicar: "))
    mult*=float(input("Introduce el segundo numero a multiplicar: "))
    print(f"El resultado de la multiplicacion es: {mult}")
elif eleccion==4:
    print("Elegiste division ")
    div=float(input("Introduce el primer numero a dividir: "))
    div/=float(input("Introduce el primer numero a dividir: "))
    print(f"El resultado de la division es: {div}")
elif eleccion==5:
    print("Elegiste division entera ")
    divi=float(input("Introduce un numero: "))
    divi//=float(input("Introduce otro numero: "))
    print(f"El resultado es: {divi}")
elif eleccion==6:
    print("Elegiste exponente ")
    a=float(input("Introduce la base: "))
    a**=float(input("Introduce el exponente"))
    print(f"El resultado es: {a}")
elif eleccion==7:
    print("Elegiste modulo o resto ")
    a=float(input("Introduce el primer numero: "))
    a%=float(input("Introduce el segundo numero: "))
    print(f"El resultado es: {a}")
else:
    print("Opcion incorrecta")