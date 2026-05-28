# Método de Newton-Raphson — Ejemplo 3

def f(x):
    return x**3 - 4*x + 1

def df(x):
    return 3*x**2 - 4

x = 1
tol = 0.0001

while abs(f(x)) > tol:

    x = x - f(x) / df(x)

print("Raiz aproximada:", x)