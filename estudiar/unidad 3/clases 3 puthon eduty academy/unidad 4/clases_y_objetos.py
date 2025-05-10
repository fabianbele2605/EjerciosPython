class Bicicleta:
    def __init__(self, color, cambios, rin):
        self.color = color
        self.cambios = cambios
        self.rin = rin

    def frenar(self):
        return "la bicicleta esta frenando."
    
    def avanzar(self):
        return "la bicicleta esta en movimiento."
    
    def girar(self):
        return "la bicicleta esta girando."
    
    
urbana = Bicicleta("Rojo", 8, 27.5)
hibrida = Bicicleta("Azul", 1, 29)

print("urbana: " + str(urbana.color))
print("comportamiento de la bicicleta urbana: " + str(urbana.girar()))
print('\n')
print("hibrida: " + str(hibrida.cambios))
print("comportamiento de la bicicleta hibrida: " + str(hibrida.avanzar()))