'''
add // Añade un elemento al final del conjunto
clear // elimina toda la informacion del conjunto
pop // devuelve y elimina un elemento arbitrario o devuelve un error si esta vacio
remove // intenta eliminar un elemento del conjunto, si no existe eleva un error 
union // devuelve un conjunto con todos los elementos de ambos conjuntos 
'''

#1 forma de crear conjunto
alumnos = {"andrea", "ruby", "marcos", "jose", "marlon"}

#print(alumnos)

#2 forma de crear conjunto
lenguajes = set(["php", "java", "c", "python"])
#print(lenguajes)

#lenguajes.add("c#")
#lenguajes.clear()
#lenguajes.pop()
#lenguajes.remove("java")

todos = alumnos.union(lenguajes)

print(todos)