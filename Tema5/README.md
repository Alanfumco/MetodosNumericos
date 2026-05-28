# Tema 5: Interpolación y Ajuste de Funciones

## Introducción

La interpolación y el ajuste de funciones son técnicas utilizadas para representar el comportamiento de un conjunto de datos mediante ecuaciones matemáticas.

La interpolación busca construir una función que pase exactamente por los puntos conocidos, mientras que los métodos de ajuste permiten obtener una aproximación cuando los datos contienen errores o variaciones experimentales.

Estas herramientas son ampliamente utilizadas en análisis de datos, ingeniería, estadística y simulaciones matemáticas.

---

# Métodos Principales

## Interpolación Lineal

Permite estimar valores intermedios utilizando una línea recta entre dos puntos conocidos.

## Interpolación Cuadrática

Utiliza un polinomio de segundo grado para aproximar una función mediante tres puntos.

## Interpolación por Segmentos

Divide el intervalo en varias partes y aplica interpolación en cada segmento individualmente.

## Correlación

Mide el grado de relación existente entre dos variables.

## Regresión Lineal

Obtiene una recta que representa la tendencia general de un conjunto de datos.

---

# Fórmulas Utilizadas

## Interpolación Lineal

```text id="a4oz8f"
y = y0 + ((x - x0)(y1 - y0)) / (x1 - x0)
```

## Interpolación Cuadrática

```text id="w8b0zj"
P(x) = a0 + a1x + a2x²
```

## Interpolación por Segmentos

```text id="jjlwmf"
S(x) = Pi(x)   para cada intervalo
```

## Correlación

```text id="i1m7ef"
r = Σ[(xi - x̄)(yi - ȳ)] / √[Σ(xi - x̄)² Σ(yi - ȳ)²]
```

## Regresión Lineal

```text id="mjlwm9"
y = a0 + a1x
```

---

# Algoritmo y Pseudocódigo (Interpolación Lineal)

## Algoritmo

1. Seleccionar dos puntos conocidos.
2. Calcular la pendiente entre ambos puntos.
3. Sustituir el valor de `x` en la ecuación lineal.
4. Obtener el valor aproximado de `y`.

## Pseudocódigo

```text id="caxj9k"
INICIO InterpolacionLineal(x0, y0, x1, y1, x)

  y <- y0 + ((x - x0) * (y1 - y0)) / (x1 - x0)

  ESCRIBIR y

FIN
```

---

# Algoritmo y Pseudocódigo (Interpolación Cuadrática)

## Algoritmo

1. Seleccionar tres puntos conocidos.
2. Construir un polinomio cuadrático.
3. Calcular los coeficientes del polinomio.
4. Evaluar el valor deseado de la función.

## Pseudocódigo

```text id="r8ghq4"
INICIO InterpolacionCuadratica(a0, a1, a2, x)

  y <- a0 + a1*x + a2*x^2

  ESCRIBIR y

FIN
```

---

# Algoritmo y Pseudocódigo (Interpolación por Segmentos)

## Algoritmo

1. Dividir el conjunto de datos en intervalos.
2. Construir una función para cada segmento.
3. Seleccionar el intervalo correspondiente al valor buscado.
4. Evaluar la función del segmento.

## Pseudocódigo

```text id="u0ms3q"
INICIO InterpolacionSegmentos(x, intervalos)

  PARA cada intervalo HACER

      SI x pertenece al intervalo ENTONCES

          calcular S(x)

      FIN SI

  FIN PARA

  ESCRIBIR S(x)

FIN
```

---

# Algoritmo y Pseudocódigo (Correlación)

## Algoritmo

1. Calcular el promedio de los valores `x`.
2. Calcular el promedio de los valores `y`.
3. Obtener las diferencias respecto a los promedios.
4. Aplicar la fórmula del coeficiente de correlación.
5. Mostrar el grado de relación entre variables.

## Pseudocódigo

```text id="6lbx0g"
INICIO Correlacion(x, y)

  calcular promedio_x
  calcular promedio_y

  calcular numerador
  calcular denominador

  r <- numerador / denominador

  ESCRIBIR r

FIN
```

---

# Algoritmo y Pseudocódigo (Regresión Lineal)

## Algoritmo

1. Calcular las sumatorias necesarias.
2. Obtener la pendiente de la recta.
3. Calcular el intercepto.
4. Construir la ecuación de regresión.
5. Mostrar la función resultante.

## Pseudocódigo

```text id="h0q7tm"
INICIO RegresionLineal(x, y)

  calcular a1
  calcular a0

  y <- a0 + a1*x

  ESCRIBIR y

FIN
```

---

# Aplicaciones de la Interpolación y Regresión

Estos métodos son utilizados en:

* análisis estadístico,
* predicción de datos,
* simulaciones matemáticas,
* inteligencia artificial,
* modelado de funciones,
* y procesamiento de información experimental.

---

# Implementaciones y Códigos

Si deseas visualizar los programas y ejemplos utilizados en este tema, puedes acceder a la carpeta correspondiente.

👉 [Ver codigos del Tema 5](./Tema_5)
