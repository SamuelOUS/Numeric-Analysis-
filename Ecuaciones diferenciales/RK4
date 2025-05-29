def rk4(f, a, b, h, y0):
    ys = [y0]
    ts = [a]
    n = int((b - a) / h)
    for i in range(n):
        t = a + i * h
        y = ys[i]
        k1 = h * f(t, y)
        k2 = h * f(t + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(t + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(t + h, y + k3)
        ys.append(y + (1/6) * (k1 + 2 * k2 + 2 * k3 + k4))
        ts.append(t + h)
    return ts, ys
