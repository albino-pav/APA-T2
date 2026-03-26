# Segunda tarea de APA 2026: Manejo de números primos

> [!Caution]
>
> El objetivo de esta tarea es manejar los tipos de datos y las estructuras de control de flujo de
> Python. Existen bibliotecas que resuelven los apartados del enunciado de una manera más eficiente
> y, sin duda, más sencilla, pero su uso está prohibido.
>
> Además, se valorará también el uso de Markdown en la redacción del fichero README.md; en concreto,
> la inclusión de código fuente con las herramientas propias de Markdown para su realce sintáctico, y
> la inclusión de imágenes con las capturas de pantalla solicitadas. El fichero README.md deberá ser
> visualizado correctamente desde la página principal del repositorio GitHub del alumno sin ninguna
> intervención por parte del profesor.
>
> Dispone del fichero MARKDOWN.md con información básica para el uso de Markdown, así como con enlaces
> a la documentación oficial del mismo.
>
> ¿Quiere saber más?, consulte con el profesorado.
  
## Nom i cognoms

> [!Important]
> Introduzca a continuación su nombre y apellidos:
>
> Alex Navarra Castañon

## Fichero `primos.py`

- El alumno debe escribir el fichero `primos.py` que incorporará distintas funciones relacionadas con el manejo
  de los números primos.

- El fichero debe incluir una cadena de documentación que incluirá el nombre del alumno y los tests unitarios
  de las funciones incluidas.

- Cada función deberá incluir su propia cadena de documentación que indicará el cometido de la función, los
  argumentos de la misma y la salida proporcionada.

- Se valorará lo pythónico de la solución; en concreto, su claridad y sencillez, y el uso de los estándares marcados
  por PEP-8. También se valorará su eficiencia computacional.

### Determinación de la *primalidad* y descomposición de un número en factores primos

Incluya en el fichero `primos.py` las tres funciones siguientes:

- `esPrimo(numero)`   Devuelve `True` si su argumento es primo, y `False` si no lo es.
  - Se debe considerar que `numero` es un número natural y mayor que uno.
  - En caso contrario, la función debe elevar la excepción `TypeError` y finalizar la ejecución.
- `primos(numero)`    Devuelve una **tupla** con todos los números primos menores que su argumento.
- `descompon(numero)` Devuelve una **tupla** con la descomposición en factores primos de su argumento.

### Obtención del mínimo común múltiplo y el máximo común divisor

Usando las tres funciones del apartado anterior (y cualquier otra que considere conveniente añadir), escriba otras
dos que calculen el máximo común divisor y el mínimo común múltiplo de sus argumentos:

- `mcm(numero1, numero2)`:  Devuelve el mínimo común múltiplo de sus argumentos.
- `mcd(numero1, numero2)`:  Devuelve el máximo común divisor de sus argumentos.

Estas dos funciones deben cumplir las condiciones siguientes:

- Aunque se trate de una solución sub-óptima, en ambos casos deberá partirse de la descomposición en factores
  primos de los argumentos usando las funciones del apartado anterior.

- Aunque también sea sub-óptimo desde el punto de vista de la programación, ninguna de las dos funciones puede
  depender de la otra; cada una debe programarse por separado.

### Obtención del mínimo común múltiplo y el máximo común divisor para un número arbitrario de argumentos

Modifique las funciones `mcm()` y `mcd()`, para que calculen el mínimo común múltiplo y el máximo común divisor
para un número arbitrario de argumentos:

- `mcm(*numeros)`:  Devuelve el mínimo común múltiplo de sus argumentos.
- `mcd(*numeros)`:  Devuelve el máximo común divisor de sus argumentos.

### Tests unitarios

La cadena de documentación del fichero debe incluir los tests unitarios de las cinco funciones. En concreto, deberán
comprobarse las siguientes condiciones:

- `esPrimo(numero)`:  Al ejecutar `[ numero for numero in range(2, 50) if esPrimo(numero) ]`, la salida debe ser
                      `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]`.
- `primos(numeor)`: Al ejecutar `primos(50)`, la salida debe ser `(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)`.
- `descompon(numero)`: Al ejecutar `descompon(36 * 175 * 143)`, la salida debe ser `(2, 2, 3, 3, 5, 5, 7, 11, 13)`.
- `mcm(num1, num2)`: Al ejecutar `mcm(90, 14)`, la salida debe ser `630`.
- `mcd(num1, num2)`: Al ejecutar `mcd(924, 780)`, la salida debe ser `12`.
- `mcm(numeros)`: Al ejecutar `mcm(42, 60, 70, 63)`, la salida debe ser `1260`.
- `mcd(numeros)`: Al ejecutar `mcd(840, 630, 1050, 1470)`, la salida debe ser `210`.

### Entrega

#### Ejecución de los tests unitarios

Inserte a continuación una captura de pantalla que muestre el resultado de ejecutar el fichero `primos.py` con la opción
*verbosa*, de manera que se muestre el resultado de la ejecución de los tests unitarios.

![Ejecución de tests](pruebas.png)

#### Código desarrollado

Inserte a continuación el contenido del fichero `primos.py` usando los comandos necesarios para que se realice el
realce sintáctico en Python del mismo.

```python
"""
primos.py

Modulo para manejar numeros primos.

Test:

>>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)

>>> mcm(90, 14)
630

>>> mcd(924, 780)
12

>>> mcm(42, 60, 70, 63)
1260

>>> mcd(840, 630, 1050, 1470)
210

"""

def esPrimo(numero):
    """
    Funcion que comprueba si el numero es primo o no.

    Si numero es primo devuelve True,
    En caso contrario devuelve False.

    numero solo puede ser entero y mayor que uno.
    """

    if not isinstance(numero, int) or numero <= 1:
        raise TypeError('La entrada tiene que ser un numero entero y mayor que uno.')
        
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    
    else:
        return True

def primos(numero):
    """
    Funcion que devuelve una tupla con todos los primos por debajo de ese numero.

    numero solo puede ser positivo y mayor que dos.
    """

    if numero < 2 or not isinstance(numero, (int, float)):
        raise TypeError('La entrada tiene que ser un numero igual o mayor que dos.')
    
    resultado = []

    for i in range(2, int(numero) + 1):
        if esPrimo(i):
            resultado.append(i)

    return tuple(resultado)

def descompon(numero):
    """
    Funcion que devuelve la descomposicion en factores primos de numero.

    numero solo puede ser entero y mayor a uno.
    """

    if not isinstance(numero, int) or numero <= 1:
        raise TypeError('La entrada tiene que ser un numero entero y mayor que uno.')

    if esPrimo(numero):
        return (numero,)

    else:        
        resultado = []
        divisor = 2

        while numero > 1:
            if numero % divisor == 0:
                resultado.append(divisor)
                numero //= divisor
            else:
                divisor += 1

        return tuple(resultado)


def mcd2(numero1, numero2):
    """
    Funcion donde entras 2 numeros y te devuelve el maximo comun divisor

    numero1 y numero2 solo pueden enteros mayores que dos ambos.
    """

    if (not isinstance(numero1, int) or numero1 <= 1 or
        not isinstance(numero2, int) or numero2 <= 1):
        raise TypeError('Las entradas tiene que ser un numero entero y mayor que uno.')

    n = list(descompon(numero1))
    m = list(descompon(numero2))

    resultado = 1

    for i in n:
        if i in m:
            resultado *= i
            m.remove(i)
            
    return resultado

def mcm2(numero1, numero2):
    """
    Funcion donde entras 2 numeros y te devuelve el minimo comun multiplo

    numero1 y numero2 solo pueden enteros mayores que dos ambos.
    """

    if (not isinstance(numero1, int) or numero1 <= 1 or
        not isinstance(numero2, int) or numero2 <= 1):
        raise TypeError('Las entradas tiene que ser un numero entero y mayor que uno.')

    n = list(descompon(numero1))
    m = list(descompon(numero2))

    resultado = 1

    for i in n:
        resultado *= i
        if i in m:
            m.remove(i)

    for i in m:
        resultado *= i

    return resultado

def mcd(* numeros):
    """
    Funcion donde entras varios numeros y te devuelve el maximo comun divisor

    numero1 y numero2 solo pueden enteros mayores que dos ambos.
    """
    if len(numeros) < 2:
        raise TypeError('Debes introducir al menos dos numeros.')

    resultado = numeros[0]

    for n in numeros[1:]:
        resultado = mcd2(resultado, n)

    return resultado

def mcm(*numeros):
    """
    Funcion donde entras varios numeros y te devuelve el minimo comun multiplo

    numero1 y numero2 solo pueden enteros mayores que dos ambos.
    """
    
    if len(numeros) < 2:
        raise TypeError('Debes introducir al menos dos numeros.')

    resultado = numeros[0]

    for n in numeros[1:]:
        resultado = mcm2(resultado, n)

    return resultado

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)
```

#### Subida del resultado al repositorio GitHub ¿y *pull-request*?

El fichero `primos.py`, la imagen con la ejecución de los tests unitarios y este mismo fichero, `README.md`, deberán
subirse al repositorio GitHub mediante la orden `git push`. Si los profesores de la asignatura consiguen montar el
sistema a tiempo, la entrega se formalizará realizando un *pull-request* al propietario del repositorio original.

El fichero `README.md` deberá respetar las reglas de los ficheros Markdown y visualizarse correctamente en el repositorio,
incluyendo la imagen con la ejecución de los tests unitarios y el realce sintáctico del código fuente insertado.
