"""
Metodos center(), ljust(), rjust()

Metodo center():

Permite centrar un String añadiendo espacios o caracteres segun se indique tanto al
inicio y al final del String.Recibe dos parametros,el primero debe ser un entero mayor al 
tamaño de la cadena y el segundo para agregar un contorno lo cual debe ser un caracter

Metodo ljust():

Permite alinear un String a la izquierda añadiendo espacios o caracteres segun se indique al final del
String.

Metodo rjust():

Permite alinear un String a la derecha añadiendo espacios o caracteres segun se indique al final del
String.

"""

#Ejemplo center():

titulo="Cien años de soledad"
print(titulo.center(40,"-"))

#Ejemplo Ijust():

autor="Gabriel Garcia Marquez"
print(autor.ljust(40,"."))

#Ejemplo rjust():

year="1967"
print(year.rjust(40,"."))
