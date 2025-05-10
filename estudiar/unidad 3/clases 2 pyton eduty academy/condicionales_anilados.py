'''edad = int(input("cuantos años tienes"))
graduacion = input("¿ya te has graduado? (si) o (no)")

if edad > 18:
    print("y que esperas para estudiar vago hp")
    if graduacion == 'si' :
        print("felicidades por tu graduacion")
'''

password = input("ingresa la contraseña: ")

if (len(password) >= 8):
    print("muy bien,contraseña suficientemente larga")

    if (password == 'noah1308'):
        print("ademas, es la contraseña correcta")
    else:
        print("pero es incorrecta")
else:
    print("tu contraseña es muy corta e insegura")
    print("ademas, es incorrecta")            

