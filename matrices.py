def producto_escalar(escalar, vector):
    '''
    (num, vector) -> vector

    >>> producto_escalar(2, [2, 1])
    [4, 2]

    :param escalar:
    :param vector:
    :return:
    '''

    vectorResultado = []
    contador = 0

    for i in vector:
        vectorResultado.append(vector[contador] * escalar)
        contador += 1

    return vectorResultado


def producto_escalar(escalar, vector):
    '''
    (num, vector) -> vector

    >>> producto_escalar(2, [2, 1])
    [4, 2]

    :param escalar:
    :param vector:
    :return:
    '''

    vectorResultado = []
    contador = 0

    while len(vector) > contador:

        vectorResultado.append(vector[contador] * escalar)
        contador += 1

    return vectorResultado
