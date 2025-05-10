'''
en una escuela de conduccion se tiene un programa que dependiendo de la edad del 
usuario debe mostrar el tipo de licencia a la que tiene derecho
condicion 1: si es menor a 16, entonces no puede conducir.
condicion 2: si es menor a 18, puede obtener un permiso para conducir.
condicion 3: si es menor a 70, puede obtener una licencia estandar.
condicion 4: si es mayor a 70, entonces nesecita una licencia especial
'''

edad = int(input("digita tu edad: "))

if edad <16:
    print("no tienes edad para conducir")

elif edad < 18:
    print("puedes obtener un permiso para conducir")

elif edad <70:
    print("puedes obtener una licencia estandar")

elif edad >70:
    print("nesecitas obtener una licencia especial")
