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
        
 def desgloseMinimoBilletes(valor):
    '''
    num -> str

    >>> desgloseMinimoBilletes(434)
    2 billetes de 200 euros.
    1 billetes de 20 euros.
    1 billetes de 10 euros.
    2 monedas de 2 euros.

    :param valor:
    :return:
    '''

    mensaje = ''

    if (valor // 500) != 0:
        mensaje += str((valor // 500)) + ' billetes de 500 euros.'
        mensaje += '\n'
        valor = valor - (valor // 500) * 500

    if (valor // 200) != 0:
        mensaje += str((valor // 200)) + ' billetes de 200 euros.'
        mensaje += '\n'
        valor = valor - (valor // 200) * 200

    if (valor // 100) != 0:
        mensaje += str((valor // 100)) + ' billetes de 100 euros.'
        mensaje += '\n'
        valor = valor - (valor // 100) * 100

    if (valor // 50) != 0:
        mensaje += str((valor // 50)) + ' billetes de 50 euros.'
        mensaje += '\n'
        valor = valor - (valor // 50) * 50

    if (valor // 20) != 0:
        mensaje += str((valor // 20)) + ' billetes de 20 euros.'
        mensaje += '\n'
        valor = valor - (valor // 20) * 20

    if (valor // 10) != 0:
        mensaje += str((valor // 10)) + ' billetes de 10 euros.'
        mensaje += '\n'
        valor = valor - (valor // 10) * 10

    if (valor // 5) != 0:
        mensaje += str((valor // 5)) + ' billetes de 5 euros.'
        mensaje += '\n'
        valor = valor - (valor // 5) * 5

    if (valor // 2) != 0:
        mensaje += str((valor // 2)) + ' monedas de 2 euros.'
        mensaje += '\n'
        valor = valor - (valor // 2) * 2

    if (valor // 1) != 0:
        mensaje += str((valor // 1)) + ' monedas de 1 euros.'
        valor = valor - (valor // 1) * 1

    print('%s' % mensaje.rstrip('\n'))

        if (impar % 2) != 0:
            return str(numero) + ' es doble de ' + str(int(impar)) + ', que es impar'
