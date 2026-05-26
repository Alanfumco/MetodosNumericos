# Interpolación cuadrática de Lagrange

# Datos
x0, y0 = 20, 120
x1, y1 = 40, 95
x2, y2 = 60, 60

# Valor a evaluar
x = 50

# Polinomios de Lagrange
L0 = ((x - x1) * (x - x2)) / ((x0 - x1) * (x0 - x2))
L1 = ((x - x0) * (x - x2)) / ((x1 - x0) * (x1 - x2))
L2 = ((x - x0) * (x - x1)) / ((x2 - x0) * (x2 - x1))

# Interpolación
y = (y0 * L0) + (y1 * L1) + (y2 * L2)

# Mostrar resultados
print("L0 =", L0)
print("L1 =", L1)
print("L2 =", L2)

print("\nResultado de la interpolación:")
print("y(50) =", y)