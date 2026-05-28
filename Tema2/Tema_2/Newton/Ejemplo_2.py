# Método de Newton-Raphson — Ejemplo 2
def f(x):
    return x**2 - 9

def df(x):
    return 2*x

x = 5
tol = 0.0001

while abs(f(x)) > tol:

    x = x - f(x) / df(x)

print("Raiz aproximada:", x)
