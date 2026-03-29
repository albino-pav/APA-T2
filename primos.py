"""
Módulo para el manejo de números primos, cálculo del MCM y MCD.
Alumno: Fulano Mengano Zutano

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
    """Evalúa si un argumento (int) es un número natural primo, devolviendo un bool."""
    if not isinstance(numero, int) or numero <= 1:
        raise TypeError("El argumento debe ser un número natural mayor que uno.")
    # all() devuelve True solo si ninguna división da resto 0
    return all(numero % i != 0 for i in range(2, int(numero**0.5) + 1))

def primos(numero):
    """Devuelve una tupla con todos los números primos menores que el argumento (int)."""
    return tuple(i for i in range(2, numero) if esPrimo(i))

def descompon(numero):
    """Devuelve una tupla con la descomposición en factores primos del argumento (int)."""
    factores = []
    d = 2
    while numero > 1:
        while numero % d == 0:
            factores.append(d)
            numero //= d
        d += 1
    return tuple(factores)

def mcm(*numeros):
    """Devuelve el MCM (int) de argumentos arbitrarios usando su descomposición prima."""
    if not numeros: return 1
    descomposiciones = [descompon(n) for n in numeros]
    factores_unicos = set(f for d in descomposiciones for f in d)
    
    resultado = 1
    for f in factores_unicos:
        # Buscamos el exponente máximo de este factor entre todos los números
        resultado *= f ** max(d.count(f) for d in descomposiciones)
    return resultado

def mcd(*numeros):
    """Devuelve el MCD (int) de argumentos arbitrarios usando su descomposición prima."""
    if not numeros: return 1
    descomposiciones = [descompon(n) for n in numeros]
    factores_base = set(descomposiciones[0])
    
    resultado = 1
    for f in factores_base:
        # Buscamos el exponente mínimo de este factor común entre todos los números
        resultado *= f ** min(d.count(f) for d in descomposiciones)
    return resultado

if __name__ == "__main__":
    import doctest
    doctest.testmod()