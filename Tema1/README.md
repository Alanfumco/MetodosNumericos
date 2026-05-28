# Tema 1: Introducción a los Métodos Numéricos

## Concepto General

Los métodos numéricos son procedimientos matemáticos utilizados para obtener soluciones aproximadas a problemas que, en muchos casos, no pueden resolverse de manera exacta. Estas técnicas son ampliamente utilizadas en programación, ingeniería y ciencias computacionales para realizar cálculos complejos mediante operaciones aritméticas.

En el área de la computación, es importante comprender cómo las computadoras representan los números reales usando punto flotante, ya que esto puede provocar pequeñas variaciones en los resultados debido a limitaciones de almacenamiento y precisión.

---

## Conceptos Importantes

### Error de Redondeo

Sucede cuando un número contiene más decimales de los que la computadora puede almacenar, por lo que se aproxima al valor más cercano.

### Cancelación Catastrófica

Aparece cuando se restan números muy similares entre sí, ocasionando pérdida de precisión en los dígitos significativos.

### Desbordamiento

Ocurre cuando el resultado de una operación supera la capacidad máxima que puede almacenar el sistema.

---

## Algoritmo: Suma Repetitiva de Números Flotantes

1. Crear una variable llamada `suma` e inicializarla en `0.0`.
2. Definir el valor que se agregará repetidamente (`0.1`).
3. Repetir la suma diez veces.
4. Mostrar el resultado obtenido y analizar la precisión decimal.

---

## Pseudocódigo

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

## Ejemplo del Tema

Este ejemplo permite observar cómo pequeñas operaciones con números decimales pueden generar diferencias en el resultado final debido a la precisión limitada de la computadora.

También se pueden analizar fenómenos como:

* errores de precisión,
* pérdida de exactitud,
* y comportamiento de números de punto flotante.

---

## Implementaciones y Códigos

Si deseas visualizar los programas y ejemplos utilizados en este tema, puedes acceder a la carpeta correspondiente desde el siguiente enlace:

 [Ver carpeta del Tema 1](./Tema_1)
