"""
Segunda tarea de APA 2026: Manejo de números primos

Nombre y apellidos: Xavi Prats Castillo

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

import doctest


def _es_natural_mayor_que_uno(numero):
    """
    Comprueba que el argumento sea un número natural mayor que uno.

    Argumentos:
        numero (int): Valor que se desea validar.

    Salida:
        bool: True si el argumento es válido.

    Excepciones:
        TypeError: Se lanza si el argumento no es un entero natural mayor que uno.
    """
    if not isinstance(numero, int) or isinstance(numero, bool) or numero <= 1:
        raise TypeError("El argumento debe ser un número natural mayor que uno.")
    return True


def esPrimo(numero):
    """
    Determina si un número natural mayor que uno es primo.

    Argumentos:
        numero (int): Número natural mayor que uno.

    Salida:
        bool: True si el número es primo y False si no lo es.

    Excepciones:
        TypeError: Se lanza si el argumento no es un número natural mayor que uno.
    """
    _es_natural_mayor_que_uno(numero)

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
    Devuelve una tupla con todos los números primos menores que el argumento.

    Argumentos:
        numero (int): Límite superior de búsqueda.

    Salida:
        tuple: Tupla con los números primos menores que numero.

    Excepciones:
        TypeError: Se lanza si el argumento no es un entero.
    """
    if not isinstance(numero, int) or isinstance(numero, bool):
        raise TypeError("El argumento debe ser un número entero.")

    resultado = []

    for candidato in range(2, numero):
        if esPrimo(candidato):
            resultado.append(candidato)

    return tuple(resultado)


def descompon(numero):
    """
    Devuelve la descomposición en factores primos de un número.

    Argumentos:
        numero (int): Número natural mayor que uno.

    Salida:
        tuple: Tupla con los factores primos de numero ordenados de menor a mayor.

    Excepciones:
        TypeError: Se lanza si el argumento no es un número natural mayor que uno.
    """
    _es_natural_mayor_que_uno(numero)

    factores = []
    resto = numero
    divisor = 2

    while divisor * divisor <= resto:
        while resto % divisor == 0:
            factores.append(divisor)
            resto //= divisor
        divisor = 3 if divisor == 2 else divisor + 2

    if resto > 1:
        factores.append(resto)

    return tuple(factores)


def _contar_factores(factores):
    """
    Cuenta cuántas veces aparece cada factor primo.

    Argumentos:
        factores (tuple): Tupla de factores primos.

    Salida:
        dict: Diccionario cuyas claves son factores primos y cuyos valores son sus exponentes.
    """
    conteo = {}

    for factor in factores:
        if factor in conteo:
            conteo[factor] += 1
        else:
            conteo[factor] = 1

    return conteo


def mcm(*numeros):
    """
    Calcula el mínimo común múltiplo de un número arbitrario de argumentos.

    El cálculo se realiza a partir de la descomposición en factores primos
    de cada uno de los números recibidos.

    Argumentos:
        *numeros (int): Números naturales mayores que uno.

    Salida:
        int: Mínimo común múltiplo de los argumentos.

    Excepciones:
        TypeError: Se lanza si no se proporciona ningún argumento o si alguno
        de ellos no es válido.
    """
    if len(numeros) == 0:
        raise TypeError("Debe proporcionarse al menos un número.")

    maximos = {}

    for numero in numeros:
        factores = descompon(numero)
        conteo = _contar_factores(factores)

        for primo, exponente in conteo.items():
            if primo not in maximos or exponente > maximos[primo]:
                maximos[primo] = exponente

    resultado = 1

    for primo, exponente in maximos.items():
        resultado *= primo ** exponente

    return resultado


def mcd(*numeros):
    """
    Calcula el máximo común divisor de un número arbitrario de argumentos.

    El cálculo se realiza a partir de la descomposición en factores primos
    de cada uno de los números recibidos.

    Argumentos:
        *numeros (int): Números naturales mayores que uno.

    Salida:
        int: Máximo común divisor de los argumentos.

    Excepciones:
        TypeError: Se lanza si no se proporciona ningún argumento o si alguno
        de ellos no es válido.
    """
    if len(numeros) == 0:
        raise TypeError("Debe proporcionarse al menos un número.")

    descomposiciones = []

    for numero in numeros:
        factores = descompon(numero)
        descomposiciones.append(_contar_factores(factores))

    comunes = {}
    primeros_factores = descomposiciones[0]

    for primo in primeros_factores:
        exponente_minimo = primeros_factores[primo]
        aparece_en_todos = True

        for conteo in descomposiciones[1:]:
            if primo not in conteo:
                aparece_en_todos = False
                break
            if conteo[primo] < exponente_minimo:
                exponente_minimo = conteo[primo]

        if aparece_en_todos:
            comunes[primo] = exponente_minimo

    resultado = 1

    for primo, exponente in comunes.items():
        resultado *= primo ** exponente

    return resultado


if __name__ == "__main__":
    doctest.testmod(verbose=True)