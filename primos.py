"""
Primos: funciones para trabajar con números primos.
Lulu Armoire Palomar

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
    Determina si un número es primo.
    
    Argumentos:
        numero (int): Número natural más grande que 1.
    
    Salida:
        bool: Devolvera True si es primo o False si no lo es.
    """ 
    # Comprovar si es un entero mayor a 1.
    if not isinstance(numero, int):
        raise TypeError("El argumento tiene que ser un número entero")
    if numero <= 1:
        raise TypeError("El argumento tiene que ser un número mayor a 1")

    # Ayuda a la eficiencia
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False 

    # Buscamos divisores impares. Empezamos en el 3 y vamos de 2 en 2 hasta la raíz cuadrada.
    i = 3
    while i * i <= numero:
        if numero % i == 0:
            return False
        i += 2
    return True 
    

def primos(numero):
    """
        Nos devuelve una tupla con todos os números primos más pequeños que el argumento.

        Argumentos:
        numero (int): Límite superior.
        
    Salida:
        tuple: Tupla con los números primos menores al argumento.
    """
    # Comprovar si es un entero mayor a 1.
    if not isinstance(numero, int):
        raise TypeError("El argumento tiene que ser un número entero")
    if numero <= 2:
        raise TypeError("El argumento tiene que ser mayor a 2")

    lista_primos = []
    for i in range(2, numero):
        if esPrimo(i):
            lista_primos.append(i)

    return tuple(lista_primos)


def descompon(numero):
    """
    Devuelve la tupla con la descomposición en factores primos de su argumento.
    Argumentos:
        numero (int): Número a descomponer (mayor a 1).
        
    Salida:
        tuple: Tupla con los factores primos.
    """
    
     # Comprovar si es un entero mayor a 1.
    if not isinstance(numero, int):
        raise TypeError("El argumento tiene que ser un número entero")
    if numero <= 1:
        raise TypeError("El argumento tiene que ser mayor a 1")

    factores = []
    n = numero
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        divisor += 1 if divisor == 2 else 2 # Despues del 2 probamos solo con impares

    if n > 1:
        factores.append(n)

    return tuple(factores)
    
def mcm(*numeros):
    """
    Calcula el mínimo común múltiplo de un número arbitrario de argumentos.
    
    Argumentos:
        *numeros (tuple): Números enteros más grandes que 1.
    
    Salida:
        int: Mínimo común múltiplo de todos los números.
    """
    # Comprobamos que haya al menos un argumento
    if len(numeros) == 0:
        raise TypeError("Necesitamos al menos un argumento")
    
    # Comprobamos que todos los argumentos son enteros más grandes que 1
    for n in numeros:
        if not isinstance(n, int):
            raise TypeError("Todos los argumentos tienen que ser números enteros")
        if n <= 1:
            raise TypeError("Todos los argumentos tienen que ser mayores que 1")
    
    todas_descomposiciones = []
    for n in numeros:
        todas_descomposiciones.append(list(descompon(n)))
        
    # Agrupamos todos los factores diferentes que aparecen
    factores_unicos = set()
    for lista in todas_descomposiciones:
        for factor in lista:
            factores_unicos.add(factor)
    
    factores_mcm = []
    
    for factor in factores_unicos:
        max_veces = 0
        for lista in todas_descomposiciones:
            veces = lista.count(factor)
            if veces > max_veces:
                max_veces = veces
        
        for _ in range(max_veces):
            factores_mcm.append(factor)
    
    resultado = 1
    for factor in factores_mcm:
        resultado = resultado * factor
    
    return resultado

def mcd(*numeros):
    """
    Calcula el máximo común divisor de un número arbitrario de argumentos.
    
    Argumentos:
        *numeros (tuple): Números enteros más grandes que 1.
    
    Salida:
        int: Máximo común divisor de todos los números.
    """
    # Comprobamos que haya al menos un argumento
    if len(numeros) == 0:
        raise TypeError("Necesitamos al menos un argumento")
    
    # Comprobamos que todos los argumentos son enteros más grandes que 1
    for n in numeros:
        if not isinstance(n, int):
            raise TypeError("Todos los argumentos tienen que ser números enteros")
        if n <= 1:
            raise TypeError("Todos los argumentos tienen que ser mayores que 1")
    
    todas_descomposiciones = []
    for n in numeros:
        todas_descomposiciones.append(list(descompon(n)))
    
    # PBuscamos los factores comunes a todos los números
    factores_comunes = todas_descomposiciones[0].copy()
    
    for i in range(1, len(todas_descomposiciones)):
        nuevos_comunes = []
        for factor in factores_comunes:
            if factor in todas_descomposiciones[i]:
                nuevos_comunes.append(factor)
                todas_descomposiciones[i].remove(factor)
        factores_comunes = nuevos_comunes
    
    resultado = 1
    for factor in factores_comunes:
        resultado = resultado * factor
    
    return resultado

    
