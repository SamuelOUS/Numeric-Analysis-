import sympy as sp

x = sp.symbols('x')

def Lagrange(x_data, y_data):
    P = 0
    n = len(x_data)
    for i in range (n):
        Li = 1
        for j in range(n):
            if j != i:
                Li *= (x-x_data[j]) / (x_data[i] - x_data[j])
        P += Li * y_data[i]
    return sp.expand(P)
