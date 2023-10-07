# Calcular el 5% de una cantidad de dinero que una persona tiene.

b = 5/100

n1 = float(input("ingrese el dinero que tiene: "))
print(f"Tu porc es: {round(n1*b , 2)}")


"""Se desea calcular cualquier porcentaje de interés para un valor de 
préstamo"""
prestamo = float(input("ingrese el monto de la cantidad: "))

porc = float(input("ingrese el porcentaje de interes: "))

print(f"El interes es: ", {round(prestamo*porc/100, 2)})
