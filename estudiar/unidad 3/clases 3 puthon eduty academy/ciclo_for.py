#word = input("ingresa una palabra: ")

'''print(word)
print(word)
print(word)
print(word)
print(word)
print(word)
print(word)
print(word)
print(word)
print(word)
'''

'''for i in range (4):
    print(word)
'''

'''print("comienzo")

contador = 1

for i in [3,4,5,7,8]:
    print(f'vuelta numero: {contador}')
    print(f'hola, ahora i vale {i} y su cuadrado es {i ** 2}')
    contador += 1


print('final')
'''

numero = int(input("¿de que numero quieres la tabla de multiplicar? "))
print("")

print(f'tabla de multiplicar del numero {numero}')

for i in range(1, 11):
    print(f'{i} x {numero} = {i*numero}')
