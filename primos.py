'''
Primos.py modulo de manejo de primos
'''

from sympy import isprime

def esPrimo(numero):
    '''
    devuelve True si primo, False si no. 
    
    >>> import primos
    >>> primos.esPrimo(91)
    False
    '''
    return isprime(numero)

import doctest
doctest.testmod()