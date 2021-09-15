import random
from Tablero import Tablero

class TableroBot():
    '''Tablero del bot'''

    def __init__(self):
        self.tablero = Tablero()
        self.tablero.barcosRandom()
   
    def sacarBarco(self, posX, posY):
        '''Saca el barco de las coodenadas ingresadas'''
        self.tablero.lista[posX][posY].sacarBarco()

    def misildisparado(self, posX, posY):
        '''Ubica el misil en las coordenadas ingresadas'''
        self.tablero.lista[posX][posY].misil()
        
    def coordenadasMisilBot(self):
        '''Genera un numero random para devolver las coordenadas a disparar'''
        posX = int(random.randrange(0,8))
        posY = int(random.randrange(0,8))

        if self.tablero.lista[posX][posY].estadoCelda() == "Misil":
            while self.tablero.lista[posX][posY].estadoCelda() == "Misil":
                posX = int(random.randrange(0,8))
                posY = int(random.randrange(0,8))
        posXY = [posX, posY]
        return posXY
