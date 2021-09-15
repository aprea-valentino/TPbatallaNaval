import random
from Tablero import Tablero

class TableroBot():
    def __init__(self):
        self.tablero = Tablero()
        self.tablero.barcosRandom()
   
    def sacarBarco(self, posX, posY):
        self.tablero.lista[posX][posY].sacarBarco()

    def misildisparado(self, posX, posY):
        self.tablero.lista[posX][posY].misil()
        
    def coordenadasMisilBot(self):
        posX = int(random.randrange(0,8))
        posY = int(random.randrange(0,8))

        if self.tablero.lista[posX][posY].estadoCelda() == "Misil":
            while self.tablero.lista[posX][posY].estadoCelda() == "Misil":
                posX = int(random.randrange(0,8))
                posY = int(random.randrange(0,8))
        posXY = [posX, posY]
        return posXY
