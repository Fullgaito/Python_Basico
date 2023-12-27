"""Conjuncion - and
disyuncion-or
negacion-not"""

#Ejemplo AND

#Evalua mas de una condicion logica en un condicional y las dos condiciones se deben de cumplir 

num=int(input("Ingrese un numero: "))
if num==5 and num>=5:
    print("Se cumple")
else:
    print("No se cumple")

#Ejemplo OR

#Evalua dos o mas condiciones y cualquiera que se cumpla la condicion es verdadera

if num==5 or num>10:
    print("Se cumple para cualquiera de los dos casos")

#Ejemplo NOT

#Hace que se niege una expresion cambiando su valor booleano dado en la condicion

if not num>5:
    print("Se nego")