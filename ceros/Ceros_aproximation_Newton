import sympy as sp

def Newton(f, x0, tol=1e-4):
  error = tol + 1
  its = 0
  while error > tol:
    raiz = x0 - (f.evalf(subs={x:x0})/sp.diff(f, x).evalf(subs={x:x0}))
    error = abs(raiz - x0)
    if(its==2):
      x2 = x0
    x0 = raiz
    its += 1
  return raiz, its, x2

x = sp.symbols("x")
f = x**2 - 6

#Newton(f, 1)
f = x**4 - 95*x**2 + 2250
raiz, its, x2 = Newton(f, 9, 1e-6)
print(f"x_2 = {x2}")
print(f"P(x_2) = {f.evalf(subs={x:x2})})")

f = 4*x**3 - 190*x
print(f"P'(x_2) = {f.evalf(subs={x:x2})})")

print(f"raiz = {raiz}")
