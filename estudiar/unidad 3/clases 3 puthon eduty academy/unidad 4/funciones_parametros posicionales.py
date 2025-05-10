'''def suma(*args):
    s = 0
    for arg in args:
        s += arg
    return s


resultado = suma(10,45,)

print(resultado)


def lenguaje(nombre, *lenguajes):
    print(f'hola {nombre}')
    print(f'tus lenguajes favoritos son: {lenguajes}')

lenguaje("fabian", "python", "java", "php")    
'''

def lenguaje(nombre, **kwargs):
    print(f'hola {nombre}')
    print("buscando informacion de tus lenguajes favoritos...")
    print("cargando informacion... \n")

    print("informacion: ")
    contador = 0

    print(type(kwargs))
    
    for clave in kwargs:
        contador += 1
        print(f'tu {contador} lenguaje favorito es: {kwargs[clave]}')

lenguaje("luis", lenguaje1 = "python", lenguaje2 = "java", lenguaje3 = "php")
