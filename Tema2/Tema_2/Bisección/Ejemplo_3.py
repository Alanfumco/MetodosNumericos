
def f(x):
    return x**3 - 4*x + 1

a = 0
b = 1
tol = 0.0001

while (b - a) / 2 > tol:

    xr = (a + b) / 2

    if f(a) * f(xr) < 0:
        b = xr
    else:
        a = xr

print("Raiz aproximada:", xr)

