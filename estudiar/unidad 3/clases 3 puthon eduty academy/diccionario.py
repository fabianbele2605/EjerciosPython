'''

#primera forma de crear un diccionario

diccionario = {
    "nombre": "sara",
    "edad": 28,
    "documento": 456234 
}

print(diccionario)

#segunda forma de crear un diccionario

diccionario_segunda_forma = dict(nombre='paola',
                                 edad=37,
                                 documento=2394534)

print(diccionario_segunda_forma)

#tercera forma de crear un 

diccionario_tercera_forma = dict([
    ('nombre', 'jose'),
    ('edad', 37),
    ('documento', 232345)
])

print(diccionario_tercera_forma)
'''

inventario = {"Manzanas": 235, "Peras": 400, "Naranjas": 250, "Sandias": 500}

#inventario.keys()
#inventario.values()

print(inventario.items())