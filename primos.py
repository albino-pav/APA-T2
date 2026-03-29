"""
Primos: funciones para trabajar con números primos.
Javier González Montesinos

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
    """Determina si un número es primo."""
    if not isinstance(numero, int) or numero <= 1:
        raise TypeError("El argumento debe ser un entero mayor que 1")
    if numero == 2: 
        return True
    if numero % 2 == 0: 
        return False
    i = 3
    while i * i <= numero:
        if numero % i == 0:
            return False
        i += 2
    return True


def primos(numero):
    """Devuelve tupla con primos menores que numero."""
    if not isinstance(numero, int) or numero < 2:
        return ()
    return tuple(i for i in range(2, numero) if esPrimo(i))


def descompon(numero):
    """Devuelve tupla con factores primos (con multiplicidad)."""
    if not isinstance(numero, int) or numero < 2:
        return ()
    
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


def mcd_dos(a, b):
    """Máximo común divisor de dos números."""
    if a == 0 or b == 0:
        return 0
    fa = descompon(abs(a))
    fb = descompon(abs(b))
    comunes = []
    i = j = 0
    while i < len(fa) and j < len(fb):
        if fa[i] == fb[j]:
            comunes.append(fa[i])
            i += 1
            j += 1
        elif fa[i] < fb[j]:
            i += 1
        else:
            j += 1
    res = 1
    for f in comunes:
        res *= f
    return res


def mcm_dos(a, b):
    """Mínimo común múltiplo de dos números."""
    if a == 0 or b == 0:
        return 0
    fa = descompon(abs(a))
    fb = descompon(abs(b))
    from collections import Counter
    ca = Counter(fa)
    cb = Counter(fb)
    res = 1
    for p in set(ca) | set(cb):
        res *= p ** max(ca[p], cb[p])
    return res


def mcd(*numeros):
    """MCD de varios números."""
    if len(numeros) == 0:
        return 0
    if len(numeros) == 1:
        return abs(numeros[0])
    
    resultado = numeros[0]
    for n in numeros[1:]:
        resultado = mcd_dos(resultado, n) 
        if resultado == 1:
            return 1
    return resultado


def mcm(*numeros):
    """MCM de varios números."""
    if len(numeros) == 0:
        return 0
    if len(numeros) == 1:
        return abs(numeros[0])
    
    resultado = numeros[0]
    for n in numeros[1:]:
        resultado = mcm_dos(resultado, n)  
    return resultado