"""
Manejo de números primos.
Tests unitarios incluidos en la documentación:

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
    Devuelve True si el argumento es primo, False en caso contrario.
    El número debe ser un natural mayor que 1.
    """
    if not isinstance(numero, int) or numero <= 1:
        raise TypeError("El argumento debe ser un número natural mayor que 1")
    
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que el argumento.
    """
    return tuple(n for n in range(2, numero) if esPrimo(n))

def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos del argumento.
    """
    factores = []
    d = 2
    temp = numero
    while temp > 1:
        while temp % d == 0:
            factores.append(d)
            temp //= d
        d += 1
    return tuple(factores)

def _get_factor_counts(numero):
    """Función auxiliar para contar exponentes de factores primos."""
    factores = descompon(numero)
    counts = {}
    for f in factores:
        counts[f] = counts.get(f, 0) + 1
    return counts

def mcd(*numeros):
    """
    Devuelve el máximo común divisor de sus argumentos basándose en
    la descomposición en factores primos (factores comunes al menor exponente).
    """
    if not numeros: return None
    
    # Obtenemos diccionarios de {factor: exponente} para cada número
    all_counts = [_get_factor_counts(n) for n in numeros]
    
    # Los factores comunes deben estar en el primer número y en todos los demás
    common_factors = set(all_counts[0].keys())
    for counts in all_counts[1:]:
        common_factors &= set(counts.keys())
    
    resultado = 1
    for f in common_factors:
        # Tomamos el mínimo exponente de cada factor común
        min_exp = min(counts[f] for counts in all_counts)
        resultado *= (f ** min_exp)
        
    return resultado

def mcm(*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos basándose en
    la descomposición en factores primos (comunes y no comunes al mayor exponente).
    """
    if not numeros: return None
    
    all_counts = [_get_factor_counts(n) for n in numeros]
    
    # Unión de todos los factores primos encontrados
    all_prime_factors = set()
    for counts in all_counts:
        all_prime_factors.update(counts.keys())
        
    resultado = 1
    for f in all_prime_factors:
        # Tomamos el máximo exponente para cada factor
        max_exp = max(counts.get(f, 0) for counts in all_counts)
        resultado *= (f ** max_exp)
        
    return resultado

if __name__ == "__main__":
    import doctest
    doctest.testmod()