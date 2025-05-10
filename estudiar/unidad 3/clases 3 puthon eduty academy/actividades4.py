agenda = {  
    "jose": 302944,
    "mario": 829455,
    "angel": 829405,
    "luis": 930594,
}

consultando = True

while consultando:
    print()
    print("MI AGENDA")
    print("---------------")
    print("1. consultar \n2. añadir \n3. modificar \n4. borrar \n5. salir")

    opcion = ""

    while opcion not in ("1", "2", "3", "4", "5"):
        opcion = input("-> ")

        if opcion == "1":
            #pedir nombre
            nombre = input("nombre: ")
            #comprobar si el nombre esta en el diccionario
            if nombre not in agenda:
                print("este nombre no existe en la agenda")
            else:
                telefono = agenda[nombre]
                print(nombre, ":", telefono)

        elif opcion == "2":
            #pedir nombre
            nombre = input("nombre: ")
            #comprobar si el nombre esta en el diccionario
            if nombre in agenda:
                print("este nombre esta en la agenda")
            else:
                telefono = int(input("digita el telefono: "))
                #añadir el telefono a la agenda
                agenda[nombre] = telefono
                print("el telefono se ha añadido correctamente")

        elif opcion == "3":
            #pedir nombre
            nombre = input("nombre: ")
            if nombre not in agenda:
                print("este nombre no existe en la agenda")
            else:
                telefono = int(input("digite el telefono: "))
                #modificar el telefono
                agenda[nombre] = telefono
                print("el telefono se ha modificado correctamente")

        elif opcion =="4":
            #pedir nomnbre
            nombre = input("nombre: ")
            if nombre not in agenda:
                print("este nombre no existe en la agenda")
            else:
                #borrar el telefono
                del agenda[nombre]
                print("el telefono se ha borrado correctamente")

        elif opcion =="5":
            consultando = False
            print("gracias por utilizar el programa")                   
