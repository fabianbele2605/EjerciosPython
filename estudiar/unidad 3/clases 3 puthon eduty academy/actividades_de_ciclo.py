#solicitar informacion

nombre = input ("nombre completo: ")
materias =5

#hacer un ciclo,pedir datos y sumar la calificacion

contador = 1
sumatoria = 0

while contador <= materias:
    nombre_materia = input("ingresa el nombre de la (" +str(contador) + ")materia: ")
    calificacion = float (input ("calificacion obtenidas en" + str(nombre_materia) + ": "))


#sumar la calificacion sumatoria
    sumatoria = sumatoria + calificacion 

#aumentar el contador para no hacer ciclo infinito
    contador = contador + 1


#hacer calculos e imprimir resultados
promedio = sumatoria / materias  
print ("***RESULTADOS***")
print (f'hola, {nombre} tiene un promedio {promedio} en el 5to semestre. ')