'''
crear una tupla con numeros,luego pedir un numero por teclado y indicar
 cuantas veces se repite
'''

numeros = (5,6,8,9,5,5,4,5,6,5,29,14,75)

numero = int(input("dame un numero: "))

#print("El numero se repite: " + str(numeros.count(numero)) + " veces.")

print("el numero "+ str(numero) + " se encuentra en el indice: " +str(numeros.index(numero)))


