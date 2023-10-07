"""" Dados tres números A, B y C, calcular las soluciones de la ecuación 
Ax2+Bx+C=0."""

# libreria para trabajar con raiz cuadrada
import math


# Variables

a = int(input("ingrese el valor de a: "))
b = int(input("ingrese el valor de b: "))
c = int(input("ingrese el valor de c: "))

# Identificar las variables en la ecuacion Ax2+Bx+C=0
# Sustituir los valores en la siguiente formula x=(-b+-sqrtb**-4*a*c)(2*a)

# Calculamos el discriminante de la ecuacion

d = (b**2)-4*a*c

# Comprobamos y calculamos mediante un condicional

if d < 0:
    print("No existen soluciones reales")

else:
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)

    print("Solucion x1: ", (x1))
    print("Solucion x2: ", (x2))
