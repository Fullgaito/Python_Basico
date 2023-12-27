nombre=input("Digita tu nombre: ")
clave=int(input("Ingrese la clave: "))
year=float(input("Ingrese los años que lleva: "))

if clave==1:
    if year==1 and year<2:
        print("6 dias de vacaciones")
    elif year>=2 and year<7:
        print("14 dias de vacaciones")
    elif year>=7:
        print("20 dias de vacaciones")
    else:
        print("Sin derecho a vacaciones")
elif clave==2:
    if year==1 and year<2:
        print("7 dias de vacaciones")
    elif year>=2 and year<7:
        print("15 dias de vacaciones")
    elif year>=7:
        print("22 dias de vacaciones")
    else:
        print("Sin derecho a vacaciones")
elif clave==3:
    if year==1 and year<2:
        print("10 dias de vacaciones")
    elif year>=2 and year<7:
        print("20 dias de vacaciones")
    elif year>=7:
        print("30 dias de vacaciones")
    else:
        print("Sin derecho a vacaciones")
else:
    print("La clave no existe")