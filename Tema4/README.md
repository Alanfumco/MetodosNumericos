# Tema 4: Diferenciación e Integración Numérica

## Introducción

La integración numérica es una técnica utilizada para aproximar el área bajo una curva cuando una integral es difícil o imposible de resolver de manera analítica. Estos métodos permiten obtener soluciones aproximadas mediante operaciones matemáticas simples aplicadas en intervalos pequeños.

Por otro lado, la diferenciación numérica se utiliza para aproximar derivadas usando valores discretos de una función.

Los métodos numéricos de integración trabajan dividiendo un intervalo en segmentos y aproximando la función mediante líneas rectas o polinomios.

---

# Métodos Principales

## Regla del Trapecio

Aproxima el área bajo la curva utilizando un trapecio entre dos puntos.

## Método de los Tres Puntos

Se utiliza principalmente para aproximar derivadas mediante diferencias finitas utilizando tres valores consecutivos.

## Simpson 1/3

Aproxima la función mediante una parábola utilizando tres puntos igualmente espaciados.

## Simpson 3/8

Utiliza cuatro puntos y una aproximación cúbica para estimar el área bajo la curva.

---

# Fórmulas Utilizadas

## Regla del Trapecio

```text id="pyjlwm"
I = (b - a) * [ f(a) + f(b) ] / 2
```

## Método de los Tres Puntos

```text id="r5xj4w"
f'(x) = [ f(x+h) - f(x-h) ] / (2h)
```

## Simpson 1/3

```text id="6qstwr"
I = (h / 3) * [ f(x0) + 4f(x1) + f(x2) ]
```

## Simpson 3/8

```text id="avh2do"
I = (3h / 8) * [ f(x0) + 3f(x1) + 3f(x2) + f(x3) ]
```

---

# Algoritmo y Pseudocódigo (Regla del Trapecio)

## Algoritmo

1. Definir la función y el intervalo `[a,b]`.
2. Evaluar la función en los extremos.
3. Aplicar la fórmula del trapecio.
4. Mostrar el área aproximada.

## Pseudocódigo

```text id="ewx5lh"
INICIO Trapecio(f, a, b)

  I <- (b - a) * ( f(a) + f(b) ) / 2

  ESCRIBIR I

FIN
```

---

# Algoritmo y Pseudocódigo (Método de los Tres Puntos)

## Algoritmo

1. Seleccionar el punto donde se desea calcular la derivada.
2. Definir el valor de incremento `h`.
3. Evaluar la función en `x+h` y `x-h`.
4. Aplicar la fórmula de diferencias centrales.
5. Mostrar el valor aproximado de la derivada.

## Pseudocódigo

```text id="sw29b2"
INICIO TresPuntos(f, x, h)

  derivada <- ( f(x+h) - f(x-h) ) / (2*h)

  ESCRIBIR derivada

FIN
```

---

# Algoritmo y Pseudocódigo (Simpson 1/3)

## Algoritmo

1. Definir la función y el intervalo `[a,b]`.
2. Calcular el punto medio del intervalo.
3. Evaluar la función en los extremos y en el punto medio.
4. Aplicar los factores de ponderación.
5. Obtener la aproximación del área.

## Pseudocódigo

```text id="r89yb5"
INICIO Simpson13(f, a, b)

  m <- (a + b) / 2

  I <- ((b - a) / 6) * ( f(a) + 4*f(m) + f(b) )

  ESCRIBIR I

FIN
```

---

# Algoritmo y Pseudocódigo (Simpson 3/8)

## Algoritmo

1. Dividir el intervalo en tres segmentos iguales.
2. Calcular los puntos intermedios.
3. Evaluar la función en cada punto.
4. Aplicar la fórmula de Simpson 3/8.
5. Mostrar el resultado de la integral aproximada.

## Pseudocódigo

```text id="u7q5pe"
INICIO Simpson38(f, a, b)

  h <- (b - a) / 3

  x1 <- a + h
  x2 <- a + 2*h

  I <- (3*h / 8) * ( f(a) + 3*f(x1) + 3*f(x2) + f(b) )

  ESCRIBIR I

FIN
```

---

# Aplicaciones de la Integración Numérica

Estos métodos son utilizados en:

* cálculo de áreas,
* simulaciones físicas,
* análisis estadístico,
* ingeniería,
* procesamiento de señales,
* y modelos matemáticos complejos.

---

# Implementaciones y Códigos

Si deseas visualizar los programas y ejemplos utilizados en este tema, puedes acceder a la carpeta correspondiente.

👉 [Ver codigos del Tema 4](./Tema_4)
