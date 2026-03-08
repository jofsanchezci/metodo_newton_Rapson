# Método de Newton-Raphson para el cálculo de raíces

## Introducción

El **método de Newton-Raphson** es un algoritmo numérico utilizado para
encontrar **raíces de funciones reales**.\
Una raíz de una función (f(x)) es un valor (x) tal que:

f(x) = 0

Este método es ampliamente usado en **ingeniería, ciencia de datos,
inteligencia artificial y simulación numérica** debido a su **rápida
convergencia**.

------------------------------------------------------------------------

## Fundamento matemático

El método utiliza una aproximación iterativa basada en la derivada de la
función.

La fórmula general es:

x\_(n+1) = x_n - f(x_n) / f'(x_n)

donde:

-   x_n : aproximación actual
-   f(x_n) : valor de la función
-   f'(x_n) : derivada de la función

El proceso se repite hasta que el error sea suficientemente pequeño.

------------------------------------------------------------------------

## Interpretación geométrica

El método funciona así:

1.  Se escoge una aproximación inicial.
2.  Se calcula la recta tangente de la función en ese punto.
3.  Se encuentra el punto donde esa tangente corta el eje x.
4.  Ese punto se usa como nueva aproximación.

Este proceso se repite iterativamente hasta converger a la raíz.

------------------------------------------------------------------------

## Aplicación al cálculo de la raíz cuadrada

Para calcular:

sqrt(a)

podemos formular el problema como:

f(x) = x² − a

y su derivada es:

f'(x) = 2x

Sustituyendo en Newton-Raphson:

x\_(n+1) = x_n − (x_n² − a)/(2x_n)

Simplificando:

x\_(n+1) = 1/2 ( x_n + a/x_n )

Esta es también conocida como el **método babilónico de la raíz
cuadrada**.

------------------------------------------------------------------------

## Algoritmo

1.  Escoger una aproximación inicial x₀
2.  Evaluar la función f(x)
3.  Evaluar la derivada f'(x)
4.  Calcular una nueva aproximación
5.  Repetir hasta cumplir una tolerancia

------------------------------------------------------------------------

## Implementación en Python

``` python
def newton_raphson(f, df, x0, tolerancia=1e-10, max_iter=100):
    """Implementación del método de Newton-Raphson"""

    x = x0

    for i in range(max_iter):

        x_nuevo = x - f(x) / df(x)

        if abs(x_nuevo - x) < tolerancia:
            return x_nuevo

        x = x_nuevo

    return x
```

------------------------------------------------------------------------

## Ejemplo: cálculo de √25

Definimos la función y su derivada:

``` python
def f(x):
    return x**2 - 25

def df(x):
    return 2*x
```

Aplicamos el método:

``` python
raiz = newton_raphson(f, df, x0=10)

print("Raíz aproximada:", raiz)
```

Salida esperada:

    Raíz aproximada: 5.0

------------------------------------------------------------------------


## Ventajas del método

-   Convergencia cuadrática (muy rápida)
-   Alta precisión
-   Implementación sencilla
-   Aplicable a múltiples problemas numéricos



