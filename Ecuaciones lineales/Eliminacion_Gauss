def gauss_eliminacion(A, b):
    n = len(b)

    # Construimos la matriz aumentada
    M = [A[i] + [b[i]] for i in range(n)]

    # Eliminación hacia adelante
    for i in range(n):
        # Verificamos que el pivote no sea cero
        if M[i][i] == 0:
            raise ValueError("Pivote cero: se necesita pivoteo parcial")

        for j in range(i + 1, n):
            factor = M[j][i] / M[i][i]
            for k in range(i, n + 1):
                M[j][k] -= factor * M[i][k]

    # Sustitución regresiva
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        suma = sum(M[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (M[i][n] - suma) / M[i][i]

    return x


# Ejemplo de uso:
A = [
    [0.003000, 59.14],
    [5.291, -6.130]

]
b = [59.17,46.78]

solucion = gauss_eliminacion(A, b)
print("Solución:", solucion)
