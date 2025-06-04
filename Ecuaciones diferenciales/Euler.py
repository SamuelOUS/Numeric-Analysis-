def euler(f, a, b, h, y0):
    ys = [y0]
    ts = [a]
    n = int((b - a) / h)
    for i in range(n):
        t = a + i * h
        y = ys[i] + h * f(t, ys[i])
        ys.append(y)
        ts.append(t + h)
    return ts, ys
