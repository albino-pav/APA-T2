"""
Manejo de números primos - Segunda tarea de APA 2026
Autor: Daniel Morera Torra

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
    """Devuelve True si numero es primo, False si no lo es.
    numero debe ser un entero mayor que 1, si no eleva TypeError.

    >>> esPrimo(7)
    True
    >>> esPrimo(9)
    False
    """
    if not isinstance(numero, int) or numero < 2:
        raise TypeError("El número debe ser un natural mayor que uno")
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


def primos(numero):
    """Devuelve una tupla con los primos menores que numero.

    >>> primos(10)
    (2, 3, 5, 7)
    """
    return tuple(n for n in range(2, numero) if esPrimo(n))


def descompon(numero):
    """Devuelve una tupla con los factores primos de numero.

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
    """Devuelve el mínimo común múltiplo de los argumentos.

    >>> mcm(90, 14)
    630
    >>> mcm(42, 60, 70, 63)
    1260
    """
    factores = {}
    for n in numeros:
        d = descompon(n)
        for p in set(d):
            factores[p] = max(factores.get(p, 0), d.count(p))
    resultado = 1
    for p, e in factores.items():
        resultado *= p**e
    return resultado


def mcd(*numeros):
    """Devuelve el máximo común divisor de los argumentos.

    >>> mcd(924, 780)
    12
    >>> mcd(840, 630, 1050, 1470)
    210
    """
    factores = {p: descompon(numeros[0]).count(p) for p in set(descompon(numeros[0]))}
    for n in numeros[1:]:
        d = descompon(n)
        factores = {p: min(e, d.count(p)) for p, e in factores.items() if p in d}
    resultado = 1
    for p, e in factores.items():
        resultado *= p**e
    return resultado


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
