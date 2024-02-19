#Acceder a los elementos de un diccionario
"Se hace por medio de la clave de cada uno de ellos"

meses={1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"Noviembre",12:"Diciembre"}
print(meses[2])
dictionary_list={"a":{"a":1},"b":[0,1,2]}
print(dictionary_list["a"]["a"])
print(dictionary_list["b"][2])

#El metodo items()
"Devuelve cada uno de los elementos del diccionario en forma de tupla"
print(list(meses.items()))

#El metodo keys()
"Se utiliza para obtener una lista de todas las claves del diccionario"
print(list(meses.keys()))

#El metodo values()
"Se utiliza para obtener una lista de todos los valores del diccionario"
print(list(meses.values()))

#El metodo clear()
"Se utiliza para eliminar los elementos de un diccionario,lista,etc.."

employees={"Juan":{"edad":23,"Salario":23000} ,"Javier":{"edad":64,"Salario":233000}}
print(f"El diccionario es:{employees}")
employees.clear()
print(employees)