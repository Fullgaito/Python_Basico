"""

Sentencia Break:

Sirve para deterner el flujo de un ciclo cuando se cumpla una condicion

Sentencia Continue:

Permite detener la iteraccion actual y volver al principio del bucle para realizar
una nueva iteraccion si la condicion del bucle se sigue cumpliendo

"""
#Ejemplo break

print("while con break")
print()

contador=0
while contador<10:
    contador+=2
    if contador==5:
        print("Se acabo")
        break
    else:
        print("Exito")
        break

#Ejemplo Continue

print("While con continue no mostrar impares ni el numero 2")
print()

conta=0

while conta<10:
    conta+=1
    if conta%2==0:
        if conta==2:
            continue
        print(conta)
    else:
        continue
