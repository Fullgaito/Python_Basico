"""
Es una estructura de datos que se utiliza para almacenar un conjunto de elementos
no ordenados.Se basa en la estructura clave-valor

"""

#Diccionario vacio
dictionary_empty={}
print(f"Diccionario vacio: {dictionary_empty}")

#Diccionario homogeneo

dictionary_ages={"Sebastian":24,"Luis":26,"Rodrigo":34}
print(f"Diccionario de edades: {dictionary_ages}")

#Diccionario heterogeneo

dictionary_dates={"name":"Margot","last name":"Robbie","age":33}
print(f"Diccionario de informacion de una persona: {dictionary_dates}")

#Diccionario con listas
dictionary_list={"a":{"a":1},"b":[0,1,2]}
print(f"Diccionario de listas y diccionario de diccionario: {dictionary_list}")

#Diccionario con clave numericas
meses={1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"Noviembre",12:"Diciembre"}
print(f"Diccionario de meses: {meses}")

#Un diccionario no puede tener claves repetidas
dictionary_repeated_keys={"Juan":20,"Eduardo":30,"Juan":22}  #Si hay claves repetidas muestra el ultimo en agregarse
print(f"Claves repetidas: {dictionary_repeated_keys}")

#Un diccionario puede tener claves numericas o de tipo texto
dictionary={1:23,"Juan":5,-2:"Hola"}
print(f"Diccionario con claves de distinto dato: {dictionary}")