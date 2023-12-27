print("El numero mas grande de 3 ingresados ")
print()

a=int(input("Digita el primer numero: "))
b=int(input("Digita el segundo numero:"))
c=int(input("Digita el tercer numero: "))

mayor=a

if a>b and a>c:
    print(f"El numero {a} es el numero mas grande de los tres")

elif b>a and b>c:
    print(f"El numero {b} es el numero mas grande de los tres")
elif c>a and c>b:
    print(f"El numero {c} es el numero mas grande de los tres")
else:
    if a==b and a==c and b==c:
        print("Los tres son iguales")
    elif a==b or a==c or b==c:
        print("Dos numeros son iguales")