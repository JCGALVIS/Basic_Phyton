vectores = {}

def principal():
    mensaje = '''Seleciones una opciòn:
    0. Salir
    1. Ingresar vector
    2. Mostrar vectore
    3. Producto escalar
    4. Suma de vectores
    5. Producto punto
    6. Mayor elemnto
    7. Menor elemento
    8. Promedio
    9. Desviación estandar
    10. Comparar
    11. Norma
    12. Moda de los elementos de un vector
    '''

    while True:
        opcion = input(mensaje)

        if opcion == '0':
            print('Gracias.')
            break

        elif opcion == '1':
            vector = ingresar_vector()
            vectores[vector[0]] = vector[1:]
        elif opcion == '2':
            mostrar_mensaje()
        elif opcion == '3':
            calcular_producto_escalar()
        elif opcion == '4':
            calcula_suma_producto()
        else:
            print('Selecione una opción valida.')



    print(opcion)

def ingresar_vector():
    '''Perminte leer un vector del usaurio'''
    vector = [input('¿Cual es el nombre de su vector? ')]

    while True:
        num = input('Ingrese su escalar o "s" para terminar ')

        if num.lower() != 's':
            try:
                num = int(num)
                vector.append(num)
            except:
                print(num, ' no es un escalar.')
        else:
            break

    return vector

def mostrar_mensaje():
    for vector in vectores:
        print('Sus vectores son:', vector, vectores[vector] )

def calcular_producto_escalar():
    nombreVector = input('Indique el nombre del vector: ')

    print('El vector', nombreVector, 'contiene', vectores[nombreVector])

    while True:
        escalar = input('Ingrese un escalar ')

        try:
            escalar = int(escalar)
            break
        except:
            print(escalar, ' no es un escalar.')

    print('El producto del escalar es:', producto_escalar(escalar, vectores[nombreVector]))

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

def calcula_suma_producto():

    while True:
        nombreVector1 = input('Indique el nombre del vector 1: ')
        print('El vector 1', nombreVector1, 'contiene', vectores[nombreVector1])

        nombreVector2 = input('Indique el nombre del vector 2: ')
        print('El vector 2', nombreVector2, 'contiene', vectores[nombreVector2])

        if len(vectores[nombreVector1]) == len(vectores[nombreVector2]):
            print('La suma de los vectores es:', suma_producto(vectores[nombreVector1], vectores[nombreVector2]))
            break
        else:
            print('Los vectores seleccionados no tiene la misma longitud.')

def suma_producto(vector1, vector2):
    vectorResultado = []
    contador = 0

    while contador < len(vector1):
        vectorResultado.append(vector1[contador] + vector2[contador])

    return vectorResultado


if __name__ == '__main__':
    principal()
