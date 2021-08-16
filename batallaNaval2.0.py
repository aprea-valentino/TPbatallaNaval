import random
class Barco:
    def __init__(self, hundido):
        self.hundido = hundido
 
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
        
        
class Tablero:
    def __init__(self):
        self.lista= []
        
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
                self.lista[posX][posY].agregarBarco(True, Barco(False))               
            else:
                self.lista[posX][posY].agregarBarco(True, Barco(False))
                
                
    def ubicaciones(self):
        letras = ['A','B','C','D','E','F','G','H']
        for i in range(0, 8):
            for x in range(0, 8):
                if self.lista[i][x].estado == True:
                    print("Hay un barco en: " + str(letras[i]) + str(x + 1))
                    
    def borrarBarcos(self):
        for i in range(0, 8):
            for x in range(0, 8):
                if self.lista[i][x].estado == True:
                    self.lista[i][x].sacarBarco(False, Barco(None))
                    
                
    def dispararTorpedo(self, posX, posY):
        if self.lista[posX-1][posY-1].barco == True:
            print("Ya dejalo ya esta muerto")
        elif self.lista[posX-1][posY-1].barco == False:
            print("le pegaste y lo hundiste, pobre barco")
            self.lista[posX-1][posY-1].barcoHundido(True, Barco(True))
        elif self.lista[posX-1][posY-1].barco == None:
            print("water")
       
