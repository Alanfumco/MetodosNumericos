# Tema 2: Métodos de Solución de Ecuaciones

## Introducción

Los métodos numéricos para solución de ecuaciones permiten encontrar aproximaciones de las raíces de una función matemática, es decir, los valores de `x` donde la función es igual a cero.

Estos métodos son ampliamente utilizados en ingeniería, programación, física y matemáticas aplicadas debido a que muchas ecuaciones no pueden resolverse de manera exacta mediante álgebra tradicional.

Los métodos iterativos realizan aproximaciones sucesivas hasta obtener un resultado suficientemente preciso según una tolerancia establecida.

---

# Métodos Principales

## 1. Método de Bisección

El método de bisección divide repetidamente un intervalo en dos partes para localizar la raíz de una función.

Este método garantiza convergencia siempre que exista un cambio de signo dentro del intervalo.

### Fórmula

```text
xr = (a + b) / 2
```

### Algoritmo

1. Definir el intervalo inicial `[a,b]`.
2. Verificar que exista cambio de signo.
3. Calcular el punto medio.
4. Evaluar la función en el punto medio.
5. Seleccionar el nuevo intervalo.
6. Repetir hasta cumplir la tolerancia.

### Pseudocódigo

```text
INICIO Biseccion(f,a,b,tol)

 SI f(a)*f(b) >= 0 ENTONCES
     RETORNAR ERROR
 FIN SI

 MIENTRAS (b-a)/2 > tol HACER

     xr <- (a+b)/2

     SI f(a)*f(xr) < 0 ENTONCES
         b <- xr
     SINO
         a <- xr
     FIN SI

 FIN MIENTRAS

 RETORNAR xr

FIN
```

---

## 2. Método de Newton-Raphson

El método de Newton-Raphson utiliza derivadas para obtener aproximaciones rápidas de la raíz de una ecuación.

Este método suele converger más rápido que otros métodos iterativos.

### Fórmula

```text
x(n+1) = xn - f(xn)/f'(xn)
```

### Algoritmo

1. Seleccionar una aproximación inicial.
2. Evaluar la función y su derivada.
3. Aplicar la fórmula iterativa.
4. Actualizar el valor de `x`.
5. Repetir hasta minimizar el error.

### Pseudocódigo

```text
INICIO NewtonRaphson(f,df,x0,tol)

 x <- x0

 MIENTRAS |f(x)| > tol HACER

     x <- x - f(x)/df(x)

 FIN MIENTRAS

 RETORNAR x

FIN
```

---

## 3. Método de la Secante

El método de la secante aproxima la raíz utilizando dos valores iniciales y evitando el uso directo de derivadas.

Este método es más rápido que bisección en muchos casos.

### Fórmula

```text
x(i+1)=xi-[f(xi)(x(i-1)-xi)]/[f(x(i-1))-f(xi)]
```

### Algoritmo

1. Definir dos aproximaciones iniciales.
2. Evaluar la función en ambos puntos.
3. Calcular la nueva aproximación.
4. Actualizar los valores anteriores.
5. Repetir hasta alcanzar el error deseado.

### Pseudocódigo

```text
INICIO Secante(f,x0,x1,tol)

 MIENTRAS |x1-x0| > tol HACER

     x2 <- x1-(f(x1)*(x0-x1))/(f(x0)-f(x1))

     x0 <- x1
     x1 <- x2

 FIN MIENTRAS

 RETORNAR x2

FIN
```

---

## 4. Método de Falsa Posición

El método de falsa posición combina características del método de bisección y secante para aproximar raíces dentro de un intervalo.

Utiliza interpolación lineal para obtener mejores aproximaciones.

### Fórmula

```text
xr = b - [f(b)(a-b)]/[f(a)-f(b)]
```

### Algoritmo

1. Definir el intervalo inicial.
2. Verificar cambio de signo.
3. Calcular el punto usando falsa posición.
4. Evaluar la función.
5. Actualizar el intervalo.
6. Repetir hasta cumplir la tolerancia.

### Pseudocódigo

```text
INICIO FalsaPosicion(f,a,b,tol)

 SI f(a)*f(b) >= 0 ENTONCES
     RETORNAR ERROR
 FIN SI

 MIENTRAS |f(xr)| > tol HACER

     xr <- b-(f(b)*(a-b))/(f(a)-f(b))

     SI f(a)*f(xr) < 0 ENTONCES
         b <- xr
     SINO
         a <- xr
     FIN SI

 FIN MIENTRAS

 RETORNAR xr

FIN
```

---

# Aplicaciones de los Métodos

Estos métodos son utilizados en:

* resolución de ecuaciones no lineales,
* simulaciones matemáticas,
* análisis científico,
* cálculos de ingeniería,
* programación numérica,
* modelado computacional,
* y desarrollo de software matemático.

---

# Implementaciones y Códigos

Si deseas visualizar los programas y ejemplos utilizados en este tema, puedes acceder a la carpeta correspondiente desde el siguiente enlace:

```text
Ver carpeta: Tema_2
```
