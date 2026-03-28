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
> Lulu Armoire Palomar

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

![Resultado de los tests](test.png)

#### Código desarrollado

Inserte a continuación el contenido del fichero `primos.py` usando los comandos necesarios para que se realice el
realce sintáctico en Python del mismo.

```python

"""
Primos: funciones para trabajar con números primos.
Lulu Armoire Palomar

Tests unitarios:

    >>> [numero for numero in range(2, 50) if esPrimo(numero)]
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
    Determina si un número es primo.
    
    Argumentos:
        numero (int): Número natural más grande que 1.
    
    Salida:
        bool: Devolvera True si es primo o False si no lo es.
    """ 
    # Comprovar si es un entero mayor a 1.
    if not isinstance(numero, int):
        raise TypeError("El argumento tiene que ser un número entero")
    if numero <= 1:
        raise TypeError("El argumento tiene que ser un número mayor a 1")

    # Ayuda a la eficiencia
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False 

    # Buscamos divisores impares. Empezamos en el 3 y vamos de 2 en 2 hasta la raíz cuadrada.
    i = 3
    while i * i <= numero:
        if numero % i == 0:
            return False
        i += 2
    return True 
    

def primos(numero):
    """
        Nos devuelve una tupla con todos os números primos más pequeños que el argumento.

        Argumentos:
        numero (int): Límite superior.
        
    Salida:
        tuple: Tupla con los números primos menores al argumento.
    """
    # Comprovar si es un entero mayor a 1.
    if not isinstance(numero, int):
        raise TypeError("El argumento tiene que ser un número entero")
    if numero <= 2:
        raise TypeError("El argumento tiene que ser mayor a 2")

    lista_primos = []
    for i in range(2, numero):
        if esPrimo(i):
            lista_primos.append(i)

    return tuple(lista_primos)


def descompon(numero):
    """
    Devuelve la tupla con la descomposición en factores primos de su argumento.
    Argumentos:
        numero (int): Número a descomponer (mayor a 1).
        
    Salida:
        tuple: Tupla con los factores primos.
    """
    
     # Comprovar si es un entero mayor a 1.
    if not isinstance(numero, int):
        raise TypeError("El argumento tiene que ser un número entero")
    if numero <= 1:
        raise TypeError("El argumento tiene que ser mayor a 1")

    factores = []
    n = numero
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        divisor += 1 if divisor == 2 else 2 # Despues del 2 probamos solo con impares

    if n > 1:
        factores.append(n)

    return tuple(factores)
    
def mcm(*numeros):
    """
    Calcula el mínimo común múltiplo de un número arbitrario de argumentos.
    
    Argumentos:
        *numeros (tuple): Números enteros más grandes que 1.
    
    Salida:
        int: Mínimo común múltiplo de todos los números.
    """
    # Comprobamos que haya al menos un argumento
    if len(numeros) == 0:
        raise TypeError("Necesitamos al menos un argumento")
    
    # Comprobamos que todos los argumentos son enteros más grandes que 1
    for n in numeros:
        if not isinstance(n, int):
            raise TypeError("Todos los argumentos tienen que ser números enteros")
        if n <= 1:
            raise TypeError("Todos los argumentos tienen que ser mayores que 1")
    
    todas_descomposiciones = []
    for n in numeros:
        todas_descomposiciones.append(list(descompon(n)))
        
    # Agrupamos todos los factores diferentes que aparecen
    factores_unicos = set()
    for lista in todas_descomposiciones:
        for factor in lista:
            factores_unicos.add(factor)
    
    factores_mcm = []
    
    for factor in factores_unicos:
        max_veces = 0
        for lista in todas_descomposiciones:
            veces = lista.count(factor)
            if veces > max_veces:
                max_veces = veces
        
        for _ in range(max_veces):
            factores_mcm.append(factor)
    
    resultado = 1
    for factor in factores_mcm:
        resultado = resultado * factor
    
    return resultado

def mcd(*numeros):
    """
    Calcula el máximo común divisor de un número arbitrario de argumentos.
    
    Argumentos:
        *numeros (tuple): Números enteros más grandes que 1.
    
    Salida:
        int: Máximo común divisor de todos los números.
    """
    # Comprobamos que haya al menos un argumento
    if len(numeros) == 0:
        raise TypeError("Necesitamos al menos un argumento")
    
    # Comprobamos que todos los argumentos son enteros más grandes que 1
    for n in numeros:
        if not isinstance(n, int):
            raise TypeError("Todos los argumentos tienen que ser números enteros")
        if n <= 1:
            raise TypeError("Todos los argumentos tienen que ser mayores que 1")
    
    todas_descomposiciones = []
    for n in numeros:
        todas_descomposiciones.append(list(descompon(n)))
    
    # PBuscamos los factores comunes a todos los números
    factores_comunes = todas_descomposiciones[0].copy()
    
    for i in range(1, len(todas_descomposiciones)):
        nuevos_comunes = []
        for factor in factores_comunes:
            if factor in todas_descomposiciones[i]:
                nuevos_comunes.append(factor)
                todas_descomposiciones[i].remove(factor)
        factores_comunes = nuevos_comunes
    
    resultado = 1
    for factor in factores_comunes:
        resultado = resultado * factor
    
    return resultado

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
```
#### Subida del resultado al repositorio GitHub ¿y *pull-request*?

El fichero `primos.py`, la imagen con la ejecución de los tests unitarios y este mismo fichero, `README.md`, deberán
subirse al repositorio GitHub mediante la orden `git push`. Si los profesores de la asignatura consiguen montar el
sistema a tiempo, la entrega se formalizará realizando un *pull-request* al propietario del repositorio original.

El fichero `README.md` deberá respetar las reglas de los ficheros Markdown y visualizarse correctamente en el repositorio,
incluyendo la imagen con la ejecución de los tests unitarios y el realce sintáctico del código fuente insertado.
