# Método de Bisección — Ejemplo 2
def f(x):
    return x**2 - 9

a = 2
b = 5
tol = 0.0001

while (b - a) / 2 > tol:

    xr = (a + b) / 2

    if f(a) * f(xr) < 0:
        b = xr
    else:
        a = xr

print("Raiz aproximada:", xr)
