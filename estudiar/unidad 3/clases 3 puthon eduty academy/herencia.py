class vehiculo():
    def __init__(self, matricula, modelo, marca, color):
        self.matricula = matricula
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.avanza = False
        self.frena = False
        self.gira = False


    def avanzar(self):
        self.avanza = True

    def frenar(self):
        self.frena = True

    def girar(self):
        self.gira = True

    def imprimir(self):
        print(f'matricula: {self.matricula} \n modelo: {self.modelo} \n marca: {self.marca} \n'            
              f' color: {self.color} \n avanzar: {self.avanza} \n' 
              f'frenar: {self.frena} \n girar:{self.gira}')


class moto(vehiculo):
    def __init__(self, matricula, modelo, marca, color, cilindraje):
        super().__init__(matricula, modelo, marca, color,)
        self.cilindraje = cilindraje

moto1 = moto("abc123", "2023", "honda", "blanca", "250")

moto1.avanzar()
moto1.frenar()
moto1.girar()
print("cilindraje" + str(moto1.cilindraje))
moto1.imprimir()

         