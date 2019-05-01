from menu import ingresar_vector

matrices = {}

def leer_matriz():
    '''
    Lee una matriz por teclado

    :return: (list of list of int) la matriz del usuario
    '''

    resultado = []

    while True:
        entrada = input('Desea ingresar una fila? s/n')
        if entrada == 'n':
            break

        resultado.append(ingresar_vector()[1:])
    return resultado

def mostrar_matriz():
    '''
    Mostrar matriz

    :return: (list of list of int) la matriz del usuario
    '''

    print('Sus matrices')
    for matriz in matrices:
        print(matriz, '=')
        for vector in matrices[matriz]:
            print(vector)

def suma_matrices():
    '''
    Sumar matrices

    :return: (list of list of int) la suma de una matriz
    '''

while True:

    MENU = """**********Menu************
    0. Salir
    1. Ingresar Matriz
    2. Ver Matrices1
    ********************************
    """

    seleccion = input(MENU)
    if seleccion == '0':
        print('Suerte')
        break
    elif seleccion == '1':
        nombre = input('Cual es el nombre de una matriz')
        matriz = leer_matriz()
        matrices[nombre] = matriz
    elif seleccion == '2':
        mostrar_matriz()
    else:
        print('Seleccion invalida')