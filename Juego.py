import time
import random
from Tablero import Tablero
from TableroBot import TableroBot
class Juego:
    def __init__(self):
        self.tablero = Tablero()
        self.tableroBot = TableroBot()
        self.inicio()

    def inicio(self):
        opcion=0
        print("------------------------------------------------------------")
        print("Que desea hacer")
        print("Quiere generar todos los barcos de manera aleatorio(1)" )
        print("Quiere posicionar los barco manualmente(2)")
        print("quitear(3)")
        opcion=int(input("ingrese su decision: "))
        if opcion == 1:
            self.barcosRandom()
            self.decision()
        if opcion == 2:
            self.agregarBarcos()
        if opcion == 3:
            exit()
            
    def decision(self):
        opcion=0
        print("------------------------------------------------------------")
        print("Que wishea hacer")
        print("Disparar(1)")
        print("Ver ubicaciones de los barcos(2)")
        print("Agregar un barco(3)")
        print("Eliminar un barco(4)")
        print("Borrar y cuenta nueva(5)")
        opcion= int(input("ingrese decision: "))
        if opcion==1:
            self.disparar()
        elif opcion==2:
            self.verUbicaciones()
        elif opcion==5:
            self.borrarBarcos()
        elif opcion==4:
            self.sacarBarco()
        elif opcion == 3:
            self.agregarUnBarco()
        elif opcion==12:
            self.tableroBot.ubicacionesBot()
            self.decision()
            
    def barcosRandom(self):
        self.tablero.barcosRandom()
        self.tableroBot.barcosRandomBot()
        
    def verUbicaciones(self):
        print("------------------------------------------------------------")
        self.tablero.ubicaciones()
        time.sleep(1)
        self.decision()
        
    def disparar(self):
        print("------------------------------------------------------------")
        posX = str(input("donde quiere disparar en x: "))
        if posX not in ["1","2","3","4","5","6","7","8"]:
            while posX not in ["1","2","3","4","5","6","7","8"]:
                posX = str(input("ingrese bien la coordenada en x: "))
        posX = int(posX)
        
        posY = str(input("ahora en y: "))
        if posY not in ["1","2","3","4","5","6","7","8"]:
            while posY not in ["1","2","3","4","5","6","7","8"]:
                posY = str(input("ingrese bien la coordenada en y: "))
        posY = int(posY)
        self.tableroBot.recibirTorpedo(posX, posY)
        if self.tableroBot.contBot == 8:
            self.borrarBarcos()
            self.inicio()
        else:
            print("Turno del bot")
            time.sleep(1)
            self.disparaBot()
            if self.tablero.cont == 8:
                self.borrarBarcos()
                self.inicio()
            self.decision()
            
    def disparaBot(self):
        posX = int(random.randrange(0, 8))
        posY = int(random.randrange(0, 8))
        self.tablero.recibirTorpedo(posX, posY)
        print(posX)
        print(posY)
        
    def borrarBarcos(self):
        self.tablero.borrarBarcos()
        self.tableroBot.borrarBarcosBot()
        self.inicio()

    def sacarBarco(self):
        print("------------------------------------------------------------")
        posX = str(input("donde quiere disparar en x: "))
        if posX not in ["1","2","3","4","5","6","7","8"]:
            while posX not in ["1","2","3","4","5","6","7","8"]:
                posX = str(input("ingrese bien la coordenada en x: "))
        posX = int(posX)

        posY = str(input("ahora en y: "))
        if posY not in ["1","2","3","4","5","6","7","8"]:
            while posY not in ["1","2","3","4","5","6","7","8"]:
                posY = str(input("ingrese bien la coordenada en y: "))
        posY = int(posY)
        
        self.tablero.sacarBarco(posX - 1, posY - 1)
        self.decision()

    def agregarUnBarco(self):
        posX = str(input("ingrese coordenada en x: "))
        if posX not in ["1","2","3","4","5","6","7","8"]:
            while posX not in ["1","2","3","4","5","6","7","8"]:
                posX = str(input("ingrese bien la coordenada en x: "))
        posX = int(posX)

        posY = str(input("ahora en y: "))
        if posY not in ["1","2","3","4","5","6","7","8"]:
            while posY not in ["1","2","3","4","5","6","7","8"]:
                posY = str(input("ingrese bien la coordenada en y: "))
        posY = int(posY)

        if self.tablero.lista[posX-1][posY-1].estado == True:
            while self.tablero.lista[posX-1][posY-1].estado == True:
                print("Ya existe un barco en esa posicion")    
                posX = str(input("ingrese otra coordenada en x: "))
                if posX not in ["1","2","3","4","5","6","7","8"]:
                    while posX not in ["1","2","3","4","5","6","7","8"]:
                        posX = str(input("ingrese bien la coordenada en x: "))
                posX = int(posX)

                posY = str(input("ahora en y: "))
                if posY not in ["1","2","3","4","5","6","7","8"]:
                    while posY not in ["1","2","3","4","5","6","7","8"]:
                        posY = str(input("ingrese bien la coordenada en y: "))
                posY = int(posY)

            self.tablero.agregarBarco(posX-1, posY-1)               
        self.tablero.agregarBarco(posX-1, posY-1)
        self.decision()

    def agregarBarcos(self):
        self.tablero.agregarBarcos()
        time.sleep(1)
        self.decision()

if __name__=="__main__":
    unJuego = Juego()      


