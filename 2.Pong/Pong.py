from p5 import *
import random
import time
posicionPelotaX = 0
posicionPelotaY = 0
velocidadX = 0
velocidadY = 0
puntosJugador1 = 0
puntosJugador2 = 0
posicionJugador1 = 0
posicionJugador2 = 0
ancho = 600
alto = 400
tamanoRectangulo = 150
sonarGolpe = 0


def dibujarTextoYRectangulos():
    text("P1:"+str(puntosJugador1), (50, 10))
    text("P2:"+str(puntosJugador2), (500, 10))
    rect((20, posicionJugador1-tamanoRectangulo/2), 10, tamanoRectangulo)           # Jugador 1
    rect((ancho-30, posicionJugador2-tamanoRectangulo/2), 10, tamanoRectangulo)     # Jugador 2

def reiniciarPosicionPelota():
    global posicionPelotaX,posicionPelotaY, velocidadX, velocidadY
    posicionPelotaX = ancho/2
    posicionPelotaY = alto/2
    velocidadX = random.randint(3, 10)
    velocidadY = random.randint(3, 10)

def evaluarGolpe():
    global velocidadX, velocidadY
    # si la bola golpea al jugador 1
    if posicionPelotaX > 30 and posicionPelotaX < 40 and  posicionPelotaY > posicionJugador1-tamanoRectangulo/2 and posicionPelotaY < posicionJugador1+tamanoRectangulo/2 :
        velocidadX = velocidadX * -1
        velocidadY = velocidadY * -1
        sonarGolpe=1
        

    # si la bola golpea al jugador 2 
    elif  posicionPelotaX > ancho-40 and posicionPelotaX < ancho -30 and posicionPelotaY > posicionJugador2-tamanoRectangulo/2 and posicionPelotaY < posicionJugador2+tamanoRectangulo/2 :
        velocidadX = velocidadX * -1
        velocidadY = velocidadY * -1
        sonarGolpe=1

    # evaluar si se golpea una pared
    elif  posicionPelotaY > alto or posicionPelotaY < 0 :
        velocidadY = velocidadY * -1
        sonarGolpe=1
    else:
        sonarGolpe=0

def setup():
    global posicionPelotaX,posicionPelotaY, velocidadX, velocidadY, puntosJugador1, puntosJugador2
    size(ancho,alto)
    fill(0, 255, 0)
    text_font(create_font("Memorial Lane.otf", 20),20)
    reiniciarPosicionPelota()



def draw():
    global posicionJugador1, posicionJugador2, posicionPelotaX,posicionPelotaY, velocidadX, velocidadY, puntosJugador1, puntosJugador2
    background(0);
    posicionJugador1=mouse_x
    posicionJugador2=mouse_y
    if puntosJugador1==5:
        text("P1 gano", (280, 200)) 
        puntosJugador1+=1
    elif puntosJugador2==5:
        text("P2 gano", (280, 200))
        puntosJugador2+=1
    elif puntosJugador1>5:        
        reiniciarPosicionPelota()
        puntosJugador1=0
        puntosJugador2=0
        time.sleep(3)
    elif puntosJugador2>5:
        reiniciarPosicionPelota()
        puntosJugador1=0
        puntosJugador2=0
        time.sleep(3)
    else:
        ellipse( (posicionPelotaX, posicionPelotaY), 20, 20)
        posicionPelotaX += velocidadX
        posicionPelotaY += velocidadY
        evaluarGolpe()
        if posicionPelotaX < -10:
            reiniciarPosicionPelota()
            puntosJugador2+=1
        if posicionPelotaX > ancho+10:
            reiniciarPosicionPelota()
            puntosJugador1+=1

    dibujarTextoYRectangulos() 

run()

