import random
from Celda import Celda
class Tablero:
    def __init__(self):
        self.lista= []
        self.celda = Celda(False, "agua")
        self.crearCeldas()
        self.cont = 0
        self.posX = 0
        self.posY = 0
        
        
    def agregarBarco(self, posX, posY):
        self.lista[posX][posY].cambiarCelda(True, False)
        
    
        
    def sacarBarco(self, posX, posY):
        self.lista[posX][posY].cambiarCelda(False, "agua")
        

    def barcoHundido(self, posX, posY):
        self.lista[posX][posY].cambiarCelda(True, True)
        
           
    def crearCeldas(self):
        self.lista= []
        for i in range(0, 8):
            self.lista.append([])
            for x in range (0, 8):
                self.lista[i].append(Celda(False, "agua"))
                
                
    def agregarBarcos(self):
        for i in range(0, 8):
            print("------------------------------------------------------------")
            posX = str(input("Seleccione una posicion en x: "))
            if posX not in ["1","2","3","4","5","6","7","8"]:
                while posX not in ["1","2","3","4","5","6","7", "8"]:
                    posX= str(input("Seleccione otra posicion en x: "))
            posX = int(posX)
            posY = str(input("seleccione una posicion en y: "))
            if posY not in ["1","2","3","4","5","6","7","8"]:
                while posY not in ["1","2","3","4","5","6","7","8"]:
                    posY= str(input("Seleccione otra posicion en y: "))
            posY = int(posY)
            if self.lista[posX-1][posY-1].estado == True:
                while self.lista[posX-1][posY-1].estado == True:
                    posX = int(input("Ya existe un barco en esa posicion, Seleccione otra coordenada en x:"))
                    posY = int(input("Seleccione una coordenada en y"))
                self.agregarBarco(posX-1, posY-1)
            else:
                self.agregarBarco(posX-1, posY-1)
           
        self.tableroBot.barcosRandomBot()
        
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
                                     
                    
            
    def recibirTorpedo(self, posX, posY):
        if self.lista[posX-1][posY-1].barco == True:
            print("El bot le pego devuelta al mismo")

        if self.lista[posX-1][posY-1].barco == False:
            print("Te han hundido un barco")
            self.cont = self.cont + 1
            self.barcoHundido(posX-1, posY-1)
            if self.cont == 8:
                print("PERDISTE CONTRA UN BOT")
                
            
        if self.lista[posX-1][posY-1].barco == "agua":
            print("water")

