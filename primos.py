
    
"""

esPrimo(numero)
---------------
>>> [numero for numero in range(2, 50) if esPrimo(numero)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

primos(numero)
--------------
>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

descompon(numero)
-----------------
>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)

mcm(numero1, numero2)
---------------------
>>> mcm(90, 14)
630

mcd(numero1, numero2)
---------------------
>>> mcd(924, 780)
12

mcm(*numeros)
-------------
>>> mcm(42, 60, 70, 63)
1260

mcd(*numeros)
-------------
>>> mcd(840, 630, 1050, 1470)
210
"""

def esPrimo(numero):
    if numero > 1 and type (numero) == int:
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
    else:
        raise TypeError("No es Natural >1")

def primos(numero):
    return tuple(i for i in range(2, numero) if esPrimo(i))

def descompon(numero):
    lista = []
    prims = primos(numero)
    while numero != 1:
        for i in prims:
            if numero % i == 0:
                lista.append(i)
                numero = numero/i
                break
    return tuple(lista)

def frecuencia_factores (factores):
    frecuencias = [0] * (max(factores)+1)
    for i in factores:
        frecuencias[i]+=1
    return frecuencias

def mcm(*numeros):

    
    resultado = 1
    lista_frecuencias = [frecuencia_factores(descompon(numero)) for numero in numeros]

    max_len = max(len(f) for f in lista_frecuencias)

    for i in range(len(lista_frecuencias)):
        if len(lista_frecuencias[i]) < max_len:
            lista_frecuencias[i] += [0] * (max_len - len(lista_frecuencias[i]))

    for primo in range(2, max_len):
        exponente_max = 0
        for f in lista_frecuencias:
            if f[primo] > exponente_max:
                exponente_max = f[primo]
        if exponente_max > 0:
            resultado *= primo ** exponente_max

    return resultado


def mcd(*numeros):
    
    resultado = 1
    lista_frecuencias = [frecuencia_factores(descompon(numero)) for numero in numeros]

    max_len = max(len(f) for f in lista_frecuencias)

    for i in range(len(lista_frecuencias)):
        if len(lista_frecuencias[i]) < max_len:
            lista_frecuencias[i] += [0] * (max_len - len(lista_frecuencias[i]))

    for primo in range(2, max_len):
        exponente_min = None
        for f in lista_frecuencias:
            if exponente_min is None or f[primo] < exponente_min:
                exponente_min = f[primo]
        if exponente_min > 0:
            resultado *= primo ** exponente_min

    return resultado

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    