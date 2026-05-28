def taylor(x0, y0, h):

    y_prima = x0 + 2*y0

    y_segunda = 1 + 2*y_prima

    y = y0 + h*y_prima + ((h**2)/2)*y_segunda

    print("Resultado:", round(y,6))


taylor(0,1,0.1)
