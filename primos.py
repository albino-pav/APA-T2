"""
    Determinación de la primalidad y mínimo común múltiplo y máximo común divisor
"""

def esPrimo(numero):
    """
    Devuelve True si su argumento es primo, y False si no lo es.
    >>> esPrimo(13)
    True
    """
    if numero <= 1: 
        return False

    for i in range(2,int(numero**0.5) + 1):
        if numero%i == 0:
            return False
    return True

def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que su argumento.
    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    
    if numero <= 1: 
        return False
    
    return tuple([i for i in range(2,numero) if esPrimo(i)])


def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.  
    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """

    if esPrimo(numero):
        return (numero, )

    lista = []
    for i in primos(numero):
        while numero % i == 0:
            lista.append(i)
            numero /= i
            
    return tuple(lista)

def mcm(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    >>> mcm(90, 14)
    630
    """
    if numero1 <= 1 or esPrimo(numero1):
        if numero1 in descompon(numero2):
            return numero2
        else:
            return numero1*numero2
        
    if numero2 <= 1 or esPrimo(numero2):
        if numero2 in descompon(numero1):
            return numero1
        else:
            return numero1*numero2
        
    exponentes1 = {}
    exponentes2 = {}

    for i in descompon(numero1):
        if i in exponentes1:
            exponentes1[i] += 1
        else:
            exponentes1[i] = 1

    for i in descompon(numero2):
        if i in exponentes2:
            exponentes2[i] += 1
        else:
            exponentes2[i] = 1

    tot = 1

    for k in exponentes1:
        if k in exponentes2:
            if exponentes1[k] > exponentes2[k]:
                tot *= k**exponentes1[k]
            else:
                tot *= k**exponentes2[k]
        else:
            tot *= k**exponentes1[k]

    for k in exponentes2:
        if k not in exponentes1:
            tot *= k**exponentes2[k]

    return tot


def mcd(numero1, numero2): 
    """
    Devuelve el máximo común divisor de sus argumentos.
    >>> mcd(924, 780)
    12
    """
    componentes1 = {}
    componentes2 = {}

    for key in descompon(numero1):
        if key in componentes1:
            componentes1[key] += 1
        else:
            componentes1[key] = 1

    for key in descompon(numero2):
        if key in componentes2:
            componentes2[key] += 1
        else:
            componentes2[key] = 1
    
    tot = 1

    for key in componentes1:
        if key in componentes2:
            if componentes1[key] < componentes2[key]:
                tot *= key**componentes1[key]
            else:
                tot *= key**componentes2[key]

    return tot

def mcmN(*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    >>> mcmN(42, 60, 70, 63)
    1260
    """
    acumulado = numeros[0]

    for numero in numeros[1:]:
        acumulado = mcm(acumulado,numero)

    return acumulado

def mcdN(*numeros): 
    """
    Devuelve el máximo común divisor de sus argumentos.
    >>> mcdN(840, 630, 1050, 1470)
    210
    """
    acumulado = numeros[0]

    for numero in numeros[1:]:
        acumulado = mcd(acumulado,numero)

    return acumulado

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)