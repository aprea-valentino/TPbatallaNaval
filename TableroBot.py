import random
from Celda import Celda
class TableroBot:
    def __init__(self):
        self.listaBot = []
        self.celda = Celda(False, "agua")
        self.crearCeldasBot()
        self.contBot = 0

    def agregarBarcoBot(self, posX, posY):
        self.listaBot[posX][posY].cambiarCelda(True, False)

    def sacarBarcoBot(self, posX, posY):
        self.listaBot[posX][posY].cambiarCelda(False, "agua")

    def barcoHundidoBot(self, posX, posY):
        self.listaBot[posX][posY].cambiarCelda(True, True)

    def crearCeldasBot(self):
        self.listaBot= []
        for i in range(0, 8):
            self.listaBot.append([])
            for x in range (0, 8):
                self.listaBot[i].append(Celda(False, "agua"))

    def barcosRandomBot(self):
        for i in range(0, 8):
            posX = int (random.randrange(0, 8))
            posY = int (random.randrange(0, 8))
            if self.listaBot[posX][posY].estado == True:
                while self.listaBot[posX][posY].estado == True:
                    posX = int (random.randrange(0, 8))
                    posY = int (random.randrange(0, 8))
                self.agregarBarcoBot(posX, posY)               
            else:
                self.agregarBarcoBot(posX, posY)

    def ubicacionesBot(self):
        letras = ['A','B','C','D','E','F','G','H']
        for i in range(0, 8):
            for x in range(0, 8):
                if self.listaBot[i][x].estado == True and self.listaBot[i][x].barco == False:
                   print("Hay un barco en: " + str(letras[i]) + str(x + 1))
                elif self.listaBot[i][x].estado == True and self.listaBot[i][x].barco == True:
                    print("Hay un barco hundido en: " + str(letras[i]) + str(x + 1))

    def borrarBarcosBot(self):
        for i in range(0, 8):
            for x in range(0, 8):
                if self.listaBot[i][x].estado == True:
                    self.sacarBarcoBot(i, x)
                    
    def recibirTorpedo(self, posX, posY):
        if self.listaBot[posX-1][posY-1].barco == True:
            print("Ya dejalo ya esta muerto")
            
        if self.listaBot[posX-1][posY-1].barco == False:
            print("Le pegaste y lo hundiste, pobre barco")
            self.contBot = self.contBot + 1
            self.barcoHundidoBot(posX-1, posY-1)
            
            if self.contBot == 8:
                print("GANASTE")
                print("Reiniciando el juego...")
                   
        if self.listaBot[posX-1][posY-1].barco == "agua":
            print("water")
