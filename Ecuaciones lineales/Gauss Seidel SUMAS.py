import numpy as np
import time

def gauss_seidel_sumas(A, b, x0=None, max_its=50, tol=1e-6):
    n = len(b)
    if x0 is None:
        x0 = np.zeros(n)

    x = x0.copy()
    res = [np.copy(x)]
    start = time.time()

    for k in range(max_its):
        x_old = x.copy()

        for i in range(n):
            s1 = sum(A[i, j] * x[j] for j in range(i))         # usa nuevos valores
            s2 = sum(A[i, j] * x_old[j] for j in range(i+1, n)) # usa valores viejos
            x[i] = (b[i] - s1 - s2) / A[i, i]

        res.append(np.copy(x))
        error = np.max(np.abs(x - x_old))
        if error < tol:
            break

    end = time.time()
    print(f"Tiempo de computo Gauss-Seidel Sumas: {end - start:.4f}s")
    return x, res
