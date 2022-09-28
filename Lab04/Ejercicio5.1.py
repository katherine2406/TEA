contador = 0 
suma = 0
while True:
    número = input("Ingrese un número: ")
    if (número == "salir"):
        break
    else:
        contador = contador + 1
        suma = suma + int(número)
        promedio = suma / contador
print("Contador;", contador)
print("Suma;", suma)

print("Promedio;", promedio)


