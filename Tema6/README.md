# Tema 6: Solución Numérica de Ecuaciones Diferenciales

## Introducción

Las ecuaciones diferenciales se utilizan para modelar fenómenos que cambian continuamente, como el movimiento de objetos, crecimiento poblacional, circuitos eléctricos y procesos físicos.

En muchos casos, obtener una solución exacta resulta complicado, por lo que se emplean métodos numéricos para aproximar los valores de la solución en diferentes puntos.

Estos métodos trabajan mediante iteraciones sucesivas utilizando información previa para calcular aproximaciones cada vez más precisas.

---

# Métodos Principales

## Método de Euler

Es uno de los métodos más simples para aproximar soluciones de ecuaciones diferenciales ordinarias utilizando pendientes.

## Método de Runge-Kutta

Mejora la precisión del método de Euler calculando varias pendientes intermedias en cada iteración.

## Series de Taylor

Aproxima funciones mediante polinomios construidos a partir de derivadas sucesivas.

---

# Fórmulas Utilizadas

## Método de Euler

```text id="3lvjlwm"
y(i+1) = yi + h * f(xi, yi)
```

## Método de Runge-Kutta de 4to Orden

```text id="lq9m0v"
y(i+1) = yi + (1/6)(k1 + 2k2 + 2k3 + k4)
```

## Serie de Taylor

```text id="4vtx8g"
f(x) = f(a) + f'(a)(x-a) + f''(a)(x-a)^2 / 2!
```

---

# Algoritmo y Pseudocódigo (Método de Euler)

## Algoritmo

1. Definir la ecuación diferencial y la condición inicial.
2. Seleccionar el tamaño del paso `h`.
3. Calcular la pendiente utilizando la función.
4. Obtener el nuevo valor aproximado.
5. Repetir el procedimiento hasta alcanzar el intervalo deseado.

## Pseudocódigo

```text id="c9s4wt"
INICIO Euler(f, x0, y0, h, n)

  x <- x0
  y <- y0

  PARA i <- 1 HASTA n HACER

      y <- y + h * f(x, y)

      x <- x + h

      ESCRIBIR x, y

  FIN PARA

FIN
```

---

# Algoritmo y Pseudocódigo (Método de Runge-Kutta)

## Algoritmo

1. Definir la ecuación diferencial.
2. Calcular cuatro pendientes aproximadas.
3. Obtener un promedio ponderado de las pendientes.
4. Actualizar el valor de la solución.
5. Repetir el proceso para cada iteración.

## Pseudocódigo

```text id="tw0n6r"
INICIO RungeKutta(f, x0, y0, h, n)

  x <- x0
  y <- y0

  PARA i <- 1 HASTA n HACER

      k1 <- h * f(x, y)

      k2 <- h * f(x + h/2, y + k1/2)

      k3 <- h * f(x + h/2, y + k2/2)

      k4 <- h * f(x + h, y + k3)

      y <- y + (k1 + 2*k2 + 2*k3 + k4) / 6

      x <- x + h

      ESCRIBIR x, y

  FIN PARA

FIN
```

---

# Algoritmo y Pseudocódigo (Series de Taylor)

## Algoritmo

1. Seleccionar el punto de expansión.
2. Calcular derivadas sucesivas de la función.
3. Construir el polinomio de Taylor.
4. Evaluar el polinomio para aproximar la función.

## Pseudocódigo

```text id="9h7m1x"
INICIO Taylor(f, x, a)

  calcular f(a)

  calcular derivadas sucesivas

  aproximacion <- f(a) + f'(a)*(x-a)

  ESCRIBIR aproximacion

FIN
```

---

# Aplicaciones de las Ecuaciones Diferenciales

Estos métodos son utilizados en:

* simulaciones físicas,
* ingeniería,
* modelado matemático,
* dinámica de sistemas,
* inteligencia artificial,
* y análisis científico.

---

# Implementaciones y Códigos

Si deseas visualizar los programas y ejemplos utilizados en este tema, puedes acceder a la carpeta correspondiente.

👉 [Ver codigos del Tema 6](./Tema_6)
