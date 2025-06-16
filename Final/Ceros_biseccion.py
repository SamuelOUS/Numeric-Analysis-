import numpy as np
import matplotlib.pyplot as plt

u = 2000
m0 = 150000
q = 2700
g = 9.81

f = lambda t: u * np.log(m0 / (m0 - q * t)) - g * t - 700
aproximaciones = np.linspace(10, 50, 500)
valores = []

def AproximacionACero(f, a, b, error):
    if f(a)*f(b) > 0:
        print("No se garantiza el teorema de Bolzano")
        return None
    else:
        while abs(b - a) > error:
            p = (a + b) / 2
            valores.append(p)
            if f(a) * f(p) > 0:
                a = p
            else:
                b = p
        print(f"Iteraciones: {len(valores)}")
        return p

raiz = AproximacionACero(f, 10, 50, 1e-5)
print(f"Raíz aproximada (t*): {raiz:.5f} s")

