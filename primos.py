
def esPrimo(numero):
    """
    esPrimo devuelve True si el numero introducido es 
    primo o False en caso contrario

    >>> esPrimo(1023)
    False

    >>> esPrimo(1021)
    True
    """
    for prova in range(2, numero):
        if numero % prova == 0:
            return False
    return True    

def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que su argumento.

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    
    if numero <= 1: 
        return False
    
    return tuple([i for i in range(2,numero) if esPrimo(i)])

def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.  

    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """
    lista = []
    divisor = 2
    while divisor * divisor <= numero:
      while numero % divisor == 0:
         lista.append(divisor)
         numero //= divisor
      divisor += 1
    if numero > 1:
        lista.append(numero)
    return tuple(lista)
  

def mcm(num1, num2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos

    >>> mcm(90, 14) 
    630
    """
    factores_1 = list(descompon(num1))
    factores_2 = list(descompon(num2))

    mcm = 1

    for i in factores_1:
        if i in factores_2:
            mcm *= i
            factores_2.remove(i)
        else:
            mcm *= i


    for i in factores_2:
        mcm *= i

    return mcm

def mcd(num1, num2):
    """
    Devuelve el máximo común divisor de sus argumentos

    >>> mcd(924, 780)
    12
    """
    factores_1 = list(descompon(num1))
    factores_2 = list(descompon(num2))

    mcd = 1

    for i in factores_1:
        if i in factores_2:
            factores_2.remove(i)
            mcd *= i
    
    return mcd


def mcmN(*numeros):
    """
    Calcula el mínimo común múltiplo para un número arbitrario de argumentos

    >>> mcmN(42, 60, 70, 63)
    1260
    """
    if not numeros:
        return 1
    resultado = numeros[0]
    for numero in numeros[1:]:
        resultado = mcm(resultado, numero)
    return resultado

def mcdN(*numeros):
    """
    Devuelve el máximo común divisor para un número arbitrario de argumentos

    >>> mcdN(840, 630, 1050, 1470)
    210
    """   
    if not numeros:
        return 1
    resultado = numeros[0]
    for numero in numeros[1:]:
        resultado = mcd(resultado, numero)
    return resultado

   

if __name__ == "__main__":
    import doctest
    doctest.testmod()
