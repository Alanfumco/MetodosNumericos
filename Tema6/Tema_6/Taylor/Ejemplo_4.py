def taylor(x0, y0, h):

    y_prima = y0 - x0**2

    y_segunda = y_prima - 2*x0

    y = y0 + h*y_prima + ((h**2)/2)*y_segunda

    print("Resultado:", round(y,6))


taylor(0,1,0.1)
