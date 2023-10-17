"""La estructura de un algoritmo de decisión es útil para programar una serie de instrucciones
que se ejecutan en función de una condición. En pseudocódigo, la estructura de un algoritmo de
decisión se escribe como sigue:"""

"""Si (condición) entonces
    instrucción 1
    instrucción 2
    ...
Sino
    instrucción 3
    instrucción 4
    ...
Fin Si"""

"""Donde condición es la expresión lógica que se evalúa y determina si se ejecutan las
instrucciones dentro del bloque entonces o las instrucciones dentro del bloque sino.
Si la condición es verdadera, se ejecutan las instrucciones dentro del bloque entonces. 
Si la condición es falsa, se ejecutan las instrucciones dentro del bloque sino.

Por ejemplo, si queremos programar un algoritmo que determine si un número es par o impar, 
podemos utilizar la estructura de decisión como sigue:"""

"""Leer número
Si (número % 2 == 0) entonces
    Escribir "El número es par"
Sino
    Escribir "El número es impar"
Fin Si"""

"""En este caso, la condición es (número % 2 == 0), que evalúa si el residuo de la división
del número entre 2 es igual a cero. Si la condición es verdadera, se ejecuta la instrucción
Escribir "El número es par". Si la condición es falsa, se ejecuta la instrucción Escribir 
"El número es impar"."""
