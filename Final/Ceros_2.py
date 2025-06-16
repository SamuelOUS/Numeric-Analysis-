import numpy as np


f = lambda x: x * np.cos(x) - np.sin(x)
df = lambda x: -x * np.sin(x)

def newton(f, df, x0, tol=1e-5):
    error = tol + 1
    iteraciones = 0
    while error > tol:
        x1 = x0 - f(x0) / df(x0)
        error = abs(x1 - x0)
        x0 = x1
        iteraciones += 1
    return x0, iteraciones


raiz, its = newton(f, df, 2.0)

print(f"Raíz aproximada (x*): {np.format_float_positional(raiz, precision=7, unique=False, fractional=False)}")
print(f"Iteraciones: {its}")
