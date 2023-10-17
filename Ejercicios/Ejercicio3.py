
"""Para calcular el promedio de tres notas se suman las notas y 
se dividen por 3, elabora un algoritmo para realizar el calculo"""

# Paso 1
# Ingresar programa para N cantidad de notas a utilizar

n = int(input("Ingrese la cantidad de notas a promediar: "))


# Paso 2
# Crear las Variables del enunciado

suma = 0
i = 1

# Paso 3
# Utilizamos un ciclo while para solicitar las notas y sumarlas con la Variable suma

while (i <= n):
    print("Ingrese la nota numero: ", i)  # Solicitamos las notas
    # Usamos float para que lea numeros con o sin decimales
    nota = float(input())
    suma = suma+nota  # Permite guardar las notas sin sobreescribir
    i += 1  # Incrmentar la variable i hasta que ya no se cumpla la condicion y finalice el ciclo while
prom = suma / n
if prom >= 5:  # condicional if / else para aprobado o reprobado
    print("Aprobado")
else:
    print("Reprobado")
