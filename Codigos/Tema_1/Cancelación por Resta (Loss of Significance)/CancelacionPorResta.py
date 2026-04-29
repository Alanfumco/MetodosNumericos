def main():
    # Dos números muy cercanos entre sí
    a = 1.000000
    b = 0.9999999999

    # Operación propensa a la cancelación
    resultado = a - b

    print("Valor de a:", a)
    print("Valor de b:", b)
    print("Resultado de (a - b):", resultado)

    # El resultado matemático exacto debería ser 1e-10

if __name__ == "__main__":
    main()