"""
Autor: Marc Grau Casado

Módulo primos: gestión de números primos.

Tests unitarios
===============

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

from collections import Counter
import doctest


def _validar_numero(numero):
    """
    Comprueba que el argumento sea un número natural mayor que uno.

    Args:
        numero (int): Valor a validar.

    Raises:
        TypeError: Si el argumento no es un entero mayor que uno.
    """
    if not isinstance(numero, int) or isinstance(numero, bool) or numero <= 1:
        raise TypeError("El argumento debe ser un número natural mayor que uno.")


def esPrimo(numero):
    """
    Devuelve True si su argumento es primo y False en caso contrario.

    Args:
        numero (int): Número natural mayor que uno.

    Returns:
        bool: True si el número es primo, False si no lo es.

    Raises:
        TypeError: Si el argumento no es un número natural mayor que uno.
    """
    _validar_numero(numero)

    if numero == 2:
        return True

    if numero % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 2

    return True


def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que su argumento.

    Args:
        numero (int): Número natural mayor que uno.

    Returns:
        tuple: Tupla con los números primos menores que numero.

    Raises:
        TypeError: Si el argumento no es un número natural mayor que uno.
    """
    _validar_numero(numero)
    return tuple(n for n in range(2, numero) if esPrimo(n))


def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.

    Args:
        numero (int): Número natural mayor que uno.

    Returns:
        tuple: Tupla con los factores primos de numero, ordenados de menor a mayor.

    Raises:
        TypeError: Si el argumento no es un número natural mayor que uno.
    """
    _validar_numero(numero)

    factores = []
    n = numero

    while n % 2 == 0:
        factores.append(2)
        n //= 2

    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        divisor += 2

    if n > 1:
        factores.append(n)

    return tuple(factores)


def mcm(*numeros):
    """
    Devuelve el mínimo común múltiplo de un número arbitrario de argumentos.

    Args:
        *numeros (int): Números naturales mayores que uno.

    Returns:
        int: Mínimo común múltiplo de los argumentos.

    Raises:
        TypeError: Si no se proporcionan argumentos válidos.
    """
    if not numeros:
        raise TypeError("Debe proporcionarse al menos un número.")

    for numero in numeros:
        _validar_numero(numero)

    maximos = Counter()

    for numero in numeros:
        factores = Counter(descompon(numero))
        for primo, exponente in factores.items():
            if exponente > maximos[primo]:
                maximos[primo] = exponente

    resultado = 1
    for primo, exponente in maximos.items():
        resultado *= primo ** exponente

    return resultado


def mcd(*numeros):
    """
    Devuelve el máximo común divisor de un número arbitrario de argumentos.

    Args:
        *numeros (int): Números naturales mayores que uno.

    Returns:
        int: Máximo común divisor de los argumentos.

    Raises:
        TypeError: Si no se proporcionan argumentos válidos.
    """
    if not numeros:
        raise TypeError("Debe proporcionarse al menos un número.")

    for numero in numeros:
        _validar_numero(numero)

    comunes = Counter(descompon(numeros[0]))

    for numero in numeros[1:]:
        factores = Counter(descompon(numero))
        interseccion = Counter()
        for primo in comunes:
            if primo in factores:
                interseccion[primo] = min(comunes[primo], factores[primo])
        comunes = interseccion

    resultado = 1
    for primo, exponente in comunes.items():
        resultado *= primo ** exponente

    return resultado


if __name__ == "__main__":
    doctest.testmod(verbose=True)
