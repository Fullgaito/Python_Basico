""""Dado un numero sumar los numeros anteriores a el de forma recursiva
Ejem= 5
5+4+3+2+1=15
"""
def sumar_anteriores(n,suma):
    if n==0:
        return suma
    else:
        suma+=n
        n=n-1
        return sumar_anteriores(n,suma)
print(sumar_anteriores(4,0))

""" Hacer potenciacion de forma recursiva"""

def potencia(base,exponente):
    if exponente==1:
        return base
    else:
        exponente-=1
        return base*potencia(base,exponente)
print(potencia(5,8))

"""Sumar elementos de una lista"""

def sumar(lista,suma,idx):
    if len(lista)==0:
        return suma
    else:
        suma+=lista[idx]
        lista.pop(idx)
        return sumar(lista,suma,0)
print(sumar([1,2,3,4,5],0,0))

"""Invertir una lista """

def invertir(lista,aux):
    if len(lista)==0:
        return aux
    elif len(lista)==1:
        aux.append(lista[0])
        return aux
    else:
        elemento=lista[-1]
        aux.append(elemento)
        lista.remove(elemento)
        return invertir(lista,aux)
print(invertir([1,2,3,4],[]))

""""Aplanar lista"""

def aplanar(lista,aux,idx,idx1):
    if len(lista[idx1])!=1:
        aux.append(lista[idx])
        return aux
    elif idx1==len(lista):
        return aux
    else:
        elemento=[lista[idx][idx1]]
        aux.append(elemento)
        resto=[lista[idx][idx1+1:idx]]
        aux.append(resto)
        return aplanar(lista,aux,idx-1,idx+1)
n=len([[3],[4],[2,1]])-1
print(aplanar([[3],[4],[2,1]],[],n,0))