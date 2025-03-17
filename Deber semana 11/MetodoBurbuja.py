def bubble_sort_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if matriz[fila][j] > matriz[fila][j + 1]:
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]

# Matriz 3x3
matriz = [
    [12, 5, 8],
    [9, 3, 1],
    [4, 7, 2]
]

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Pedir al usuario la fila a ordenar
fila_a_ordenar = int(input("Ingresa el índice de la fila que deseas ordenar (0-2): "))

# Aplicar Bubble Sort en la fila seleccionada
bubble_sort_fila(matriz, fila_a_ordenar)

# Mostrar la matriz después de ordenar la fila
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print (fila)
    print(f"\nCiudad: {ciudad}")