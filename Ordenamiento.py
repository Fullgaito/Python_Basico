# Definir las dos listas originales
lista1 = [3, 7, 1, 5, 9]
lista2 = [2, 8, 4, 6, 0]

# Combinar las dos listas en una sola
lista_combinada = lista1 + lista2

# Implementar el algoritmo de ordenamiento 
def ordenamiento(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Ordenar la lista de forma descendente 
ordenamiento(lista_combinada)

print("Lista combinada ordenada de forma descendente:", lista_combinada)
