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
> Xavier Fernández Rodriguez

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


![Resultado de los tests unitarios](tests.png)



#### Código desarrollado

Inserte a continuación el contenido del fichero `primos.py` usando los comandos necesarios para que se realice el
realce sintáctico en Python del mismo.

```python
Alumno: Xavi Fernandez Rodriguez

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
    Evalúa si un número dado es primo.
    
    Argumentos:
    numero -- Un número natural mayor que 1.
    
    Devuelve:
    True si el número es primo, False en caso contrario.
    
    Excepciones:
    TypeError -- Si el argumento no es un número entero o es menor o igual a 1.
    """
    if not isinstance(numero, int) or numero <= 1:
        raise TypeError("El argumento debe ser un número natural mayor que uno.")
    
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


def primos(numero):
    """
    Calcula todos los números primos menores que un valor dado.
    
    Argumentos:
    numero -- El límite superior (exclusivo) para buscar números primos.
    
    Devuelve:
    Una tupla con todos los números primos menores que el argumento.
    """
    return tuple(i for i in range(2, numero) if esPrimo(i))


def descompon(numero):
    """
    Calcula la descomposición en factores primos de un número.
    
    Argumentos:
    numero -- Número natural a descomponer.
    
    Devuelve:
    Una tupla con la secuencia de factores primos en orden ascendente.
    """
    factores = []
    divisor = 2
    n = numero
    
    while n > 1:
        if n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        else:
            divisor += 1
            
    return tuple(factores)


def mcm(*numeros):
    """
    Calcula el mínimo común múltiplo (MCM) de una cantidad arbitraria de números.
    Se basa en la descomposición de factores primos (sub-óptimo según el enunciado).
    
    Argumentos:
    *numeros -- Una secuencia arbitraria de números enteros.
    
    Devuelve:
    El mínimo común múltiplo de todos los argumentos pasados.
    """
    factores_maximos = {}
    
    for num in numeros:
        factores = descompon(num)
        # Contamos cuántas veces aparece cada factor en el número actual
        conteo_actual = {f: factores.count(f) for f in set(factores)}
        
        # Nos quedamos con el exponente máximo para cada factor primo
        for factor, cantidad in conteo_actual.items():
            if factor in factores_maximos:
                factores_maximos[factor] = max(factores_maximos[factor], cantidad)
            else:
                factores_maximos[factor] = cantidad
                
    resultado = 1
    for factor, cantidad in factores_maximos.items():
        resultado *= (factor ** cantidad)
        
    return resultado


def mcd(*numeros):
    """
    Calcula el máximo común divisor (MCD) de una cantidad arbitraria de números.
    Se basa en la descomposición de factores primos sin depender de la función mcm.
    
    Argumentos:
    *numeros -- Una secuencia arbitraria de números enteros.
    
    Devuelve:
    El máximo común divisor de todos los argumentos pasados.
    """
    if not numeros:
        return 1
        
    # Inicializamos los factores comunes con la descomposición del primer número
    factores_comunes = {}
    factores_iniciales = descompon(numeros[0])
    for f in set(factores_iniciales):
        factores_comunes[f] = factores_iniciales.count(f)
        
    # Intersectamos con los factores de los siguientes números (exponente mínimo)
    for num in numeros[1:]:
        factores = descompon(num)
        conteo_actual = {f: factores.count(f) for f in set(factores)}
        
        nuevos_comunes = {}
        for factor, cantidad in factores_comunes.items():
            if factor in conteo_actual:
                nuevos_comunes[factor] = min(cantidad, conteo_actual[factor])
                
        factores_comunes = nuevos_comunes
        
    resultado = 1
    for factor, cantidad in factores_comunes.items():
        resultado *= (factor ** cantidad)
        
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
