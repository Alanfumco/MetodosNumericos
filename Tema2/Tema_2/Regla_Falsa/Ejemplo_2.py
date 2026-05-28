# Método de la Secante — Ejemplo 2
def f(x):
    return x**2 - 9

x0 = 2
x1 = 5
tol = 0.0001

while abs(x1 - x0) > tol:

    x2 = x1 - (f(x1) * (x0 - x1)) / (f(x0) - f(x1))

    x0 = x1
    x1 = x2

print("Raiz aproximada:", x2)