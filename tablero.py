import random
from Celda import Celda

class Tablero:
    def __init__(self):
        self.lista= []
        self.listaBot = []
        self.celda = Celda(False, None)
        self.crearCeldas()
        self.crearCeldasBot()
        self.cont = 0
        self.contBot = 0
        
    def agregarBarco(self, posX, posY):
        self.lista[posX][posY].cambiarCelda(True, False)
        
    def agregarBarcoBot(self, posX, posY):
        self.listaBot[posX][posY].cambiarCelda(True, False)
        
    def sacarBarco(self, posX, posY):
        self.lista[posX][posY].cambiarCelda(False, None)
        
    def sacarBarcoBot(self, posX, posY):
        self.listaBot[posX][posY].cambiarCelda(False, None)

    def barcoHundido(self, posX, posY):
        self.lista[posX][posY].cambiarCelda(True, True)
        
    def barcoHundidoBot(self, posX, posY):
        self.listaBot[posX][posY].cambiarCelda(True, True)
           
    def crearCeldas(self):
        self.lista= []
        for i in range(0, 8):
            self.lista.append([])
            for x in range (0, 8):
                self.lista[i].append(Celda(False, None))
                
    def crearCeldasBot(self):
        self.listaBot= []
        for i in range(0, 8):
            self.listaBot.append([])
            for x in range (0, 8):
                self.listaBot[i].append(Celda(False, None))
                
                
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
                
                
    def ubicaciones(self):
        letras = ['A','B','C','D','E','F','G','H']
        for i in range(0, 8):
            for x in range(0, 8):
                if self.lista[i][x].estado == True and self.lista[i][x].barco == False:
                   print("Hay un barco en: " + str(letras[i]) + str(x + 1))
                elif self.lista[i][x].estado == True and self.lista[i][x].barco == True:
                    print("Hay un barco hundido en: " + str(letras[i]) + str(x + 1))
                    
    def ubicacionesBot(self):
        letras = ['A','B','C','D','E','F','G','H']
        for i in range(0, 8):
            for x in range(0, 8):
                if self.listaBot[i][x].estado == True and self.listaBot[i][x].barco == False:
                   print("Hay un barco en: " + str(letras[i]) + str(x + 1))
                elif self.listaBot[i][x].estado == True and self.listaBot[i][x].barco == True:
                    print("Hay un barco hundido en: " + str(letras[i]) + str(x + 1))
                    
    def borrarBarcos(self):
        for i in range(0, 8):
            for x in range(0, 8):
                if self.lista[i][x].estado == True:
                    self.sacarBarco(i, x)
                    
    def borrarBarcosBot(self):
        for i in range(0, 8):
            for x in range(0, 8):
                if self.listaBot[i][x].estado == True:
                    self.sacarBarcoBot(i, x)
                    
    def recibirTorpedo(self, posX, posY):
        if self.lista[posX-1][posY-1].barco == True:
            print("El bot le pego devuelta al mismo")

        if self.lista[posX-1][posY-1].barco == False:
            print("Te han hundido un barco")
            self.contBot = self.comtBot + 1
            self.barcoHundido(posX-1, posY-1)
            if self.contBot == 8:
                print("PERDISTE CONTRA UN BOT")
                pri
            
        if self.lista[posX-1][posY-1].barco == None:
            print("No has recibido ningun daño")
                    
    def dispararTorpedo(self, posX, posY):
        if self.listaBot[posX-1][posY-1].barco == True:
            print("Ya dejalo ya esta muerto")
            
        if self.listaBot[posX-1][posY-1].barco == False:
            print("Le pegaste y lo hundiste, pobre barco")
            self.cont = self.cont + 1
            self.barcoHundidoBot(posX-1, posY-1)
            
            if self.cont == 2:
                print("GANASTE")
                print("Reiniciando el juego...")
                
            
        if self.listaBot[posX-1][posY-1].barco == None:
            print("water")
            

