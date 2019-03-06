def esParentesis(caracter):
    '''
    (str of len == 1) -> str

    >>> esParentesis('(')
    'Es paréntesis'

    >>> esParentesis('k')
    'No es paréntesis'

    >>> esParentesis('kd')
    Traceback (most recent call last):
    ..
    TypeError: kd no es un parentesis

    :param caracter:
    :return:
    '''

    lenCaracter = len(caracter)

    if(lenCaracter != 1):
        raise TypeError(str(caracter) + ' no es un parentesis')
    elif(caracter == '(' or caracter == ')'):
        return 'Es paréntesis'
    else:
        return 'No es paréntesis'

def division(dividendo, divisor):
    '''
    (num, num) -> num

    >>> division(4, 2)
    2.0

    >>> division(15, 3)
    5.0

    >>> division(5, 0)
    Traceback (most recent call last):
    ..
    ZeroDivisionError: La división en cero no es posible

    >>> division('ds', 5)
    Traceback (most recent call last):
    ..
    TypeError: ds no es numerico

    >>> division(30, 'asde')
    Traceback (most recent call last):
    ..
    TypeError: asde no es numerico

    :param divisor:
    :param dividendo:
    :return:
    '''

    if (type(dividendo) != float  and type(dividendo) != int):
        raise TypeError(str(dividendo) + ' no es numerico')
    elif (type(divisor) != float and type(divisor) != int):
        raise TypeError(str(divisor) + ' no es numerico')
    elif (divisor == 0):
       raise ZeroDivisionError('La división en cero no es posible')
    else:
        return dividendo / divisor

def esDobleDeUnImpar(numero):
    '''
    (num of type == int) -> str

    >>> esDobleDeUnImpar(14)
    '14 es doble de 7, que es impar'

    >>> esDobleDeUnImpar(2.6)
    Traceback (most recent call last):
    ..
    TypeError: 2.6 no es entero

    >>> esDobleDeUnImpar('asd')
    Traceback (most recent call last):
    ..
    TypeError: asd no es entero


    :param mumero:
    :return:
    '''


    if (type(numero) != int):
        raise TypeError(str(numero) + ' no es entero')
    else:
        impar = numero / 2

        if (impar % 2) != 0:
            return str(numero) + ' es doble de ' + str(int(impar)) + ', que es impar'