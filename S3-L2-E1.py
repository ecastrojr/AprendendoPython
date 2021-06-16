x1=int(input("Entre com o valor x do primeiro ponto: "))
y1=int(input("Entre com o valor y do primeiro ponto: "))
x2=int(input("Entre com o valor x do segundo ponto: "))
y2=int(input("Entre com o valor y do segundo ponto: "))

import math

d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
print(d)
if d >= 10:
    print("longe")

else:
    print("perto")