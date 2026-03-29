"""
Tarea de APA 2026: Manejo de números primos
Nombre: Steven Daniel Vizcaino Cedeño

Tests unitarios:
>>> [numero for numero in range(2, 50) if esPrimo(numero)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)
>>> mcd(924, 780)
12
>>> mcm(90, 14)
630
>>> mcd(840, 630, 1050, 1470)
210
>>> mcm(42, 60, 70, 63)
1260
"""

def esPrimo(numero):
    """
    Devuelve True si el argumento es primo.
    Argumento: numero (int) natural > 1.
    Salida: bool.
    """
    if not isinstance(numero, int) or numero <= 1:
        raise TypeError("El argumento debe ser un número natural mayor que 1")
    
    # Un número es primo si no es divisible por ningún número entre 2 y su raíz cuadrada
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primos(numero):
    """Devuelve tupla con primos menores que el argumento."""
    return tuple(n for n in range(2, numero) if esPrimo(n))

def descompon(numero):
    """Devuelve la descomposición en factores primos."""
    factores = []
    d = 2
    temp = numero
    while temp > 1:
        while temp % d == 0:
            factores.append(d)
            temp //= d
        d += 1
    return tuple(factores)

def mcd(*numeros):
    """
    Calcula el MCD de un número arbitrario de argumentos.
    Usa la descomposición en factores primos.
    """
    if not numeros: return None
    
    # Obtenemos los factores del primer número como base
    comunes = list(descompon(numeros[0]))
    
    for num in numeros[1:]:
        factores_num = list(descompon(num))
        nueva_lista_comunes = []
        # Solo nos quedamos con los factores que estén en AMBOS
        for f in comunes:
            if f in factores_num:
                nueva_lista_comunes.append(f)
                factores_num.remove(f) # Evitamos repetir el mismo factor
        comunes = nueva_lista_comunes
        
    # Multiplicamos los factores comunes para obtener el MCD
    resultado = 1
    for f in comunes:
        resultado *= f
    return resultado

def mcm(*numeros):
    """
    Calcula el MCM de un número arbitrario de argumentos.
    Usa la descomposición en factores primos.
    """
    if not numeros: return None
    
    todos_los_factores = {} # Diccionario para guardar el máximo exponente de cada factor
    
    for num in numeros:
        factores = descompon(num)
        # Contamos cuántas veces sale cada factor en este número
        conteo = {}
        for f in factores:
            conteo[f] = conteo.get(f, 0) + 1
        
        # Actualizamos el máximo exponente visto hasta ahora para cada primo
        for f, cantidad in conteo.items():
            if f not in todos_los_factores or cantidad > todos_los_factores[f]:
                todos_los_factores[f] = cantidad
                
    # Multiplicamos cada factor por su máximo exponente
    resultado = 1
    for f, exponente in todos_los_factores.items():
        resultado *= (f ** exponente)
    return resultado
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)