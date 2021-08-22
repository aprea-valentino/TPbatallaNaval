import random
from Celda import Celda

class Tablero:
    def __init__(self):
        self.lista= []
        self.celda = Celda(False, None)
        self.crearCeldas()
        
    def agregarBarco(self, posX, posY):
        self.lista[posX][posY].cambiarCelda(True, False)
        
    def sacarBarco(self, posX, posY):
        self.lista[posX][posY].cambiarCelda(False, None)

    def barcoHundido(self, posX, posY):
        self.lista[posX][posY].cambiarCelda(True, True)
           
    def crearCeldas(self):
        self.lista= []
        for i in range(0, 8):
            self.lista.append([])
            for x in range (0, 8):
                self.lista[i].append(Celda(False, None))
                
    def barcosRandom(self):
        for i in range(0, 8):
            posX = int (random.randrange(0, 8))
            posY = int (random.randrange(0, 8))
            if self.lista[posX][posY].estado == True:
                while self.lista[posX][posY].estado == True:
                    posX = int (random.randrange(0, 8))
                    posY = int (random.randrange(0, 8))
                self.agregarBarco(posX, posY)               
            else:
                self.agregarBarco(posX, posY)
                
                
    def ubicaciones(self):
        letras = ['A','B','C','D','E','F','G','H']
        for i in range(0, 8):
            for x in range(0, 8):
                if self.lista[i][x].estado == True and self.lista[i][x].barco == False:
                   print("Hay un barco en: " + str(letras[i]) + str(x + 1))
                elif self.lista[i][x].estado == True and self.lista[i][x].barco == True:
                    print("Hay un barco hundido en: " + str(letras[i]) + str(x + 1))
                    
                    
    def borrarBarcos(self):
        for i in range(0, 8):
            for x in range(0, 8):
                if self.lista[i][x].estado == True:
                    self.sacarBarco(i, x)
                    
                
    def dispararTorpedo(self, posX, posY):
        if self.lista[posX-1][posY-1].barco == True:
            print("Ya dejalo ya esta muerto")
        elif self.lista[posX-1][posY-1].barco == False:
            print("le pegaste y lo hundiste, pobre barco")
            self.barcoHundido(posX-1, posY-1)
        elif self.lista[posX-1][posY-1].barco == None:
            print("water")
            

