n=int(input("Digite el numero para hallar su tabla de multiplicar: "))
f=int(input("Digite hasta donde va la tabla de multiplicar: "))
for i in range(0,f+1,1):
    print(f"{n} X {i} = {n*i}")