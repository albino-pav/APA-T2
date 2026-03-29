"""
Autor: Ainhoa Dumitru

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
    Devuelve True si el número es primo.

    :param numero: entero mayor que 1
    :return: True o False
    """
    if not isinstance(numero, int) or numero <= 1:
        raise TypeError("El número debe ser natural mayor que 1")

    if numero == 2:
        return True

    if numero % 2 == 0:
        return False

    for i in range(3, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            return False

    return True


def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que numero.

    :param numero: entero
    :return: tupla de números primos
    """
    return tuple(n for n in range(2, numero) if esPrimo(n))


def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos del número.

    :param numero: entero mayor que 1
    :return: tupla de factores primos
    """
    if not isinstance(numero, int) or numero <= 1:
        raise TypeError("El número debe ser natural mayor que 1")

    factores = []
    divisor = 2

    while numero > 1:
        while numero % divisor == 0:
            factores.append(divisor)
            numero //= divisor
        divisor += 1

    return tuple(factores)

def mcd(*numeros):
    """
    Devuelve el máximo común divisor de varios números.

    :param numeros: enteros mayores que 1
    :return: mcd
    """
    if not numeros:
        raise TypeError("Debe proporcionar al menos un número")

    from collections import Counter

    # Descomposición del primer número
    comunes = Counter(descompon(numeros[0]))

    for numero in numeros[1:]:
        factores = Counter(descompon(numero))
        comunes &= factores  # intersección (mínimos)

    resultado = 1
    for factor, exponente in comunes.items():
        resultado *= factor ** exponente

    return resultado


def mcm(*numeros):
    """
    Devuelve el mínimo común múltiplo de varios números.

    :param numeros: enteros mayores que 1
    :return: mcm
    """
    if not numeros:
        raise TypeError("Debe proporcionar al menos un número")

    from collections import Counter

    maximos = Counter()

    for numero in numeros:
        factores = Counter(descompon(numero))
        for factor in factores:
            maximos[factor] = max(maximos[factor], factores[factor])

    resultado = 1
    for factor, exponente in maximos.items():
        resultado *= factor ** exponente

    return resultado

