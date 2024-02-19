"""
El ácido desoxirribonucleico, el ADN, es la principal molécula de almacenamiento de información en los sistemas biológicos. 
Está compuesto por cuatro bases de ácidos nucleicos: guanina ('G'), citosina ('C'), adenina ('A') y timina ('T').
El ácido ribonucleico, ARN, es la principal molécula mensajera de las células. 
El ARN difiere ligeramente del ADN en su estructura química y no contiene timina. En el ARN, la timina se reemplaza por otro ácido nucleico, uracilo ('U').

Cree una función que traduzca una cadena de ADN determinada en ARN.

Por ejemplo:

"GCAT"  =>  "GCAU"
La cadena de entrada puede tener una longitud arbitraria; en particular, puede estar vacía. 
Se garantiza que todas las entradas serán válidas, es decir, cada cadena de entrada sólo estará formada por , 'G'y /o .'C''A''T'

"""

def dna_to_rna(dna):
    while "T" in dna:
        T=dna.find("T")
        dna=dna[0:T]+"U"+dna[T+1:len(dna)]
    return dna