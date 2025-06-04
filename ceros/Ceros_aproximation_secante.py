import numpy as np
import matplotlib.pyplot as plt

def secante(x0, x1, f, tol=1e-6):
  its = 0
  error = 1
  while error > tol:
    x2 = x1 - (f(x1) * (x0 - x1))/(f(x0) - f(x1))
    error = abs(x2 - x1)
    if(its == 2):
      x_2 = x1
    x0 = x1
    x1 = x2
    print(x0, its)
    its += 1
  print(error)
  return x2, its, x_2
"""
r = 1
V = 0.75
f = lambda h: (np.pi * h**2 *(3*r-h))/3 - V

c, i = secante(1, 2, f)
print(c, f(c))
"""
r = 2
l = 7
v = 8.5

f = lambda h: (r**2 * np.arccos((r-h)/r) - (r - h * np.sqrt(2*r*h - h**2))) * l - v

raiz, its, x_2= secante(1, 1.2, f)

print(f"x2 = {x_2}")
print(f"Raiz = {raiz}")
