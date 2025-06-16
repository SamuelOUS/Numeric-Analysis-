import sympy as sp

u = 2000
m0 = 150000
q = 2700
g = 9.81

t = sp.symbols('t')

f_sym = u * sp.ln(m0 / (m0 - q * t)) - g * t - 700
f_prime = sp.diff(f_sym, t)

def newton(f, f_prime, x0, tol=1e-5):
    iteraciones = 0
    error = tol + 1
    while error > tol:
        f_val = f.evalf(subs={t: x0})
        f_der = f_prime.evalf(subs={t: x0})
        x1 = x0 - f_val / f_der
        error = abs(x1 - x0)
        x0 = x1
        iteraciones += 1
    return x1, iteraciones

raiz_newton, iter_newton = newton(f_sym, f_prime, x0=20)
print(f"Newton-Raphson: t* ≈ {raiz_newton:.5f} s, Iteraciones = {iter_newton}")
