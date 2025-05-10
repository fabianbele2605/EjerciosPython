'''def es_par(numero):
    if numero % 2 == 0:
        print(f'el numero {numero} es par')
    else:
        print(f'el numero {numero} es impar')

es_par(15)


def saludar(nombre):
    print("hola " + nombre + " eres el mejor programadror")

saludar("mario")


def resta(a = None, b = None):
    if a == None or b == None:
        print("Error, debes enviar dos numeros a la funciones")
        return
    return a-b

resultado = resta(9,6)

print(resultado)
'''

def multiplicacion(numero = None):
    if numero == None:
        print("por favor, introduce un numero")
    else:
        print(f'TABLA DE MULTIPLICAR DEL {numero}')
        for i in range(1,11):
            print(f'{i} x {numero} = {i * numero}')

multiplicacion(5)                