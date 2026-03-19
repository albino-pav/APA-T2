# primos.py
# Guillem Perez Sanchez QP 2024-25

# APA-T2: Manejo de numeros primos

# Determinación de la primalidad y descomposición de un número en factores primos

def esPrimo(numero):
    # Devuelve True si su argumento es primo, y False si no lo es.
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primos(numero): 
    # Devuelve una tupla con todos los números primos menores que su argumento.
    resultado=[]
    for i in range(1,numero-1):
        if esPrimo(i):
            resultado.append(i)
    return tuple(resultado)

def descompon(numero):
    # Devuelve una tupla con la descomposición en factores primos de su argumento.
    resultado = []
    divisor = 2
    while numero > 1:
        if numero % divisor == 0:  # Si es divisible, es un factor primo.
            resultado.append(divisor)
            numero //= divisor  # Divide el número por el divisor.
        else:
            divisor += 1  # Prueba con el siguiente divisor.
    return tuple(resultado)

# Obtención del mínimo común múltiplo y el máximo común divisor

"""
Estas dos funciones deben cumplir las condiciones siguientes:
- Aunque se trate de una solución sub-óptima, en ambos casos 
  deberá partirse de la descomposición en factores primos de 
  los argumentos usando las funciones del apartado anterior.
- Aunque también sea sub-óptimo desde el punto de vista de la 
  programación, ninguna de las dos funciones puede depender de 
  la otra; cada una debe programarse por separado.
"""

def mcm(numero1, numero2): 
    # Devuelve el mínimo común múltiplo de sus argumentos.
    mayor = max(numero1, numero2)  # Empezamos con el mayor de los dos números
    while True:
        if mayor % numero1 == 0 and mayor % numero2 == 0:
            return mayor
        mayor += 1

def mcd(numero1, numero2): 
    # Devuelve el máximo común divisor de sus argumentos.
    while numero2 != 0:
        numero1, numero2 = numero2, numero1 % numero2
    return numero1

# Obtención del mínimo común múltiplo y el máximo común divisor para un número arbitrario de argumentos

def mcmN(*numeros): 
    # Devuelve el mínimo común múltiplo de sus argumentos.
    resultado = 1
    for num in numeros:
        resultado = mcm(resultado,num)
    return resultado

def mcdN(*numeros): 
    # Devuelve el máximo común divisor de sus argumentos.  
    resultado = numeros[0]  # Inicializamos con el primer número
    for num in numeros[1:]:  # Iteramos desde el segundo número en adelante
        resultado = mcd(resultado, num)
    return resultado

# TESTS

# esPrimo(numero): Al ejecutar [ numero for numero in range(2, 50) if esPrimo(numero) ], la salida debe ser [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47].

ans1 = [ numero for numero in range(2, 50) if esPrimo(numero) ]

# primos(numeor): Al ejecutar primos(50), la salida debe ser (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47).

ans2 = primos(50)

# descompon(numero): Al ejecutar descompon(36 * 175 * 143), la salida debe ser (2, 2, 3, 3, 5, 5, 7, 11, 13).

ans3 = descompon(36 * 175 * 143)

# mcm(num1, num2): Al ejecutar mcm(90, 14), la salida debe ser 630.

ans4 = mcm(90,14)

# mcd(num1, num2): Al ejecutar mcd(924, 780), la salida debe ser 12.

ans5 = mcd(924,780)

# mcmN(numeros): Al ejecutar mcm(42, 60, 70, 63), la salida debe ser 1260.

ans6 = mcmN(42,60,70,63)

# mcdN(numeros): Al ejecutar mcd(840, 630, 1050, 1470), la salida debe ser 210.

ans7 = mcdN(840,630,1050,1470)

print(ans1)
print(ans2)
print(ans3)
print(ans4)
print(ans5)
print(ans6)
print(ans7)