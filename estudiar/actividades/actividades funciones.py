print("Bienvenido al conversor de monedas  \n")

def conversor(moneda_actual, valor, moneda_a_convertir):
    if moneda_actual == 1:

        def dolarTo():
            if moneda_a_convertir == "1":
                print(f'{valor} dolares esquivale a ${valor * 3750} pesos colombianos')
            elif moneda_a_convertir == "2":
                print(f'${valor} dolares equivale a ¥{valor * 6.37} yuanes')
            elif moneda_a_convertir == "3":
                print(f'${valor} dolares equivale a £{valor * 0.76} libra esterlinas')
            else:
                print("no se reconoce la moneda_a_convertir")

        dolarTo()

    elif moneda_actual == 2:

        def euroTo():
            if moneda_a_convertir == "1":
                print(f'€{valor} euro equivale a ${valor * 4000} pesos colombianos')

            elif moneda_a_convertir == "2":
                print(f'€{valor} euro equivale a ¥{valor * 6.93} yuanes')

            elif moneda_a_convertir == "3":
                print(f'€{valor} euro equivale a £{valor * 0.83} libra esterlinas')
            else:
                print("no se reconoce la moneda_a_convertir")

        euroTo()

    else:
         print("no se reconoce la moneda_a_convertir")                          


moneda_actual = int(input("ingrese su moneda actual: \n 1. dolar \n 2. euro \n"))

valor = float (input("ingrese el valor a convertir: \n"))

moneda_a_convertir = input(
        "¿A que moneda quiere convertirlo? \n 1. pesos colombianos"
        "\n 2. yuanes \n 3. libra esterlinas \n")

conversor(moneda_actual,valor,moneda_a_convertir)
