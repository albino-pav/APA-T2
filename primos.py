"""

Alumno: Xavi Fernandez Rodriguez

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
    """
    Evalúa si un número dado es primo.
    
    Argumentos:
    numero -- Un número natural mayor que 1.
    
    Devuelve:
    True si el número es primo, False en caso contrario.
    
    Excepciones:
    TypeError -- Si el argumento no es un número entero o es menor o igual a 1.
    """
    if not isinstance(numero, int) or numero <= 1:
        raise TypeError("El argumento debe ser un número natural mayor que uno.")
    
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


def primos(numero):
    """
    Calcula todos los números primos menores que un valor dado.
    
    Argumentos:
    numero -- El límite superior (exclusivo) para buscar números primos.
    
    Devuelve:
    Una tupla con todos los números primos menores que el argumento.
    """
    return tuple(i for i in range(2, numero) if esPrimo(i))


def descompon(numero):
    """
    Calcula la descomposición en factores primos de un número.
    
    Argumentos:
    numero -- Número natural a descomponer.
    
    Devuelve:
    Una tupla con la secuencia de factores primos en orden ascendente.
    """
    factores = []
    divisor = 2
    n = numero
    
    while n > 1:
        if n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        else:
            divisor += 1
            
    return tuple(factores)


def mcm(*numeros):
    """
    Calcula el mínimo común múltiplo (MCM) de una cantidad arbitraria de números.
    Se basa en la descomposición de factores primos (sub-óptimo según el enunciado).
    
    Argumentos:
    *numeros -- Una secuencia arbitraria de números enteros.
    
    Devuelve:
    El mínimo común múltiplo de todos los argumentos pasados.
    """
    factores_maximos = {}
    
    for num in numeros:
        factores = descompon(num)
        # Contamos cuántas veces aparece cada factor en el número actual
        conteo_actual = {f: factores.count(f) for f in set(factores)}
        
        # Nos quedamos con el exponente máximo para cada factor primo
        for factor, cantidad in conteo_actual.items():
            if factor in factores_maximos:
                factores_maximos[factor] = max(factores_maximos[factor], cantidad)
            else:
                factores_maximos[factor] = cantidad
                
    resultado = 1
    for factor, cantidad in factores_maximos.items():
        resultado *= (factor ** cantidad)
        
    return resultado


def mcd(*numeros):
    """
    Calcula el máximo común divisor (MCD) de una cantidad arbitraria de números.
    Se basa en la descomposición de factores primos sin depender de la función mcm.
    
    Argumentos:
    *numeros -- Una secuencia arbitraria de números enteros.
    
    Devuelve:
    El máximo común divisor de todos los argumentos pasados.
    """
    if not numeros:
        return 1
        
    # Inicializamos los factores comunes con la descomposición del primer número
    factores_comunes = {}
    factores_iniciales = descompon(numeros[0])
    for f in set(factores_iniciales):
        factores_comunes[f] = factores_iniciales.count(f)
        
    # Intersectamos con los factores de los siguientes números (exponente mínimo)
    for num in numeros[1:]:
        factores = descompon(num)
        conteo_actual = {f: factores.count(f) for f in set(factores)}
        
        nuevos_comunes = {}
        for factor, cantidad in factores_comunes.items():
            if factor in conteo_actual:
                nuevos_comunes[factor] = min(cantidad, conteo_actual[factor])
                
        factores_comunes = nuevos_comunes
        
    resultado = 1
    for factor, cantidad in factores_comunes.items():
        resultado *= (factor ** cantidad)
        
    return resultado


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)