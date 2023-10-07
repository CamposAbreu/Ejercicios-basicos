"""Se desea calculara el espacio recorrido por un cuerpo si viaja a una 
velocidad de 15 m/s durante 60 minutos"""

d = ()
v = 15
t = 60*60/1

print(f"Tu d es: {v*t}")

"""Modificar el algoritmo anterior para que solicite los datos de velocidad y 
tiempo"""

v = float(input("Cual es el valor de la velocidad?: "))
t = float(input("Cual es el valor del tiempo?: "))
t = t*60/1

d = float(v*t)
print("La distancia recorrida es: ", d)
