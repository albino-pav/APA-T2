"""
Gestión de números primos.

Autor: Fulano Mengano Zutano

Tests unitarios de las funciones incluidas en este módulo:

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

    Arguments:
        numero: número natural mayor que 1.

    Returns:
        True si el número es primo, False si no lo es.

    Raises:
        TypeError: si el argumento no es un número natural mayor que 1.

    >>> esPrimo(2)
    True
    >>> esPrimo(4)
    False
    """
    if not isinstance(numero, int) or numero < 2:
        raise TypeError("El argumento debe ser un número natural mayor que 1.")

    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            return False
    return True


def primos(numero):
    """
    Devuelve todos los números primos menores que el argumento.

    Arguments:
        numero: número natural.

    Returns:
        Tupla con todos los primos menores que numero.

    >>> primos(10)
    (2, 3, 5, 7)
    """
    return tuple(n for n in range(2, numero) if esPrimo(n))


def descompon(numero):
    """
    Devuelve la descomposición en factores primos del argumento.

    Arguments:
        numero: número natural mayor que 1.

    Returns:
        Tupla con los factores primos de numero (con repetición).

    >>> descompon(12)
    (2, 2, 3)
    """
    factores = []
    divisor = 2
    while numero > 1:
        while numero % divisor == 0:
            factores.append(divisor)
            numero //= divisor
        divisor += 1
    return tuple(factores)


def mcm(*numeros):
    """
    Calcula el mínimo común múltiplo de dos o más números.

    Arguments:
        *numeros: dos o más números naturales.

    Returns:
        El mínimo común múltiplo de todos los argumentos.

    >>> mcm(90, 14)
    630
    >>> mcm(42, 60, 70, 63)
    1260
    """
    def mcm_dos(a, b):
        factores_a = list(descompon(a))
        factores_b = list(descompon(b))
        resultado = []
        for factor in set(factores_a + factores_b):
            resultado += [factor] * max(factores_a.count(factor), factores_b.count(factor))
        product = 1
        for f in resultado:
            product *= f
        return product

    result = numeros[0]
    for n in numeros[1:]:
        result = mcm_dos(result, n)
    return result


def mcd(*numeros):
    """
    Calcula el máximo común divisor de dos o más números.

    Arguments:
        *numeros: dos o más números naturales.

    Returns:
        El máximo común divisor de todos los argumentos.

    >>> mcd(924, 780)
    12
    >>> mcd(840, 630, 1050, 1470)
    210
    """
    def mcd_dos(a, b):
        factores_a = list(descompon(a))
        factores_b = list(descompon(b))
        resultado = []
        for factor in set(factores_a) & set(factores_b):
            resultado += [factor] * min(factores_a.count(factor), factores_b.count(factor))
        product = 1
        for f in resultado:
            product *= f
        return product

    result = numeros[0]
    for n in numeros[1:]:
        result = mcd_dos(result, n)
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
