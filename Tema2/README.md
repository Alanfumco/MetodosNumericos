# Tema 2: Métodos de Solución de Ecuaciones

## Introducción

Los métodos de solución de ecuaciones se utilizan para encontrar las raíces de funciones matemáticas, es decir, los valores de `x` donde una función toma el valor de cero.

En muchos problemas de ingeniería, física y programación, las ecuaciones no lineales no pueden resolverse fácilmente de forma algebraica, por lo que es necesario utilizar métodos numéricos iterativos que permitan aproximar la solución.

Existen diferentes técnicas para resolver este tipo de problemas. Algunos métodos garantizan encontrar una solución dentro de un intervalo específico, mientras que otros ofrecen resultados más rápidos dependiendo de la aproximación inicial utilizada.

---

## Métodos Principales

### Método de Bisección

Consiste en dividir repetidamente un intervalo en dos partes para localizar la raíz de una función.

### Método de Newton-Raphson

Utiliza derivadas para aproximar rápidamente la raíz de una ecuación mediante iteraciones sucesivas.

### Método de la Secante

Es similar al método de Newton-Raphson, pero evita el uso de derivadas utilizando dos aproximaciones iniciales.

---

## Fórmulas Utilizadas

### Método de Bisección

```text id="xtvg7f"
xr = (a + b) / 2
```

### Método de Newton-Raphson

```text id="m7izp1"
x(n+1) = xn - f(xn) / f'(xn)
```

### Método de la Secante

```text id="1q6ocm"
x(i+1) = xi - [ f(xi)(x(i-1) - xi) ] / [ f(x(i-1)) - f(xi) ]
```


## Algoritmo y Pseudocódigo (Bisección)

### Algoritmo

1. Definir un intervalo inicial `[a,b]`.
2. Verificar que exista un cambio de signo en la función.
3. Calcular el punto medio del intervalo.
4. Evaluar la función en el punto medio.
5. Seleccionar el nuevo subintervalo donde se encuentre la raíz.
6. Repetir el procedimiento hasta alcanzar la tolerancia deseada.

### Pseudocódigo

```text id="f0j2mx"
INICIO Biseccion(f, a, b, tol)

  SI f(a) * f(b) >= 0 ENTONCES
      RETORNAR ERROR
  FIN SI

  MIENTRAS (b - a)/2 > tol HACER

      xr <- (a + b)/2

      SI f(a) * f(xr) < 0 ENTONCES
          b <- xr
      SINO
          a <- xr
      FIN SI

  FIN MIENTRAS

  RETORNAR xr

FIN
```

---

## Algoritmo y Pseudocódigo (Newton-Raphson)

### Algoritmo

1. Seleccionar una aproximación inicial.
2. Evaluar la función y su derivada.
3. Aplicar la fórmula de Newton-Raphson.
4. Obtener una nueva aproximación.
5. Continuar iterando hasta minimizar el error.

### Pseudocódigo

```text id="4vqct8"
INICIO NewtonRaphson(f, df, x0, tol)

  x <- x0

  MIENTRAS |f(x)| > tol HACER

      x <- x - f(x)/df(x)

  FIN MIENTRAS

  RETORNAR x

FIN
```

---

## Algoritmo y Pseudocódigo (Secante)

### Algoritmo

1. Elegir dos valores iniciales.
2. Evaluar la función en ambos puntos.
3. Calcular una nueva aproximación usando la ecuación de la secante.
4. Actualizar los valores anteriores.
5. Repetir el procedimiento hasta alcanzar el error permitido.

### Pseudocódigo

```text id="2gprk5"
INICIO Secante(f, x0, x1, tol)

  MIENTRAS |x1 - x0| > tol HACER

      x2 <- x1 - ( f(x1) * (x0 - x1) ) / ( f(x0) - f(x1) )

      x0 <- x1
      x1 <- x2

  FIN MIENTRAS

  RETORNAR x2

FIN
```

---

## Aplicaciones de los Métodos

Estos métodos son ampliamente utilizados en:

* resolución de ecuaciones no lineales,
* simulaciones computacionales,
* cálculos científicos,
* ingeniería,
* análisis matemático,
* y desarrollo de software.

---

## Implementaciones y Códigos

Si deseas visualizar los programas y ejemplos utilizados en este tema, puedes acceder a los archivos correspondientes desde la carpeta del tema.

👉 [Ver codigos del Tema 2](./Tema_2)
