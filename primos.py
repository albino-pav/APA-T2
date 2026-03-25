"""
primos.py
Autor: Saül Muñoz Rodríguez

Módulo con funciones básicas para trabajar con números primos.

Incluye:
- esPrimo(numero): determina si un número es primo.
- primos(numero): devuelve una tupla con los primos menores que numero.
- descompon(numero): devuelve la descomposición en factores primos.
- mcd(*numeros): devuelve el maximo comun divisor de cualquier grupo de numeros.
- mcm(*numeros): devuelve el minimo comun multiplo de cualquier grupo de numeros.

Tests:
>>> [numero for numero in range(2, 50) if esPrimo(numero)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)

>>> mcd(924, 780)
12
    
>>> mcd(840, 630, 1050, 1470)
210

>>> mcm(90, 14)
630
    
>>> mcm(42, 60, 70, 63)
1260

"""

def esPrimo(numero):
    """
    Devuelve True si 'numero' es primo y False si no.

    >>> [numero for numero in range(2, 50) if esPrimo(numero)]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    """
    if not isinstance(numero, int) or numero <= 1:
        raise TypeError("El número debe ser un entero mayor que 1")

    for prueba in range(2, numero):
        if numero % prueba == 0:
            return False
    return True


def primos(numero):
    """
    Devuelve una tupla con todos los numeros primos menores que su argumento

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

    """
    if not isinstance(numero, int) or numero <= 1:
        raise TypeError("El número debe ser un entero mayor que 1")

    lista = []

    for candidato in range(2, numero):
        if esPrimo(candidato):
            lista.append(candidato)

    primosMenores = tuple(lista)
    return primosMenores
    
def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento
    
    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    
    """ 
    if not isinstance(numero, int) or numero <= 1:
        raise TypeError("El número debe ser un entero mayor que 1")

    factores = ()
    divisor = 2

    while numero > 1:
        if numero % divisor == 0:
            factores = factores + (divisor,)
            numero = numero // divisor
        else:
            divisor += 1

    return factores
 
def mcd(*numeros):
    """
    Devuelve el máximo común divisor de sus argumentos usando factores primos

    >>> mcd(924, 780)
    12
    
    >>> mcd(840, 630, 1050, 1470)
    210
    
    """
    if len(numeros) < 2:
        raise TypeError("Debe proporcionar al menos dos números")

    factores_comunes = list(descompon(numeros[0]))

    for n in numeros[1:]:
        factores_n = list(descompon(n))
        nuevos_comunes = []
        for f in factores_comunes:
            if f in factores_n:
                nuevos_comunes.append(f)
                factores_n.remove(f)
        factores_comunes = nuevos_comunes

    resultado = 1
    for f in factores_comunes:
        resultado *= f

    return resultado

    
def mcm(*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos usando factores primos

    >>> mcm(90, 14)
    630
    
    >>> mcm(42, 60, 70, 63)
    1260
    
    """
    if len(numeros) < 2:
        raise TypeError("Debe proporcionar al menos dos números")

    factores_totales = []

    for n in numeros:
        factores_n = list(descompon(n))
        temp = factores_totales.copy()
        for f in factores_n:
            if f in temp:
                temp.remove(f)
            else:
                factores_totales.append(f)

    resultado = 1
    for f in factores_totales:
        resultado *= f

    return resultado

    

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)