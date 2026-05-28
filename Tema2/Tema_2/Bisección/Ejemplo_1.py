def f(x):
    return x**3 - x - 2

a = 1
b = 2
tol = 0.0001

while (b - a) / 2 > tol:

    xr = (a + b) / 2

    if f(a) * f(xr) < 0:
        b = xr
    else:
        a = xr

print("Raiz aproximada:", xr)