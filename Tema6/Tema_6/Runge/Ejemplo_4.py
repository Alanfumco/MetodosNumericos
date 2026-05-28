def runge_kutta(f, x0, y0, h, n):

    x = x0
    y = y0

    for i in range(n):

        k1 = h * f(x, y)

        k2 = h * f(x + h/2, y + k1/2)

        k3 = h * f(x + h/2, y + k2/2)

        k4 = h * f(x + h, y + k3)

        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6

        x = x + h

        print("Iteracion:", i+1)
        print("x =", round(x,4))
        print("y =", round(y,6))
        print("----------------")

runge_kutta(
    lambda x,y: y - x**2,
    0,
    1,
    0.1,
    1
)