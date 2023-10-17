""" Solicitar el usuario y contraseña de una persona si el usuario es “Lucas” y la 
contraseña “abc123” presentar un mensaje de bienvenida al sistema, de 
lo contrario mostrar un mensaje de que hay un error en el usuario o la 
contraseña"""

usuario = input("ingrese su nombre de usuario: ")
contraseña = input("ingrese su contraseña: ")

if usuario =="Lucas" and contraseña == "abc123":
  print("bienvenido al sistema.")
else:
  print("hay un error en el usuario o la contraseña.")
    