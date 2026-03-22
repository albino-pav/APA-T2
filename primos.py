"""
Manejo de números primos.

Nombre: Álvaro Ramo Irurre

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
    Devuelve True si numero es primo, False si no lo es.

    El argumento debe ser un número natural mayor que 1.
    En caso contrario, eleva TypeError.

    >>> esPrimo(2)
    True
    >>> esPrimo(9)
    False
    """
    if not isinstance(numero, int) or numero < 2:
        raise TypeError(f"{numero} no es un número natural mayor que 1")

    for divisor in range(2, int(numero**0.5) + 1):
        if numero % divisor == 0:
            return False
    return True


def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que numero.

    >>> primos(10)
    (2, 3, 5, 7)
    """
    return tuple(n for n in range(2, numero) if esPrimo(n))


def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de numero.

    >>> descompon(12)
    (2, 2, 3)
    """
    factores = []
    divisor = 2
    while divisor * divisor <= numero:
        while numero % divisor == 0:
            factores.append(divisor)
            numero //= divisor
        divisor += 1
    if numero > 1:
        factores.append(numero)
    return tuple(factores)


def mcm(*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.

    >>> mcm(4, 6)
    12
    """
    factores_mcm = {}
    for numero in numeros:
        factores = descompon(numero)
        conteo = {}
        for factor in factores:
            conteo[factor] = conteo.get(factor, 0) + 1
        for factor, exp in conteo.items():
            if factores_mcm.get(factor, 0) < exp:
                factores_mcm[factor] = exp

    resultado = 1
    for factor, exp in factores_mcm.items():
        resultado *= factor ** exp
    return resultado


def mcd(*numeros):
    """
    Devuelve el máximo común divisor de sus argumentos.

    >>> mcd(12, 8)
    4
    """
    factores_mcd = {}
    for i, numero in enumerate(numeros):
        factores = descompon(numero)
        conteo = {}
        for factor in factores:
            conteo[factor] = conteo.get(factor, 0) + 1

        if i == 0:
            factores_mcd = conteo
        else:
            factores_mcd = {
                factor: min(exp, conteo.get(factor, 0))
                for factor, exp in factores_mcd.items()
                if factor in conteo
            }

    resultado = 1
    for factor, exp in factores_mcd.items():
        resultado *= factor ** exp
    return resultado


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)