#solicita informacion

nombre = input("ingrese el numero del cliente")
valor_compra = float(input("ingrese el valoe de la compra"))

#establecer condiciones

if valor_compra <80:
    print(f'hola, {nombre}.el valor a pagar es: $ {valor_compra}')

elif 80<= valor_compra < 150:
    descuento=0.1
elif 150<= valor_compra <= 300:
    descuento=0.15
elif 300<= valor_compra < 500:
    descuento=0.2

precio_final=valor_compra - (valor_compra * descuento)

print(f'compra sin descuento: {valor_compra} . \n compra con descuento: {precio_final} ')
