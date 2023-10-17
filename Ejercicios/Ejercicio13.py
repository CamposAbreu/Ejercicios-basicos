''' Para calcular el volumen de un cilindro se emplean las 
siguientes formulas : volumen=Ab*h, también se puede 
calcular volumen=pi +r2 * h. Elaborar un algoritmo que 
calcule el volumen.'''

from math import pi

pi = round( pi,  4)
h = float(input("ingrese un valor para la altura: "))
r = float(input("ingrese un valor para el radio: "))
r = (r**2)

print(pi * r * h)


# Calculemos el area del cilindro A = Pi * r2

A = (pi * r)
print("El area del cilindro es: ", A)

V = (A * h)
print("El volumen del cilindro es: ", V)
