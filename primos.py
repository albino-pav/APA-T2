'''
Primos.py modulo de manejo de primos
Roberto Dos Ramos
'''

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
def esPrimo(numero):
    '''
    devuelve True si primo, False si no.(espero) 
    >>> [numero for numero in range(2, 50) if esPrimo(numero)]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    '''
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primos(numero):
    '''
    devuelve una tupla de numeros primos menores que numero
    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    '''
    return tuple(primo for primo in range(2,numero) if esPrimo(primo))

def descompon(n):
    '''
    descompone n en sus factores primos
    escogemos un primo y dividimos a n hasta que el residuo !=0,
    pasamos al siguiente primo hasta que n = 1
    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    '''
    factores = []
    for p in primos(n):
        while n % p == 0:
            factores.append(p)
            n = n // p
        if n == 1:
            break
    return tuple(factores)

def mcm(*numeros):
    '''
    >>> mcm(90, 14)
    630
    >>> mcm(42, 60, 70, 63)
    1260
    '''
    factores = []
    for n in numeros:
        factores += list(descompon(n))
    
    unicos = set(factores)
    resultado = 1
    for f in unicos:
        resultado *= f ** max(descompon(n).count(f) for n in numeros)
    return resultado

def mcd(*numeros):
    '''
    >>> mcd(924, 780)
    12
    >>> mcd(840, 630, 1050, 1470)
    210
    '''
    factores = []
    for n in numeros:
        factores += list(descompon(n))
    
    unicos = set(factores)
    resultado = 1
    for f in unicos:
        resultado *= f ** min(descompon(n).count(f) for n in numeros)
    return resultado

import doctest
doctest.testmod(verbose=True)