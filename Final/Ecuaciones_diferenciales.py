import numpy as np
import matplotlib.pyplot as plt


m = 20
k = 20
c = 2 * np.sqrt(k * m)
h = 0.001
a = 0
b = 15

def f(t, y):
    x = y[0]
    v = y[1]
    dxdt = v
    dvdt = -(c/m)*v - (k/m)*x
    return np.array([dxdt, dvdt])

# Método de Runge-Kutta 4
def RK4(f, a, b, h, y0):
    n = int((b - a) / h)
    t_values = np.linspace(a, b, n+1)
    y_values = [y0]

    for i in range(n):
        t = t_values[i]
        y = y_values[-1]
        k1 = h * f(t, y)
        k2 = h * f(t + h/2, y + k1/2)
        k3 = h * f(t + h/2, y + k2/2)
        k4 = h * f(t + h, y + k3)
        y_next = y + (k1 + 2*k2 + 2*k3 + k4)/6
        y_values.append(y_next)

    return t_values, np.array(y_values)

# Condición inicial: x=1, v=0
y0 = np.array([1, 0])
t, y = RK4(f, a, b, h, y0)

print(y)

