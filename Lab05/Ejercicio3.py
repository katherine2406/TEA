try:
    entrada = input("Ingresar el nombre del archivo: ")
    archivo = open(entrada, "r", encoding="UTF-8")
    for linea in archivo:
        print(linea.upper())
except:
    print("Error, archivo no existe")

