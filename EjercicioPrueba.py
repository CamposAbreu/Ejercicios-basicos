

string = input("Ingrese una palabra: ")
palabra = input("Ingrese una palabra que desees eliminar: ")
substring = ""
indice = string.find(palabra)
substring = string[0 : indice] + string[indice + len(palabra) + 1 : ]

print(substring)

