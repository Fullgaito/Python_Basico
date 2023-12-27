"operadores relaciones"

"""
se compara dos elementos entre si
menor que  <
mayor que >
igual a ==
es diferente !=
menor o igual a <=
mayor o igual a >=

"""

#ejemplo

print("Introduce dos numeros a comparar")

a=int(input("Introduce el primer numero: "))
b=int(input("Introduce el segundo numero: "))

print(f"Los numeros a comparar son {a} y {b}")

if a==b:
    print("Los numeros son iguales")
elif a>b:
    print(f"El numero {a} es mayor al {b}")
elif b>a:
    print(f"El numero {b} es mayor al {a}")

