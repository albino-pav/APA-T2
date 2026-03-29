

# PRÁCTICA 2 : MÓDULO PARA MANEJO DE NÚMEROS PRIMOS
# Alicia Varón López - G12


"""
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

## FUNCIÓN esPrimo()
def esPrimo(numero):
    """Devuelve True si el número es primo, False si no lo es.
    Args:numero: Número natural mayor que 1
    Returns:bool: True si es primo, False si no lo es
    Raises:TypeError: Si el argumento no es un número natural mayor que 1"""
    # Verificar tipo y valor
    if not isinstance(numero, int) or numero <= 1:
        raise TypeError("El argumento debe ser un número natural mayor que 1")
    # Comprobar si es primo
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

## FUNCIÓN primos()
def primos(numero):
    """Devuelve una tupla con todos los números primos menores que el argumento.
    Args:numero: Número límite superior
    Returns: tuple: Números primos menores que numero"""
    primos_lista = []
    for n in range(2, numero):
        try:
            if esPrimo(n):
                primos_lista.append(n)
        except TypeError:
            continue
    return tuple(primos_lista)


## FUNCIÓN descompon()
def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos del argumento.
    Args:numero: Número a descomponer
    Returns:tuple: Factores primos
    """
    factores = []
    n = numero
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        else:
            divisor += 1

    return tuple(factores)


## FUNCIÓN mcm()
def mcm(*numeros):
    """
    Devuelve el mínimo común múltiplo de los argumentos.
    Args:*numeros: Números para calcular el mcm
    Returns:int: Mínimo común múltiplo
    """
    from collections import Counter

    factores_totales = {}

    for num in numeros:
        factores = descompon(num)
        contador = Counter(factores)
        for primo, exp in contador.items():
            if primo not in factores_totales or exp > factores_totales[primo]:
                factores_totales[primo] = exp

    resultado = 1
    for primo, exp in factores_totales.items():
        resultado *= primo ** exp

    return resultado

## FUNCIÓN mcd()
def mcd(*numeros):
    """
    Devuelve el máximo común divisor de los argumentos.
    Args:*numeros: Números para calcular el mcd
    Returns:int: Máximo común divisor
    """
    from collections import Counter

    if not numeros:
        return 0

    factores = [Counter(descompon(num)) for num in numeros]

    if factores:
        factores_comunes = set(factores[0].keys())
        for f in factores[1:]:
            factores_comunes &= set(f.keys())

        resultado = 1
        for primo in factores_comunes:
            min_exp = min(f[primo] for f in factores)
            resultado *= primo ** min_exp

        return resultado

    return 1


## EJECUCIÓN DE LOS TESTS
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)