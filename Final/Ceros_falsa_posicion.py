import numpy as np
import matplotlib.pyplot as plt


u = 2000
m0 = 150000
q = 2700
g = 9.81

f = lambda t: u * np.log(m0 / (m0 - q * t)) - g * t - 700

aproximaciones = np.linspace(10, 50, 500)
valores = []

def FalsaPosicion(f, a, b, error):
    if f(a) * f(b) > 0:
        print("No se garantiza el teorema de Bolzano")
        return
    else:
        p = b - f(b) * ((a - b) / (f(a) - f(b)))
        while abs(f(p)) > error:
            p = b - f(b) * ((a - b) / (f(a) - f(b)))
            valores.append(p)

            if f(a) * f(p) > 0:
                a = p
            else:
                b = p
        print(f"Iteraciones: {len(valores)}")
        print(f"f(p) ≈ {f(p)}")
        return p

raiz = FalsaPosicion(f, 10, 50, 1e-5)
print(f"Raíz aproximada (t*): {raiz:.5f} segundos")

