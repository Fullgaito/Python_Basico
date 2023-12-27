""""
Metodos strip(), rstrip(), lstrip()

Metodo strip():

Elimina caracteres especificados al inicio y al final de una cadena de caractere
sino se especifica elimina espacios en blanco y saltos de linea.

Metodo rstrip():

Se usa para eliminar unicamente caracteres especificados al final de una cadena
sino se especifica elimina espacios en blanco y saltos de linea.

Metodo lstrip():

Se usa para eliminar unicamente caracteres especificados al inicio de una cadena
sino se especifica caracteres a eliminar solo eliminara espacios en blanco y saltos de linea.

"""

#Ejemplo strip()

nombre=" Sergio "
print(nombre)
print(nombre.strip()) #Elimina los espacios al inicio y al final
print(nombre.strip(" oS")) #Elimina los caracteres del parametro si estos se encuentran al inicio y al final de la cadena

#Ejemplo rstrip()

cadena="Diciembre "
print(cadena)
print(cadena.rstrip()) #Elimina el espacio en blanco del final
print(cadena.rstrip(" erb")) #Elimina estos caracteres que verifica si se encuentran o no al final de la cadena

#Ejemplo lstrip()

caracter=" Universidad"
print(caracter)
print(caracter.lstrip()) #Elimina el espacio del inicio
print(caracter.lstrip(" Uni")) #Elimina los caracteres especificados si se encuentran al inicio de la cadena
