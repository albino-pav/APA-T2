"""

primos.py módulo de manejo de números primos realizado por Hug Feijoo Giralt.

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
    Devuelve True si numero es primo; False si no lo es.
    """

    try:
        if numero %1 != 0 or numero <= 1:
            raise TypeError("Numero debe ser un numero natural mayor que 1")
    except:
        raise TypeError("Numero debe ser un numero natural mayor que 1")

    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1
        
    return True


def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que numero.
    """
    
    tupla_primos = ()
    candidato = 2
    
    while candidato < numero:
        if esPrimo(candidato):
            tupla_primos += (candidato,)
        candidato += 1
        
    return tupla_primos
    

    
def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de numero.
    """
    
    try:
        if numero % 1 != 0 or numero <= 1:
            raise TypeError("El argumento debe ser un número natural y mayor que uno.")
    except:
        raise TypeError("El argumento debe ser un número natural y mayor que uno.")
        
    tupla_factores = ()
    divisor = 2
    resto = numero
    
    while resto > 1:
        if resto % divisor == 0:
            tupla_factores += (divisor,)
            resto //= divisor  
        else:
            divisor += 1
            
    return tupla_factores

def mcm(*numeros):
    """Devuelve el mínimo común múltiplo de un número arbitrario de argumentos."""
    # 1. Descomponemos todos los números en una tupla de tuplas
    descomposiciones = ()
    for n in numeros:
        descomposiciones += (descompon(n),)
        
    # 2. Obtenemos una tupla con todos los factores únicos que existen
    factores_unicos = ()
    for desc in descomposiciones:
        for factor in desc:
            esta = False
            for f in factores_unicos:
                if f == factor:
                    esta = True
            if not esta:
                factores_unicos += (factor,)
                
    # 3. Calculamos el MCM usando la máxima aparición de cada factor
    resultado = 1
    for factor in factores_unicos:
        max_veces = 0
        for desc in descomposiciones:
            # Contamos cuántas veces aparece el factor en esta descomposición
            veces = 0
            for f in desc:
                if f == factor:
                    veces += 1
            if veces > max_veces:
                max_veces = veces
                
        # Multiplicamos el resultado por el factor elevado a 'max_veces'
        contador = 0
        while contador < max_veces:
            resultado *= factor
            contador += 1
            
    return resultado
    
def mcd(*numeros):
    """Devuelve el máximo común divisor de un número arbitrario de argumentos."""
    descomposiciones = ()
    for n in numeros:
        descomposiciones += (descompon(n),)
        
    factores_primer_numero = ()
    for factor in descomposiciones[0]:
        esta = False
        for f in factores_primer_numero:
            if f == factor:
                esta = True
        if not esta:
            factores_primer_numero += (factor,)
            
    resultado = 1
    for factor in factores_primer_numero:
        min_veces = -1  
        
        for desc in descomposiciones:
            veces = 0
            for f in desc:
                if f == factor:
                    veces += 1
            
            if min_veces == -1 or veces < min_veces:
                min_veces = veces
                
        contador = 0
        while contador < min_veces:
            resultado *= factor
            contador += 1
            
    return resultado


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)