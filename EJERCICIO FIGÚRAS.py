from FIGURAS import *

p1 = PUNTO(5,5)
p2 = PUNTO(5,10)
Cuadrado = Cuadrado(p1, p2)
Circulo = Circulo(p1,p2)

Cuadrado.calcular_area()
Circulo.calcular_area()

print (Cuadrado.area)
print (Circulo.area)
