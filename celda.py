from Barco import Barco
class Celda:
    def __init__(self, estado, barco):
        self.estado = estado
        self.barco = barco       
        
    def cambiarCelda(self, estado, barco):
        self.estado = estado
        self.barco = barco
        
