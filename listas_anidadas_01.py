"""
Es una lista dentro de otra lista que se puede ver y entender como una matriz
donde se trabaja con filas y columnas donde se almacena cada uno de los elementos
contenidos.
"""

matriz=[[0,1,0],[0,1,0]] #2x3
print(matriz[0])
print(matriz[1])

#Matriz desde teclado

n=int(input("Cuantas filas tendra la matriz?: "))
m=int(input("Cuantas columnas tendra la matriz?: "))
filas=list()
matrix=list()
for i in range(n):
    for j in range(m):
        elemento=int(input(f"Introduce el elemento [{i}][{j}]: "))
        filas.append(elemento)
        elemento=0
    matrix.append(filas)
    filas=list()
for s in matrix:
    print(s)

#funcion de crear matriz desde teclado

def creacion_matriz():
    n=int(input("Cuantas filas tendra la matriz?: "))
    m=int(input("Cuantas columnas tendra la matriz?: "))
    filas=list()
    matrix=list()
    for i in range(n):
        for j in range(m):
            elemento=int(input(f"Introduce el elemento [{i}][{j}]: "))
            filas.append(elemento)
            elemento=0
        matrix.append(filas)
        filas=list()
    return matrix