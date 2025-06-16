import numpy as np


f = lambda x: np.exp(-x) - np.log(x)

aproximaciones = np.linspace(1, 2, 500)
valores = []

def AproximacionACero(f, a, b, error):
    if f(a) * f(b) > 0:
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

raiz = AproximacionACero(f, 1, 2, 1e-5)
print(raiz)
