import numpy as np
import matplotlib.pyplot as plt

f = lambda  x: x**10 - 1
aproximaciones  = np.linspace(0, 1.5, 100)
plt.plot(aproximaciones, f(aproximaciones), 'b' )
plt.axhline(0, color = 'red', linewidth = 1, linestyle = 'dashed')
valores = []

def FalsaPosicion(f, a,b, error):
    if f(a)*f(b) > 0:
        print("No se garantiza el teorema de Bolzano")
        return
    else:
        p = b - f(b) * ((a - b) / (f(a) - f(b)))
        while abs(f(p)) > error:
            p = b - f(b)*((a-b)/(f(a)- f(b)))
            valores.append(p)

            if (f(a)*f(p) > 0):
                a = p
            else:
                b = p
        print(f"Iteraciones: {len(valores)}")
        return p

print(f"Raíz aproximada: {FalsaPosicion(f, 0, 1.5, 1e-5)}")

plt.grid()
plt.show()
