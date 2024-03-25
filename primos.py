"""
Joel Joan Morera | Gerard Cots
"""


def esPrimo(numero) -> bool:
    if numero <= 1:
        return False
    for value in range(2, int(numero**0.5) + 1):
        if numero % value == 0:
            return False
    return True


def primos(numero) -> tuple:
    return tuple(num for num in range(2, numero) if esPrimo(num))


def descompon(numero) -> tuple:
    tuple_ = []
    for valor in primos(numero):
        while numero % valor == 0:
            tuple_.append(valor)
            numero //= valor
    return tuple(tuple_)


def list_product(llista) -> int:
    producto = 1
    for factor in llista:
        producto *= factor
    return producto


def remove_same(llista1, llista2) -> list:
    for factor in llista1:
        if factor in llista2:
            llista2.remove(factor)
    return llista2 


def same_factors(llista1, llista2) -> list:
    factores_comunes = []
    for factor in llista1:
        if factor in llista2:
            factores_comunes.append(factor)
            llista2.remove(factor)
    return factores_comunes


def mcm(numero1, numero2) -> int:
    factores_primos_num1 = list(descompon(numero1))
    factores_primos_num2 = list(descompon(numero2))
  
    factores_mcm = (factores_primos_num1 
                    + remove_same(factores_primos_num1, factores_primos_num2))
    return list_product(factores_mcm)


def mcd(numero1, numero2) -> int:
    factores_primos_num1 = list(descompon(numero1))
    factores_primos_num2 = list(descompon(numero2))
    return list_product(same_factors(factores_primos_num1, 
                                     factores_primos_num2))


def mcmN(*argumentos) -> int:
    factores_mcm = []
    for num in argumentos:
        factores_mcm += remove_same(factores_mcm, list(descompon(num)))

    return list_product(factores_mcm)


def mcdN(*argumentos) -> int:
    factores_mcd = list(descompon(argumentos[0]))
    for num in argumentos:
        factores_num = list(descompon(num))
        factores_mcd = same_factors(factores_mcd, factores_num)
    
    return list_product(factores_mcd)



    


        
