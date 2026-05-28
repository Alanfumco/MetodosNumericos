# Método de Newton-Raphson — Ejemplo 1
def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

x = 1.5
tol = 0.0001

while abs(f(x)) > tol:

    x = x - f(x) / df(x)

print("Raiz aproximada:", x)
