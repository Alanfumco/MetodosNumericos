# Tema 3: Métodos de Solución de Sistemas de Ecuaciones

## Introducción

Los métodos numéricos para sistemas de ecuaciones permiten resolver conjuntos de ecuaciones lineales simultáneas mediante procedimientos matemáticos iterativos y directos.

Estos métodos son fundamentales en áreas como ingeniería, física, programación y análisis computacional, ya que muchos problemas reales pueden representarse mediante matrices y sistemas lineales.

Existen métodos directos, que obtienen la solución en un número determinado de pasos, y métodos iterativos, que aproximan la solución mediante repeticiones sucesivas.

---

# Métodos Principales

## 1. Método de Gauss-Jordan

El método de Gauss-Jordan transforma la matriz aumentada del sistema hasta obtener una matriz identidad, permitiendo encontrar directamente los valores de las incógnitas.

### Fórmula

```text
A|B → I|X
```

### Algoritmo

1. Formar la matriz aumentada.
2. Seleccionar un pivote.
3. Dividir la fila entre el pivote.
4. Hacer ceros arriba y abajo del pivote.
5. Repetir el proceso para cada fila.
6. Obtener las soluciones.

### Pseudocódigo

```text
INICIO GaussJordan

 PARA i <- 1 HASTA n HACER

     pivote <- A[i][i]

     DIVIDIR fila i ENTRE pivote

     PARA j <- 1 HASTA n HACER

         SI j != i ENTONCES

             factor <- A[j][i]

             RESTAR factor * fila i A fila j

         FIN SI

     FIN PARA

 FIN PARA

 MOSTRAR soluciones

FIN
```

---

## 2. Método de Jacobi

El método de Jacobi es un método iterativo que aproxima las soluciones usando únicamente los valores de la iteración anterior.

### Fórmula

```text
xi(k+1) = (bi - Σ(aij*xj(k))) / aii
```

### Algoritmo

1. Definir una aproximación inicial.
2. Calcular nuevos valores para cada incógnita.
3. Utilizar solamente valores anteriores.
4. Repetir hasta cumplir la tolerancia.

### Pseudocódigo

```text
INICIO Jacobi

 LEER matriz A y vector B

 DEFINIR valores iniciales

 REPETIR

     PARA i <- 1 HASTA n HACER

         suma <- 0

         PARA j <- 1 HASTA n HACER

             SI i != j ENTONCES

                 suma <- suma + A[i][j]*x[j]

             FIN SI

         FIN PARA

         xNuevo[i] <- (B[i]-suma)/A[i][i]

     FIN PARA

     x <- xNuevo

 HASTA cumplir tolerancia

 MOSTRAR resultados

FIN
```

---

## 3. Método de Gauss-Seidel

El método de Gauss-Seidel mejora el método de Jacobi utilizando inmediatamente los nuevos valores calculados durante cada iteración.

### Fórmula

```text
xi(k+1) = (bi - Σ(aij*xj)) / aii
```

### Algoritmo

1. Definir valores iniciales.
2. Calcular nuevas aproximaciones.
3. Actualizar inmediatamente los resultados.
4. Repetir hasta minimizar el error.

### Pseudocódigo

```text
INICIO GaussSeidel

 LEER matriz A y vector B

 DEFINIR valores iniciales

 REPETIR

     PARA i <- 1 HASTA n HACER

         suma <- 0

         PARA j <- 1 HASTA n HACER

             SI i != j ENTONCES

                 suma <- suma + A[i][j]*x[j]

             FIN SI

         FIN PARA

         x[i] <- (B[i]-suma)/A[i][i]

     FIN PARA

 HASTA cumplir tolerancia

 MOSTRAR resultados

FIN
```

---

## 4. Método de Eliminación Gaussiana

La eliminación gaussiana convierte el sistema en una matriz triangular superior para resolver posteriormente mediante sustitución hacia atrás.

### Fórmula

```text
A|B → U|B
```

### Algoritmo

1. Formar la matriz aumentada.
2. Seleccionar pivotes.
3. Hacer ceros debajo del pivote.
4. Continuar hasta triangular la matriz.
5. Resolver mediante sustitución hacia atrás.

### Pseudocódigo

```text
INICIO EliminacionGaussiana

 PARA k <- 1 HASTA n-1 HACER

     PARA i <- k+1 HASTA n HACER

         factor <- A[i][k] / A[k][k]

         PARA j <- k HASTA n HACER

             A[i][j] <- A[i][j] - factor*A[k][j]

         FIN PARA

         B[i] <- B[i] - factor*B[k]

     FIN PARA

 FIN PARA

 REALIZAR sustitucion hacia atras

 MOSTRAR soluciones

FIN
```

---

# Aplicaciones de los Métodos

Estos métodos son utilizados en:

* análisis estructural,
* simulaciones matemáticas,
* programación científica,
* modelado computacional,
* ingeniería,
* álgebra lineal,
* y resolución de sistemas grandes de ecuaciones.

---

# Implementaciones y Códigos

Si deseas visualizar los programas y ejemplos utilizados en este tema, puedes acceder a la carpeta correspondiente desde el siguiente enlace:

```text
Ver carpeta: Tema_3
```
