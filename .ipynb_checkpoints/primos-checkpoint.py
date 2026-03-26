"""
primos.py

Modulo para manejar numeros primos.

Test:

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
    Funcion que comprueba si el numero es primo o no.

    Si numero es primo devuelve True,
    En caso contrario devuelve False.

    numero solo puede ser entero y mayor que uno.
    """

    if not isinstance(numero, int) or numero <= 1:
        raise TypeError('La entrada tiene que ser un numero entero y mayor que uno.')
        
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    
    else:
        return True

def primos(numero):
    """
    Funcion que devuelve una tupla con todos los primos por debajo de ese numero.

    numero solo puede ser positivo y mayor que dos.
    """

    if numero < 2 or not isinstance(numero, (int, float)):
        raise TypeError('La entrada tiene que ser un numero igual o mayor que dos.')
    
    resultado = []

    for i in range(2, int(numero) + 1):
        if esPrimo(i):
            resultado.append(i)

    return tuple(resultado)

def descompon(numero):
    """
    Funcion que devuelve la descomposicion en factores primos de numero.

    numero solo puede ser entero y mayor a uno.
    """

    if not isinstance(numero, int) or numero <= 1:
        raise TypeError('La entrada tiene que ser un numero entero y mayor que uno.')

    if esPrimo(numero):
        return (numero,)

    else:        
        resultado = []
        divisor = 2

        while numero > 1:
            if numero % divisor == 0:
                resultado.append(divisor)
                numero //= divisor
            else:
                divisor += 1

        return tuple(resultado)


def mcd2(numero1, numero2):
    """
    Funcion donde entras 2 numeros y te devuelve el maximo comun divisor

    numero1 y numero2 solo pueden enteros mayores que dos ambos.
    """

    if (not isinstance(numero1, int) or numero1 <= 1 or
        not isinstance(numero2, int) or numero2 <= 1):
        raise TypeError('Las entradas tiene que ser un numero entero y mayor que uno.')

    n = list(descompon(numero1))
    m = list(descompon(numero2))

    resultado = 1

    for i in n:
        if i in m:
            resultado *= i
            m.remove(i)
            
    return resultado

def mcm2(numero1, numero2):
    """
    Funcion donde entras 2 numeros y te devuelve el minimo comun multiplo

    numero1 y numero2 solo pueden enteros mayores que dos ambos.
    """

    if (not isinstance(numero1, int) or numero1 <= 1 or
        not isinstance(numero2, int) or numero2 <= 1):
        raise TypeError('Las entradas tiene que ser un numero entero y mayor que uno.')

    n = list(descompon(numero1))
    m = list(descompon(numero2))

    resultado = 1

    for i in n:
        resultado *= i
        if i in m:
            m.remove(i)

    for i in m:
        resultado *= i

    return resultado

def mcd(* numeros):
    """
    Funcion donde entras varios numeros y te devuelve el maximo comun divisor

    numero1 y numero2 solo pueden enteros mayores que dos ambos.
    """
    if len(numeros) < 2:
        raise TypeError('Debes introducir al menos dos numeros.')

    resultado = numeros[0]

    for n in numeros[1:]:
        resultado = mcd2(resultado, n)

    return resultado

def mcm(*numeros):
    """
    Funcion donde entras varios numeros y te devuelve el minimo comun multiplo

    numero1 y numero2 solo pueden enteros mayores que dos ambos.
    """
    
    if len(numeros) < 2:
        raise TypeError('Debes introducir al menos dos numeros.')

    resultado = numeros[0]

    for n in numeros[1:]:
        resultado = mcm2(resultado, n)

    return resultado

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)
    