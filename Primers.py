"""
Txell Vilamajó i Puixeu
TASCA 2: APA CURS 2025-2026

Primers.py Mòdul de gestió de nombres primers
"""

def esPrimer(numero):
    """ 
    Retorna True si el nombre és primer i False si no ho és
    
    "Un nombre primer és un nombre natural més gran que 1 que només té dos divisors positius: ell mateix i l'1"

    Test unitari:
    >>> [ numero for numero in range(2, 50) if esPrimer(numero) ]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    
    """
    # Es considera que un numero és un numero natural i major de 1, en cas contrari la funció ha de elevar l'excepció "TypeError" i finalitzar l'execució. 
    if numero <= 1 or type(numero) is not int:
        raise TypeError("El nombre ha de ser enter i > 1")
    # Comprovem si el nombre és primer o no
    for prova in range(2, numero):
        if numero % prova == 0: # Es comrpova si el nombre és divisible entre 2 i tots els nombres enters fins a arribar al numero-1. 
            return False
    # Si no s'ha trobat cap divisor, el numero és primer i la funció ha de retornar True
    return True

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Primers(numero):
    """
    Retorna una tupla amb els numeros primers menors que el seu argument

    Test unitari:
    >>> Primers(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

    """
    Nombres_primers = [] # Creem la llista buida (no podem crear directament una tupla perquè les tuples son immutables)
    for i in range(2, numero):
        if esPrimer(i)==True:
            Nombres_primers.append(i)
    # Convertim la llista a una tupla
    return tuple(Nombres_primers)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def descompon(numero):
    """
    Retorna una tupla amb la descomposició en factors primers del seu argument

    Test unitari:
    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """
    descomposicio_factors = [] # Creem la llista buida (no podem crear directament una tupla perquè les tuples son immutables)
    divisor = 2  # El 2 és el primer numero primer (comencem la descomposició)
    numero_reduit = numero # Fem una copia per no modificar l'original

    while numero_reduit > 1:  # EL bucle acaba quan s'arriba al final de la descomposició (el nombre val 1)
        while numero_reduit % divisor == 0:
            descomposicio_factors.append(divisor) # Afegim el factor a la llista
            numero_reduit = numero_reduit/divisor #int(numero_reduit/divisor) -->  Ens quedem amb la part entera 
        # Quan el nombre no es pot dividir més pel divisor actual, passem al següent
        divisor+=1
            # No cal que comprovem que el divisor és un nombre primer perquè quan arribem a nombres no primers el while numero_reduit % divisor mai donarà residu 0. Això és degut a qualsevol número compost, com el 4, el 9, el 12... estan format per nombres primers més petits.
    return tuple(descomposicio_factors)  # Retornem en format tupla
               
         
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mcm(numero1, numero2):
    """
    Calcula el MCM (minim comú multiple) de dos numeros a partir de la seva descomposicio en factors

    Necessitem identificar els factors comunis i no comuns i quedar-nos amb l'exponent més gran

    Test Unitari:
    >>> mcm(90, 14)
    630
    """
    # Trobem els factors que formen cada numero. 
    factors1 = descompon(numero1)
    factors2 = descompon(numero2)
    
    factors_totals = [] # Llista per mirar factors comuns i no comuns entre els dos numeros

    for factor in factors1:
        if factor not in factors_totals:
            factors_totals.append(factor)

    for factor in factors2:
        if factor not in factors_totals:
            factors_totals.append(factor)

    # Ara tenim una llista amb tots els factors comuns i no comuns entre els dos numeros.
    # Inicialitzem el resultat a 1
    mcm = 1
    
    # Busquem els exponents de cada factor i trobem el màxim
    for factor in factors_totals:
        comptador_num1 = 0
        for factor1 in factors1:
            if factor1 == factor:
                comptador_num1 += 1

        comptador_num2 = 0
        for factor2 in factors2:
            if factor2 == factor:
                comptador_num2 += 1

        if comptador_num1 > comptador_num2:
            exponent_maxim = comptador_num1
        else:
            exponent_maxim = comptador_num2

        # Multipliquem el resultat de mcm pel factor elevat a l'exponent màxim
        mcm = mcm * (factor ** exponent_maxim)

    return mcm


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def mcd(numero1, numero2):
    """
    Calcula el MCD (maxim comú divisor) de dos numeros a partir de la seva descomposició en factors.

    Necessitem identificar els factors que comparteixen els dos numeros i quedar-nos amb l'exponent més petit
    
    Test unitari:
    >>> mcd(924, 780)
    12
    """
    # Trobem els factors que formen cada numero. 
    factors1 = descompon(numero1)
    factors2 = descompon(numero2)

    factors_comuns = [] #Llista buida per gruadar els factors comuns
    
    for factor in factors1:
        if factor in factors2 and factor not in factors_comuns:
            factors_comuns.append(factor)
                
    # Ara tenim la llista factors_comuns amb tots els factors que comparteixen els dos numeros
    mcd = 1  # Inicialitzem el resultat del mcd
    
    # Necessitem mirar quantes vegades es repateixen a cada número els factors comuns
    for factor in factors_comuns:
        comptador_num1 = 0 # Posem el comptador a 0
        for factor1 in factors1:  # Mentres el factor estigui dins els factors del numero 1
            if factor1 == factor: 
                comptador_num1 += 1

        # Fem el mateix pel numero 2
        comptador_num2 = 0
        for factor2 in factors2:
            if factor2 == factor:
                comptador_num2 += 1

        # Ens hem de quedar amb el d'exponent més petit, comprovem els valors dels comptadors
        if comptador_num1 < comptador_num2:
            exponent_minim = comptador_num1
        else:
            exponent_minim = comptador_num2
        
        mcd = mcd * (factor ** exponent_minim)  # Multipliquem el resultat pel factor elevat a l'exponent mínim

    return mcd


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mcm_numeros(*numeros):
    """
    Retorna el MCM (mínim comú multiple) dels seus arguments (pot tenir més de 2 numeros com a arguments)

    Test unitari:
    >>> mcm_numeros(42, 60, 70, 63)
    1260
    """
    llista_de_nums_descomposats = [] # Per guardar la descomposició de cada numero
    factors_totals = [] # Llista amb els factors comunis i no comuns

    # Primer de tot necessitem descomposar cada numero i fer la llista de factors únics
    for numero in numeros:
        num_descomposat = descompon(numero)
        llista_de_nums_descomposats.append(num_descomposat)
        for factor in num_descomposat:
            if factor not in factors_totals:
                factors_totals.append(factor)

    mcm = 1 # Inicialitzem el resultat a 1, per després poder anar fent la multiplicació

    # Ara per cada factor hem de buscar el màxim exponent  
    for factor in factors_totals:
        exp_max = 0
        # Analitzem la descpomosició de cada numero de l'argument
        for num_descomposat in llista_de_nums_descomposats:
            comptador = 0
            for f in num_descomposat:
                if f == factor:
                    comptador += 1
            if comptador > exp_max:
                exp_max = comptador

        # Actualitzem el valor del mcm
        mcm = mcm * (factor ** exp_max)
        
    return mcm


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mcd_numeros(*numeros):
    """
    Retorna el MCD (maxim comú divisor) dels seus arguments (pot tenir més de 2 numeros com a arguments)

    Test unitari:
    >>> mcd_numeros(840, 630, 1050, 1470)
    210
    """

    llista_de_nums_descomposats = [] # Llista per guardar els numeros descomposats
    factors_comuns = [] # Llista per guardar els factors comuns
    
    for numero in numeros:
        num_descomposat = descompon(numero)
        llista_de_nums_descomposats.append(num_descomposat)

    for factor in llista_de_nums_descomposats[0]:  # Necessitem agafar els factors del primer numero descomposat per comparar
        es_comu = True
        # Mirem si el factor apareix a la descomposicio de la resta de numeros
        for i in range(1, len(llista_de_nums_descomposats)):
            if factor not in llista_de_nums_descomposats[i]:
                es_comu = False  # Si no està a cap dels altres numeros, el factor NO ÉS COMÚ
                break
        if es_comu and factor not in factors_comuns:
            factors_comuns.append(factor)

    mcd = 1 # Inicialitzem el resultat
    for factor in factors_comuns:
        # Calculem l'exponent del primer numero per fer-lo servir de referència
        exp_min = 0
        for f in llista_de_nums_descomposats[0]:
            if f == factor:
                exp_min += 1

        # Calculem l'exponent del següent numero i el comparem amb l'anterior
        for i in range(1, len(llista_de_nums_descomposats)):
            comptador = 0
            for f in llista_de_nums_descomposats[i]:
                if f == factor:
                    comptador += 1
            if comptador < exp_min:
                exp_min = comptador
                
        # Actualitzem el resultat del mcd
        mcd = mcd * (factor ** exp_min)
    return mcd
                

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)