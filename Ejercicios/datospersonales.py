# PRINT AND INPUT

Nombre = input("Cual es tu Nombre: ")
Apellido = input("Cual es tu Apellido: ")

print("Tu nombre es: " + Nombre + " " + Apellido)


# Calcular el indice de masa corporal
# Formula para calacular el IMC = (kilogramos) ÷ (metros cuadrados)

print(Nombre + " " + "Calculemos tu IMC: ")

# IMC = (kilogramos) ÷ (metros cuadrados)
# Cambiamos las variables de strings a numericas para poder realizar el calculo del IMC


Estatura = float(input("Cual es tu estatura: "))

Peso = int(input("Cual es tu peso en kg: "))

# Utilizamos  " round " para redondear la cantidad de decimales del resultado

print(f"Tu IMC es: {round(Peso/Estatura**2 , 2)} ")
