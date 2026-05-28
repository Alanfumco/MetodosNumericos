# Tema 3: Métodos de Solución de Sistemas de Ecuaciones

## Introducción

Los métodos de solución de sistemas de ecuaciones permiten encontrar los valores desconocidos de varias variables al mismo tiempo. Estos procedimientos son fundamentales en áreas como ingeniería, programación, física y análisis numérico, ya que muchos problemas reales pueden representarse mediante sistemas lineales.

Existen dos tipos principales de métodos:

* **Métodos directos**, que obtienen la solución en un número finito de pasos.
* **Métodos iterativos**, que generan aproximaciones sucesivas hasta alcanzar una solución suficientemente precisa.

---

## Métodos Principales

### Método de Gauss-Jordan

Transforma la matriz del sistema hasta obtener una matriz identidad, permitiendo encontrar directamente el valor de cada incógnita.

### Método de Jacobi

Calcula nuevas aproximaciones utilizando únicamente los valores de la iteración anterior.

### Método de Gauss-Seidel

Similar al método de Jacobi, pero aprovecha los valores recién calculados para acelerar la convergencia.

---

## Fórmulas Utilizadas

### Método de Jacobi

```text id="nwl7r5"
xi(k+1) = ( bi - Σ(aij * xj(k)) ) / aii
```

### Método de Gauss-Seidel

```text id="j4v7bn"
xi(k+1) = ( bi - Σ(aij * xj(k+1)) - Σ(aij * xj(k)) ) / aii
```

---

# Algoritmo y Pseudocódigo (Gauss-Jordan)

## Algoritmo

1. Seleccionar una fila pivote.
2. Dividir toda la fila entre el elemento diagonal para convertirlo en 1.
3. Eliminar los demás elementos de la columna usando operaciones entre filas.
4. Repetir el procedimiento para todas las filas.
5. Obtener directamente las soluciones del sistema.

## Pseudocódigo

```text id="3xzkp8"
INICIO GaussJordan(A, b)

  PARA i <- 1 HASTA n HACER

      pivote <- A[i,i]

      PARA j <- 1 HASTA n HACER
          A[i,j] <- A[i,j] / pivote
      FIN PARA

      b[i] <- b[i] / pivote

      PARA k <- 1 HASTA n HACER

          SI k != i ENTONCES

              factor <- A[k,i]

              PARA j <- 1 HASTA n HACER
                  A[k,j] <- A[k,j] - factor * A[i,j]
              FIN PARA

              b[k] <- b[k] - factor * b[i]

          FIN SI

      FIN PARA

  FIN PARA

  RETORNAR b

FIN
```

---

# Algoritmo y Pseudocódigo (Jacobi)

## Algoritmo

1. Definir una aproximación inicial.
2. Calcular nuevos valores para cada variable utilizando los valores anteriores.
3. Repetir las iteraciones hasta que el error sea menor a la tolerancia establecida.
4. Mostrar el vector solución aproximado.

## Pseudocódigo

```text id="h6x0pw"
INICIO Jacobi(A, b, x0, tol, max_iter)

  PARA k <- 1 HASTA max_iter HACER

      PARA i <- 1 HASTA n HACER

          suma <- 0

          PARA j <- 1 HASTA n HACER

              SI i != j ENTONCES
                  suma <- suma + A[i,j] * x0[j]
              FIN SI

          FIN PARA

          x_nuevo[i] <- ( b[i] - suma ) / A[i,i]

      FIN PARA

      SI norma(x_nuevo - x0) < tol ENTONCES
          RETORNAR x_nuevo
      FIN SI

      x0 <- x_nuevo

  FIN PARA

FIN
```

---

# Algoritmo y Pseudocódigo (Gauss-Seidel)

## Algoritmo

1. Seleccionar un vector inicial.
2. Actualizar cada variable utilizando inmediatamente los nuevos valores calculados.
3. Repetir el proceso iterativo.
4. Detenerse cuando el error sea suficientemente pequeño.

## Pseudocódigo

```text id="2i0l4d"
INICIO GaussSeidel(A, b, x, tol, max_iter)

  PARA k <- 1 HASTA max_iter HACER

      error <- 0

      PARA i <- 1 HASTA n HACER

          suma <- 0

          PARA j <- 1 HASTA n HACER

              SI i != j ENTONCES
                  suma <- suma + A[i,j] * x[j]
              FIN SI

          FIN PARA

          x_nuevo <- ( b[i] - suma ) / A[i,i]

          error <- error + |x_nuevo - x[i]|

          x[i] <- x_nuevo

      FIN PARA

      SI error < tol ENTONCES
          RETORNAR x
      FIN SI

  FIN PARA

FIN
```

---

## Aplicaciones de los Sistemas de Ecuaciones

Estos métodos son utilizados en:

* simulaciones matemáticas,
* modelado físico,
* circuitos eléctricos,
* análisis estructural,
* inteligencia artificial,
* y programación científica.

---

## Implementaciones y Códigos

Si deseas visualizar los programas y ejemplos utilizados en este tema, puedes acceder a los archivos correspondientes desde la carpeta del tema.

👉 [Ver codigos del Tema 3](./Tema_3)
