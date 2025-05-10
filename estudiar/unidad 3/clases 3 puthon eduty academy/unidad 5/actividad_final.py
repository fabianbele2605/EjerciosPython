class persona:

    def __init__(self):
        self.nombre=input("ingrese el nombre:")
        self.edad=int(input("ingrese la edad:"))

    def imprimir(self):
        print("nombre:",self.nombre)
        print("edad:",self.edad)


class cuidadano(persona):

    def __init__(self):
        super().__init__()
        self.deposito=float(input("ingrese el dinero a depositar:"))

    def imprimir(self):
        return super().imprimir()
        print("deposito:",self.deposito)

    def impuestos(self):
        if self.deposito >4000:
            print(f'el cuidadano {self.nombre} debe pagar impuesto')
        else:
            print(f'el cuidadano {self.nombre} no debe pagar impuesto')


#instancias
cuidadano1 = cuidadano()
cuidadano1.imprimir()
cuidadano1.impuestos()



        