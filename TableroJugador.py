
from Tablero import Tablero
from TableroBot import TableroBot

class TableroJugador():
    '''Tablero del jugador'''
    def __init__(self):
        self.tablero = Tablero()
        self.bot = TableroBot()

        
    def agregarBarco(self, posX, posY):
        self.tablero.agregarBarco(posX, posY)
    
        
    def sacarBarco(self, posX, posY):
        self.bot.tablero.lista[posX][posY].sacarBarco()
        

    def misildisparado(self, posX, posY):
        
        self.bot.tablero.lista[posX][posY].misil()
                    
            
    def dispararTorpedo(self, posX, posY):
        if self.bot.tablero.lista[posX][posY].barco == None:
            self.misildisparado(posX, posY)
            print("Agua")

        elif self.bot.tablero.lista[posX][posY].barco.hundido == True:
            print("Dejalo ya esta muerto")
            
        else:
            self.bot.sacarBarco(posX, posY)
            print("Hundiste un barco, pobre barco")

            self.bot.tablero.contador += 1

            if self.bot.tablero.contador == 8:
                print("has ganado, bien hecho")

                
    def ponerCoordenadas(self):
        posY = str(input("Ingrese una letra: "))
        posY = posY.upper()
        letras = ['A','B','C','D','E','F','G','H']
        
        if posY not in ['A','B','C','D','E','F','G','H']: 
            while posY not in ['A','B','C','D','E','F','G','H']:
                posY= str(input("Ingrese una letra valida: "))
                posY = posY.upper()
                exit

        posX = str(input("ingrese coordenada en x: "))
        if posX not in ["1","2","3","4","5","6","7","8"]:
            while posX not in ["1","2","3","4","5","6","7","8"]:
                posX = str(input("ingrese bien la coordenada en x: "))
        posX = int(posX)

        for i in range (0,8):
            if posY == letras[i]:
                posX -= 1
                coordenadas = [i, posX]

        return coordenadas
