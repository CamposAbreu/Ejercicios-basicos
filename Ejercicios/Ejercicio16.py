"""Solicitar un nombre y edad de una persona, si la edad es mayor de 18 
años mostrar un mensaje eres adulto, de lo contrario mostrar el mensaje 
eres joven."""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad >= 18 :
  print(nombre, "eres adulto")
else:
  print(nombre, "eres joven")
  