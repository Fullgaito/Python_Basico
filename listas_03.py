#Eliminar una lista - instruccion del
"Elimina todos o parte de los elementos de una lista"

pares=[2,4,6,8,10,12,14]
del pares [0:3] #elimina los elementos que estan en las posiciones indicadas
print(pares)
del pares[:] #elimina todos los elementos de una lista
print(pares)
#del pares elimina la lista por completo
#print(pares)

#Invertir una lista - metodo reverse()

futbolistas=["Messi","Cristiano","Haaland","Salah"]
print(f"Lista original: {futbolistas}")
futbolistas.reverse()
print(f"Lista invertida: {futbolistas}")

#Ordenar elementos de una lista - sort()

numeros=[5,3,1,2,4]
print(f"Lista original: {numeros}")
numeros.sort(reverse=True) #Ordena de forma descendente
print(f"Lista descendente: {numeros}")
numeros.sort() #ordena de forma ascendente
print(f"Lista ascendente: {numeros}")

#Buscar elementos en una lista - index()

vocales=["a","e","i","o","u"]
print(vocales.index("e"))

#Concatenar listas - extend()

invitados=["carolina","Juan","Sebastian","Rosa"]
amigos=["Luis","Manuel"]
#invitados=invitados+amigos Otra forma de concatenar
invitados.extend(amigos)
print(invitados)

#Sumar los elementos de una lista -sum()

impares=[3,5,7,9,11]
print(sum(impares))
