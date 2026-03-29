"""
Biel Piqué Marti

Tests unitarios:
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
    """
    Determina si un número natural es primo.

    Argumentos:
        numero (int): Número natural mayor que 1.

    Salida:
        (bool): True si el número es primo, False en caso contrario.
    """
    if not isinstance(numero, int) or numero <= 1:
        raise TypeError("El argumento debe ser un número entero mayor que 1.")
    
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primos(numero):
    """
    Obtiene una colección de todos los números primos menores que un límite dado.

    Argumentos:
        numero (int): El límite superior (no incluido).

    Salida:
        (tuple): Tupla con los números primos menores que 'numero'.
    """
    return tuple(n for n in range(2, numero) if esPrimo(n))

def descompon(numero):
    """
    Realiza la descomposición en factores primos de un número entero.

    Argumentos:
        numero (int): Número a descomponer.

    Salida:
        (tuple): Tupla con los factores primos del número, ordenados de menor a mayor.
    """
    factores = []
    divisor = 2
    temp = numero
    while temp > 1:
        while temp % divisor == 0:
            factores.append(divisor)
            temp //= divisor
        divisor += 1
    return tuple(factores)

def mcd(*numeros):
    """
    Calcula el máximo común divisor de un número arbitrario de argumentos
    partiendo de su descomposición en factores primos.

    Argumentos:
        *numeros (int): Uno o más números enteros.

    Salida:
        (int): El máximo común divisor de todos los argumentos proporcionados.
    """
    if not numeros:
        return None
    
    # 1. Obtener los diccionarios de factores para cada número
    lista_diccionarios = []
    for n in numeros:
        factores = descompon(n)
        d = {}
        for f in factores:
            d[f] = d.get(f, 0) + 1
        lista_diccionarios.append(d)

    # 2. Buscar factores comunes a TODOS los números
    factores_comunes = set(lista_diccionarios[0].keys())
    for d in lista_diccionarios[1:]:
        factores_comunes &= set(d.keys())

    # 3. Calcular el MCD: factores comunes al menor exponente
    resultado = 1
    for f in factores_comunes:
        min_exponente = min(d[f] for d in lista_diccionarios)
        resultado *= (f ** min_exponente)
        
    return resultado


def mcm(*numeros):
    """
    Calcula el mínimo común múltiplo de un número arbitrario de argumentos
    partiendo de su descomposición en factores primos.

    Argumentos:
        *numeros (int): Uno o más números enteros.

    Salida:
        (int): El mínimo común múltiplo de todos los argumentos proporcionados.
    """
    if not numeros:
        return None

    # 1. Obtener diccionarios de factores
    lista_diccionarios = []
    for n in numeros:
        factores = descompon(n)
        d = {}
        for f in factores:
            d[f] = d.get(f, 0) + 1
        lista_diccionarios.append(d)

    # 2. Recopilar todos los factores que aparecen en cualquier número
    todos_los_factores = set()
    for d in lista_diccionarios:
        todos_los_factores.update(d.keys())

    # 3. Calcular el MCM: todos los factores al mayor exponente
    resultado = 1
    for f in todos_los_factores:
        max_exponente = max(d.get(f, 0) for d in lista_diccionarios)
        resultado *= (f ** max_exponente)
        
    return resultado