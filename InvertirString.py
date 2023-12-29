"""
Dado un string imprimirlo al reves

"""

string=input("Digite un string: ")


for i in range(len(string)-1,-1,-1):
    print(string[i],end="")