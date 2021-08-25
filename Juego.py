import time
import random
from Tablero import Tablero
class Juego:
    def __init__(self):
        self.tablero = Tablero()
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
            self.tablero.ubicacionesBot()
            self.decision()
            
    def barcosRandom(self):
        self.tablero.barcosRandom()
        self.tablero.barcosRandomBot()
        
    def verUbicaciones(self):
        print("------------------------------------------------------------")
        self.tablero.ubicaciones()
        time.sleep(1)
        self.decision()
        
    def disparar(self):
        print("------------------------------------------------------------")
        posX = int(input("donde quiere disparar en x: "))
        posY = int(input("ahora en y: "))
        self.tablero.dispararTorpedo(posX, posY)
        if self.tablero.cont == 2:
            self.borrarBarcos()
            self.inicio()
        else:
            print("Turno del bot")
            time.sleep(1)
            self.disparaBot()
            self.decision()
            
    def disparaBot(self):
        posX = int(random.randrange(0, 8))
        posY = int(random.randrange(0, 8))
        self.tablero.recibirTorpedo(posX, posY)
        print(posX)
        print(posY)
        
    def borrarBarcos(self):
        self.tablero.borrarBarcos()
        self.tablero.borrarBarcosBot()
        self.inicio()

    def sacarBarco(self):
        print("------------------------------------------------------------")
        posX = int(input("seleccione una posicion en x: "))
        posY = int(input("seleccione una posicion en y: "))
        self.tablero.sacarBarco(posX - 1, posY - 1)
        self.decision()

    def agregarUnBarco(self):
        posX = int(input("seleccione una posicion en x: "))
        posY = int(input("seleccione una posicion en y: "))
        self.tablero.agregarBarco(posX-1, posY-1)
        self.decision()

    def agregarBarcos(self):
        for i in range(0,8):
            print("------------------------------------------------------------")
            posX = int(input("seleccione una posicion en x: "))
            posY = int(input("seleccion una posiscion en y: "))
            self.tablero.agregarBarco(posX-1, posY-1)
        time.sleep(1)
        self.decision()

if __name__=="__main__":
    unJuego = Juego()      


