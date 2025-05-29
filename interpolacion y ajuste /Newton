import numpy as np

def diferencias_divididas(x, y):
    n = len(x)
    coef = np.copy(y).astype(float)
    for j in range(1, n):
        coef[j:n] = (coef[j:n] - coef[j - 1:n - 1]) / (x[j:n] - x[0:n - j])
    return coef

def newton_interpolacion(x_data, y_data, x_eval):
    coef = diferencias_divididas(x_data, y_data)
    n = len(coef)
    p = coef[n - 1]
    for k in range(1, n):
        p = coef[n - 1 - k] + (x_eval - x_data[n - 1 - k]) * p
    return p

# Ejemplo de uso
x = np.array([1, 2, 4], dtype=float)
y = np.array([1, 4, 16], dtype=float)

x_interp = 3  # Punto en el que quieres interpolar
resultado = newton_interpolacion(x, y, x_interp)

print(f"El valor interpolado en x = {x_interp} es {resultado}")
