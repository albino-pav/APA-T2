"""
Nombre del alumno: Sandra Cots Agüera
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
    """Devuelve True si el argumento es primo. Requiere natural > 1."""
    if not isinstance(numero, int) or numero <= 1:
        raise TypeError("Debe ser un número natural mayor que 1.")
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primos(numero):
    """Devuelve tupla con primos menores que el argumento."""
    return tuple(n for n in range(2, numero) if esPrimo(n))

def descompon(numero):
    """Descomposición en factores primos."""
    f, d, n = [], 2, numero
    while n > 1:
        while n % d == 0:
            f.append(d)
            n //= d
        d += 1
    return tuple(f)

def mcd(*numeros):
    """Máximo Común Divisor de n argumentos."""
    from collections import Counter
    res = Counter(descompon(numeros[0]))
    for n in numeros[1:]:
        c = Counter(descompon(n))
        for k in res:
            res[k] = min(res[k], c[k])
    total = 1
    for k, v in res.items(): total *= k**v
    return total

def mcm(*numeros):
    """Mínimo Común Múltiplo de n argumentos."""
    from collections import Counter
    res = Counter()
    for n in numeros:
        c = Counter(descompon(n))
        for k, v in c.items():
            res[k] = max(res[k], v)
    total = 1
    for k, v in res.items(): total *= k**v
    return total

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
