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
a=creacion_matriz()
b=creacion_matriz()

if len(a)==len(b):
    print("Se pueden sumar")
    matriz1=list()
    final=list()
    for u in range(len(a)):
        for q in range(len(b)):
            matriz1.append(a[u][q]+b[u][q])
        final.append(matriz1)
        matriz1=list()
else:
    print("No se pueden sumar")
for w in final:
    print(w)


