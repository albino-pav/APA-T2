"""
Módulo para el manejo de números primos.

Incluye funciones para:

- Determinar si un número es primo.
- Obtener todos los primos menores que un número dado.
- Descomponer un número en factores primos.
- Calcular el mínimo común múltiplo (mcm).
- Calcular el máximo común divisor (mcd).

Autor
-----
Oriol López Miret
"""

def esPrimo(numero):
    """
    Devuelve `True` si el numero es primo, y `False` si no lo es.

    Args:
        numero(int): Numero para evaluar.

    Returns:
        bool: `True` si es primo o `False` si no lo es.

    Raises:
        TypeError: Si el numero no es entero y mayor a 2.

    Tests:
        >>> [numero for numero in range(2, 50) if esPrimo(numero)]
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    if numero < 2 or type(numero) != int:
        raise TypeError("Numero | Formato incorrecto,  insertar un numero entero mayor a 1")
    else:
        for num in range(2, numero):
            if numero % num == 0:
                return False
        else:
            return True

def primos(numero):
    """
    Devuelve una tupla con todos los numeros primos menores que su argumento.

    Args:
        numero(int): Numero para evaluar.

    Returns:
        tuple: Tupla de los numeros primos.

    Tests:
        >>> primos(50)
        (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    temporal = []
    
    for num in range(2, numero):
        if esPrimo(num):
            temporal.append(num)
    return tuple(temporal)

def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.

    Args:
        numero(int): Numero para descomponer.

    Returns:
        tuple: Tupla de los numeros primos.

    Tests:
        >>> descompon(36 * 175 * 143)
        (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """
    temporal = []
    iterador = 2
    while iterador != -1:
        if numero // iterador == 1:
            temporal.append(numero)
            iterador = -1
        elif numero % iterador == 0:
            temporal.append(iterador)
            numero = numero // iterador
            iterador = 2
        else:
            iterador += 1
    return tuple(temporal)

def mcm(*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.

    Args:
        *numero(int): Lista de numeros enteros.

    Returns:
        int: MCM de la lista de numeros.

    Tests:
         >>> mcm(90, 14)
        630
        >>> mcm(42, 60, 70, 63)
        1260
    """
    lista = list(descompon(numeros[0]))
    for numero in numeros[1:]:
        listatemp = list(descompon(numero))
        listanueva = []
        copiatemp = lista.copy()
    
        for iterador in listatemp:
            if iterador in copiatemp:
                copiatemp.remove(iterador)
            else:
                listanueva.append(iterador)
        lista.extend(listanueva)
        
        resultado = 1
        for temp in lista:
            resultado *= temp
    
    return resultado

def mcd(*numeros):
    """
    Devuelve el máximo común divisor de sus argumentos.

    Args:
        *numeros (int): Lista de numeros enteros.

    Returns:
        int: MCD de la lista de numeros.
        
    Tests:
        >>> mcd(924, 780)
        12
        >>> mcd(840, 630, 1050, 1470)
        210
    """
    numero1 = numeros[0]

    for numero2 in numeros[1:]:
        lista1 = list(descompon(numero1))
        lista2 = list(descompon(numero2))
        listatemp = []

        for factor in lista1:
            if factor in lista2:
                listatemp.append(factor)
                lista2.remove(factor)

        resultado = 1
        for f in listatemp:
            resultado *= f

        numero1 = resultado

    return numero1

import doctest
doctest.testmod(verbose=True)