filas = int(input("Ingresa el número de filas: "))
columnas = int(input("Ingresa el número de columnas: "))

matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        numero = int(input(f"Ingrese el número en la posición [{i}][{j}]: "))
        fila.append(numero)
    matriz.append(fila)

print("La matriz generada es:")
for fila in matriz:
    print(fila)