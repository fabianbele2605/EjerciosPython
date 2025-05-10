class Gato():
    def sonido(self):
        print("MIAU")

class perro():
    def sonido(self):
        print("WOU")

class cerdo ():
     def sonido(self):
          print("OING OING")

def escucharsonido(animal):
        animal.sonido()

gato1 = Gato()
perro1 = perro()
cerdo1 = cerdo()

escucharsonido(cerdo1)