import time
import random
from typing import Coroutine
from TableroJugador import TableroJugador

class Juego:
    def __init__(self) -> None:
        self.jugador = TableroJugador()
        self.Inicio()

    def Inicio(self):
        self.decision()

        while (self.jugador.bot.tablero.contador != 8):
            decision = int(input("Desea ver las ubicaciones de tus barcos(1) o disparar torpedo(2)"))
            
            if decision == 1:
                self.jugador.tablero.ubicaciones()
            elif decision == 2:
                print("Su turno")
                print("Ingrese coordenadas A-H y 1-8")
                coordenadas = self.jugador.ponerCoordenadas()
                self.jugador.dispararTorpedo(coordenadas[1], coordenadas[0])

                if self.jugador.tablero.contador == 8:
                    break
                print("Turno del bot")
                coordenadas = self.jugador.bot.coordenadasMisilBot()
                self.misilJugador(coordenadas[0], coordenadas[1])

        if self.jugador.tablero.contador == 8:
            print("Has ganado")
        else:
            print("Perdiste contra un bot")

    def misilJugador(self, posX, posY):
        if self.jugador.tablero.lista[posX][posY].barco == None:
            self.misilHundido(posX, posY)
            print("Agua")
        else:
            self.barcoHundidoJ(posX, posY)
            print("El bot hundio un barco")
        
        if self.jugador.tablero.contador == 8:
            print("Gano el bot")

    def barcoHundidoJ(self, posX, posY):
        self.jugador.tablero.lista[posX][posY].sacarBarco()

    def misilHundido(self, posX, posY):
        self.jugador.tablero.lista[posX][posY].misil()

    def decision(self):
        '''Decide si poner random o no, todos los barcos'''
        rta = int(input("Desea poner los 8 barcos manualmente(1) o de manera random(2)"))
        if rta == 1:
            for i in range(0,8):
                coordenadas = self.jugador.ponerCoordenadas()
                if self.jugador.tablero.lista[coordenadas[1]][coordenadas[0]].estado == True:
                    while self.jugador.tablero.lista[coordenadas[1]][coordenadas[0]].estado == True:
                        print("No repita coordenadas")
                        coordenadas = self.jugador.ponerCoordenadas()
                self.jugador.agregarBarco(coordenadas[1], coordenadas[0])
        elif rta == 2:
            self.jugador.tablero.barcosRandom()              
            
if __name__=="__main__":
    unJuego = Juego()      


