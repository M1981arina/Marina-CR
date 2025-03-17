def ordenar_fila(matriz, fila):
    matriz[fila] = sorted(matriz[fila])  # Ordena la fila seleccionada

# Definir la matriz 3x3
matriz = [
    [12, 5, 8],
    [9, 3, 1],
    [4, 7, 2]
]

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Elegir la fila a ordenar (0, 1 o 2)
fila_a_ordenar = int(input("Ingresa el índice de la fila que deseas ordenar (0-2): "))

# Ordenar la fila
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)