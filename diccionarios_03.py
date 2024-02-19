#Modificar y agregar elementos de un diccionario

meses={1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"Noviembre",12:"Diciembre"}

meses[1]="enero" #modificacion
meses[13]="No existe" #insercion
print(meses)

#El metodo copy()
"Se utiliza para crear una copia de un objeto"
copia=meses.copy()
print(copia)

#El metodo fromkeys()
"Crea un nuevo diccionario con claves de una secuencia dada y valores previamente establecidos"
sequence=["uno","dos","tres"] #claves
value=[1,2,3] #valor asignado
dic=dict.fromkeys(sequence,value)
print(dic)

#El metodo get()
"Obtiene los valores que estan asociados a cada una de las claves de un diccionario"
personas={"Uva":1500,"Manzana":1200}
print(personas.get("Pera"))

#El metodo popitem()
"Se usa para eliminar y devolver el ultimo par clave-valor agregado a un diccionario"
eliminado=personas.popitem()
print(eliminado)
print(personas)