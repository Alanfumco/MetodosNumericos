# Tema 1: Introducción a los Métodos Numéricos

## Concepto General

Los métodos numéricos son técnicas matemáticas utilizadas para obtener soluciones aproximadas a distintos problemas matemáticos mediante operaciones aritméticas y algoritmos computacionales.

Estas herramientas son fundamentales en áreas como ingeniería, programación, física y ciencias computacionales, ya que permiten resolver problemas complejos que muchas veces no tienen solución exacta de manera analítica.

En computación es muy importante comprender cómo las computadoras representan los números reales mediante punto flotante, debido a que la memoria y la precisión son limitadas. Esto puede provocar errores durante los cálculos numéricos.

---

# Métodos y Conceptos Importantes

## 1. Acumulación de Errores en Bucles

Sucede cuando pequeños errores de redondeo se van acumulando después de muchas iteraciones repetitivas.

### Fórmula

```text
suma = suma + valor
```

### Algoritmo

1. Inicializar una variable en cero.
2. Repetir una suma decimal varias veces.
3. Mostrar el resultado final.
4. Comparar el resultado esperado con el obtenido.

### Pseudocódigo

```text
INICIO

 suma <- 0.0

 PARA i <- 1 HASTA 10 HACER
     suma <- suma + 0.1
 FIN PARA

 ESCRIBIR suma

FIN
```

---

## 2. Cancelación por Resta

Ocurre cuando se restan números muy cercanos entre sí, provocando pérdida de precisión en los dígitos significativos.

### Fórmula

```text
resultado = a - b
```

### Algoritmo

1. Definir dos números muy similares.
2. Realizar la resta.
3. Observar la pérdida de precisión.

### Pseudocódigo

```text
INICIO

 a <- 1.000001
 b <- 1.000000

 resultado <- a - b

 ESCRIBIR resultado

FIN
```

---

## 3. Comparación Directa

Este problema ocurre cuando se comparan números decimales directamente usando igualdad exacta.

### Fórmula

```text
a == b
```

### Algoritmo

1. Declarar dos números flotantes.
2. Compararlos directamente.
3. Mostrar si son iguales o no.

### Pseudocódigo

```text
INICIO

 a <- 0.1 + 0.2
 b <- 0.3

 SI a == b ENTONCES
     ESCRIBIR "Iguales"
 SINO
     ESCRIBIR "Diferentes"
 FIN SI

FIN
```

---

## 4. Conversión Estrecha

Sucede cuando un valor grande se convierte a un tipo de dato más pequeño, perdiendo información.

### Fórmula

```text
entero = decimal
```

### Algoritmo

1. Declarar un número decimal.
2. Convertirlo a entero.
3. Mostrar la pérdida de decimales.

### Pseudocódigo

```text
INICIO

 decimal <- 5.98

 entero <- decimal

 ESCRIBIR entero

FIN
```

---

## 5. Desbordamiento Silencioso

Ocurre cuando un número supera la capacidad máxima de almacenamiento permitida.

### Fórmula

```text
resultado = numero_maximo + 1
```

### Algoritmo

1. Definir un número muy grande.
2. Sumar una unidad.
3. Observar el comportamiento del sistema.

### Pseudocódigo

```text
INICIO

 numero <- 999999999

 numero <- numero + 1

 ESCRIBIR numero

FIN
```

---

## 6. Error de Redondeo Binario

Las computadoras representan números decimales en binario, lo que provoca aproximaciones.

### Fórmula

```text
0.1 + 0.2
```

### Algoritmo

1. Sumar números decimales.
2. Mostrar el resultado.
3. Analizar la diferencia decimal.

### Pseudocódigo

```text
INICIO

 resultado <- 0.1 + 0.2

 ESCRIBIR resultado

FIN
```

---

## 7. Pérdida de Precisión por Magnitud

Sucede cuando se suman números muy pequeños con números extremadamente grandes.

### Fórmula

```text
resultado = numero_grande + numero_pequeño
```

### Algoritmo

1. Declarar un número muy grande.
2. Declarar un número pequeño.
3. Realizar la suma.
4. Observar la pérdida de precisión.

### Pseudocódigo

```text
INICIO

 grande <- 1000000000
 pequeño <- 0.000001

 resultado <- grande + pequeño

 ESCRIBIR resultado

FIN
```

---

# Ejemplo del Tema

Todos estos ejemplos permiten comprender cómo las limitaciones internas de las computadoras afectan los cálculos matemáticos.

Con estos métodos es posible analizar:

* errores de precisión,
* errores de redondeo,
* pérdida de exactitud,
* comportamiento de números flotantes,
* y limitaciones de almacenamiento.

---

# Implementaciones y Códigos

Si deseas visualizar los programas y ejemplos utilizados en este tema, puedes acceder a la carpeta correspondiente desde el siguiente enlace:
