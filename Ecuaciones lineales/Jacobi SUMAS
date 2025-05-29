import numpy as np
import time

def jacobi_sumatorias(matrix, vector, x_0=None, max_it=50, tol=1e-6):
    if x_0 is None:
        x_0 = np.zeros(len(vector), dtype=float)
    
    res = [np.copy(x_0)]
    n = len(vector)
    x_sol = np.zeros(n, dtype=float)
    k = 0
    error = 1
    start = time.time()

    while k < max_it and error > tol:
        for i in range(n):
            summatory = 0
            for j in range(n):
                if i != j:
                    summatory += matrix[i][j] * x_0[j]
            x_sol[i] = (vector[i] - summatory) / matrix[i][i]

        res.append(np.copy(x_sol))  # se agrega al final de la iteración completa
        error = np.max(np.abs(x_sol - x_0))
        x_0 = np.copy(x_sol)
        k += 1

    end = time.time()
    print(f"Tiempo de computo Jacobi Sumas: {end - start:.5f}s")
    return x_sol, res
