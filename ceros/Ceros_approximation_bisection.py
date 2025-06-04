import numpy as np
import matplotlib.pyplot as plt

g = 32.17
t = 1
x = 1.7

# Definir la función
f = lambda w: -g/(2*w**2)*((np.exp(w*t) - np.exp(-w*t)) / 2 - np.sin(w*t)) - x

# Intervalo de búsqueda
aproximaciones = np.linspace(-3, -0.001, 100)
plt.plot(aproximaciones, f(aproximaciones), 'b', label="f(w)")
plt.axhline(0, color='red', linewidth=1, linestyle='dashed')

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
        print(f"f(p) ≈ {f(p)}")
        return p

# Ejecutar el método
raiz = AproximacionACero(f, -1, -0.001, 1e-5)
print(f"Raíz aproximada: {raiz}")

# Mostrar gráfico
plt.grid()
plt.title("Método de Bisección aplicado a f(w)")
plt.xlabel("w")
plt.ylabel("f(w)")
plt.legend()
plt.show()
