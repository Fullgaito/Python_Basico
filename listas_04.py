"""
Dada una lista cuya longitud es digitada por el usuario agregar uno a uno cada uno
de sus elementos segun corresponda el tamaño de la lista y mostrar la suma de los elementos
digitados

"""

t=int(input("¿Cuantos numeros enteros contendra la lista?: "))
lista=list()
for i in range(1,t+1,1):
    a=int(input(f"Introduce el numero {i} en la lista: "))
    lista.append(a)

print(f"Lista:{lista}")
print(f"La suma total de los elementos es: {sum(lista)}")

"""
Dada una lista ya definida eliminar un elemento que el usuario digita por teclado sin importar si esta
en mayuscula o en minuscula y si se encuentra en mas de una vez se debe eliminar por completo
ese caracter.

"""

letras=["A","B","b","c","E","e","f"]
print(letras)
caracter=input("Introduce el elemento que desea eliminar: ")
for i in range(0,len(letras),1):
    if caracter in letras:
        letras.remove(caracter)
    elif caracter.lower() in letras:
        letras.remove(caracter.lower())

print(f"Elemento eliminado: {letras}")

"""
Dada una lista con numeros eliminar el primero y el ultimo y agregar estos numeros a una nueva lista
"""
numeros=[1,2,3,4,5]
eliminados=list()
print(f"Lista original: {numeros}")
eliminados.append(numeros.pop(0))
eliminados.append(numeros.pop())
print(f"Lista numeros: {numeros}")
print(f"Lista numeros eliminados: {eliminados}")

