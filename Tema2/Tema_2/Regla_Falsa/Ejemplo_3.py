# Método de la Secante — Ejemplo 3
def f(x):
    return x**3 - 4*x + 1

x0 = 0
x1 = 1
tol = 0.0001

while abs(x1 - x0) > tol:

    x2 = x1 - (f(x1) * (x0 - x1)) / (f(x0) - f(x1))

    x0 = x1
    x1 = x2

print("Raiz aproximada:", x2)