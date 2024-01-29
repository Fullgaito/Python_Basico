#Acceder a los elementos de una lista
"Se hace necesario conocer el indice para acceder a los elementos"

lista=[2,3,"Hola"]
print(lista[1])
print(lista[0:2])

#modificar elementos de una lista

letras=["a","b","c","d","e"]
print(letras)
letras[1]="e"
print(letras)
letras[0:2]=["i","h"]
print(letras)

#Agregar elementos a una lista - append()
"Agrega elementos al final de la lista"

colores=["Azul","Rojo","Amarillo","Verde"]
print(colores)
colores.append("Morado")
print(colores)

#insertar elementos a una lista - insert()
"Inserta elementos en una posicion determinada"

numeros=[0,1,3,4,5]
print(numeros)
numeros.insert(2,2) #primer indice la posicion a insertar dentro de la lista y el otro parametro dato a insertar
print(numeros)

#Eliminar elementos de una lista - pop()
"Retorna el elemento que se elimina"

paises=["colombia","Venezuela","Ecuador","Argentina","Uruguay"]
print(paises)
paises.pop() #elimina el ultimo elemento
print(paises)
paises.pop(1) #elimina el elemento que se encuentra en el parametro
print(paises)
paises.pop(-2)
print(paises)

#Eliminar elementos de una lista - remove()
"Permite eliminar el elemento que se encuentra dentro del argumento"

vocales=["a","e","i","o","u"]
print(vocales)
vocales.remove("i")
print(vocales)
