import time
from Tablero import Tablero
class Juego:
    def __init__(self):
        self.tablero = Tablero()
        self.tablero.crearCeldas()
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
            self.agregarBarco()
        if opcion == 3:
            exit()
            
    def decision(self):
        opcion=0
        print("------------------------------------------------------------")
        print("Que wishea hacer")
        print("Disparar(1)")
        print("Ver ubicaciones de los barcos(2)")
        print("Borrar y cu8enta nueva(3)")
        opcion= int(input("ingrese decision: "))
        if opcion==1:
            self.disparar()
        if opcion==2:
            self.verUbicaciones()
        if opcion==3:
            self.borrarBarcos()
            
    def barcosRandom(self):
        self.tablero.barcosRandom()
        
    def verUbicaciones(self):
        print("------------------------------------------------------------")
        self.tablero.ubicaciones()
        self.decision()
        
    def disparar(self):
        print("------------------------------------------------------------")
        posX = int(input("donde quiere disparar en x: "))
        posY = int(input("ahora en y: "))
        self.tablero.dispararTorpedo(posX, posY)
        self.decision()
        
    def borrarBarcos(self):
        self.tablero.borrarBarcos()
        self.inicio()

    def agregarBarco(self):
        for i in range(0,8):
            print("------------------------------------------------------------")
            posX = int(input("seleccione una posicion en x: "))
            posY = int(input("seleccion una posiscion en y: "))
            self.tablero.agregarBarco(posX-1, posY-1)
        self.decision()

if __name__=="__main__":
    unJuego = Juego()      


