#calculadora de indice de masa corporal (imc)

contador = 0

print("calculadora de indice de masa corporal (IMC)")

while contador != 2:
    contador = int(input("¿quieres seguir calculando el IMC? 1.Si y 2.No \n"))

    if contador ==1:
        estatura = float(input("ingresa su estatura en metros: "))
        peso = float(input("ingrese su peso en kilogramos: "))
        resultado = round(peso/(estatura ** 2), 2)

        if resultado < 18.5:
            print(f'IMC {resultado} = BAJO DE PESO')
        elif 18.5 <resultado < 24.99:
            print(f'IMC {resultado} = PESO NORMAL') 
        elif 25 < resultado < 30:
            print(f'IMC {resultado} = SOBREPESO') 
        elif resultado > 30:
            print(f'IMC {resultado} = OBECIDAD') 

    elif contador == 2:
        print("hasta pronto")


print("gracias por usar la calculadora de IMC")
