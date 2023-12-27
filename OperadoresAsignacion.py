# operadores de asignacion
"""
igual =  Ejemplo:  x=12
suma o acumulacion  +=  Ejemplo x+=1  o x=x+1
resta -=  Ejemplo  x-=1
multiplicacion *= Ejemplo x*=2
division /= Ejemplo x/=2
division entera //=  Ejemplo x//=10

"""
x=0

for i in range (1,11,1):
    x+=i
    print(x)
    if i==10:
        print(f"El resultado final es:{x}")
  