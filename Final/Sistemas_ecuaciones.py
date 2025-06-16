import numpy as np
import time

# Sistema del ejercicio
A = np.array([
    [10, 2, -1],
    [-3, -6, 2],
    [1, 1, 5]
], dtype=float)

b = np.array([27, -61.5, -21.3], dtype=float)

def gauss_seidel(A, b, x0=None, max_its=50, tol=1e-6):
    D = np.diag(np.diag(A))
    L = D - np.tril(A)
    U = D - np.triu(A)

    Tg = np.dot(np.linalg.inv(D - L), U)
    Cg = np.dot(np.linalg.inv(D - L), b)

    if x0 is None:
        x0 = np.zeros(len(b))

    v_propios, vec_propios = np.linalg.eig(Tg)
    radio = max(abs(v_propios))

    if radio < 1:
        start = time.time()
        error = 1
        k = 0
        while k < max_its and error > tol:
            x1 = np.dot(Tg, x0) + Cg
            error = np.max(np.abs(x1 - x0))
            k += 1
            x0 = np.copy(x1)
            print(x1)

        end = time.time()
        print(f"Execution time: {end - start:.4f}s, {k} iterations")
        return x1
    else:
        print("No converge con el metodo de Gauss Seidel")

# Condición inicial
x0 = np.array([1, 0, 1], dtype=float)

# Ejecutar el método
print(f"Solución final = {gauss_seidel(A, b, x0)}")
