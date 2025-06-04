import numpy as np
import time

def jacobi_matrices(A, b, x0=None, max_its=50, tol=1e-6):
    D = np.diag(np.diag(A))
    L = np.tril(A, -1)
    U = np.triu(A, 1)

    Tj = np.linalg.inv(D) @ (L + U)
    Cj = np.linalg.inv(D) @ b

    if x0 is None:
        x0 = np.zeros(len(b))
        
    res = [np.copy(x0)]
    v_propios, _ = np.linalg.eig(Tj)
    radio = max(abs(v_propios))

    if radio < 1:
        start = time.time()
        error = 1
        k = 0
        while k < max_its and error > tol:
            x1 = Tj @ x0 + Cj
            error = np.max(np.abs(x1 - x0))
            x0 = np.copy(x1)
            res.append(x1)
            k += 1
        end = time.time()

        print(f"Tiempo de cómputo Jacobi Matrices: {end - start:.4f}s")
        return x1, res
    else:
        print("No converge con el método de Jacobi")
        return None, res
