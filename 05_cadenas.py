"""
Metodos startswith(), endswith()

Metodo startswith():

Se utiliza para comprobar si una cadena de caracteres comienza con una subcadena en
particular,es posible establecer un rango inicial de busqueda.

Metodo endswith():

Se utiliza para comprobar si una cadena de caracteres termina con una subcadena en particular
es posible establecer un rango inicial de busqueda.

"""

#Ejemplo startswith():

cad="Colombia"
print(cad.startswith("Colo"))

#Ejemplo endswith():

mensaje="Error"
print(mensaje.endswith("rror",1,len(mensaje)))