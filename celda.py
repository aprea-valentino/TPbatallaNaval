class Celda:
    def __init__(self, estado, barco):
        self.estado = estado
        self.barco = barco
        self.cont = 0       
        
    def agregarBarco(self, estado, barco):
        self.estado = True
        self.barco = False

    def sacarBarco(self, estado, barco):
        self.estado = False
        self.barco = None

    def barcoHundido(self, estado, barco):
        self.estado = True
        self.barco = True
