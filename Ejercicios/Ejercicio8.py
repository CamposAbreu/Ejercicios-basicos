"""" Dados dos números enteros calcular el cociente y 
el resto de su división entera"""

# Variables de Entrada

n1 = int(input("ingrese el primer numero: "))
n2 = int(input("ingrese el segundo numero: "))

# Proceso

c = n1 / n2
r = n1 % n2

# Resultado

print("El cociente es: " + str(int(c)))
print("El resto es: " + str(int(r)))

# Segundo algoritmo


def cociente_resto(dividendo, divisor):
    dividendo = int(input("ingrese el primer numero: "))
    divisor = int(input("ingrese el segundo numero: "))
    print("El cociente es: ", dividendo / divisor)
    print("El resto es: ", dividendo % divisor)
