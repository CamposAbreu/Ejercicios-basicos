""" El precio de un producto es a 5.6 dólares sin se compran mas de 10 
unidades, de lo contrario es 7 dólares, elaborar un algoritmo que solicite la 
cantidad de producto y calcule el valor a pagar según la restricción 
indicada."""

producto = int(input("ingrese la cantidad de productos: "))
precio1 = float(5.6)
precio2 = float(7)

if producto > 10:
  print(f"El valor a pagar es", {producto * precio1})
else:
  print(f"El precio a pagar es ", {producto * precio2})
  
  

    