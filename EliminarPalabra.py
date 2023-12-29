""""
Dada una cadena de caracteres escrita desde teclado,eliminar un subtring o parte de esa cadena segun la palabra que digite 
el usuario.

Metodo find():

Devuelve el indice en donde empieza una palabra dentro de una cadena

"""

cad=input("Digite una cadena: ")

cad1=input("Digite la frase a eliminar: ")

sub=""

indice=cad.find(cad1) #Indica en donde empieza la palabra a eliminar
sub=cad [0:indice] + cad[indice+len(cad1)+1:]


print(sub)


