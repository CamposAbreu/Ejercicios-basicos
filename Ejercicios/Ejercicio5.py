"""Elabora un algoritmo que solicite 3 números y les calcule
el porcentaje de 3%, 5% y 15% a cada numero"""


a = 3/100
b = 5/100
c = 15/100


n1 = float(input("ingrese el primer numero: "))
n2 = float(input("ingrese el segundo numero: "))
n3 = float(input("ingrese el tercer numero: "))


print(f"Tu porc es: {round(n1*a , 2)} {round(n1*b  ,2)} {round(n1*c  ,2)} ")
print(f"Tu porc es: {round(n2*a , 2)} {round(n2*b  ,2)} {round(n2*c  ,2)} ")
print(f"Tu porc es: {round(n3*a , 2)} {round(n3*b  ,2)} {round(n3*c  ,2)} ")
