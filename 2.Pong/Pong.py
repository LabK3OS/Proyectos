from p5 import *
import random
import time
posicionPelotaX=0
posicionPelotaY=0
velocidadX=0
velocidadY=0
puntosJugador1=0
puntosJugador2=0
ancho=600
alto=400
tamanoRectangulo = 150;

def setup():
    global posicionPelotaX,posicionPelotaY, velocidadX, velocidadY, puntosJugador1, puntosJugador2
    size(ancho,alto)
    fill(0, 255, 0)    
    posicionPelotaX = ancho/2
    posicionPelotaY = alto/2
    velocidadX = random.randint(3, 10)
    velocidadY = random.randint(3, 10)
    text_font(create_font("Memorial Lane.otf", 20),20)


def draw():
    global posicionPelotaX,posicionPelotaY, velocidadX, velocidadY, puntosJugador1, puntosJugador2
    background(0);

    if puntosJugador1==4:
        text("P1 gano", (280, 200)) 
        puntosJugador1+=1
    elif puntosJugador2==4:
        text("P2 gano", (280, 200))
        puntosJugador2+=1
    elif puntosJugador1==5:
               
        posicionPelotaX = ancho/2
        posicionPelotaY = alto/2
        velocidadX = random.randint(3, 10)
        velocidadY = random.randint(3, 10)
        puntosJugador1=0
        puntosJugador2=0
        time.sleep(3)

    elif puntosJugador2==5:
                
        posicionPelotaX = ancho/2
        posicionPelotaY = alto/2
        velocidadX = random.randint(3, 10)
        velocidadY = random.randint(3, 10)
        puntosJugador1=0
        puntosJugador2=0
        time.sleep(3) 
    else:


        ellipse( (posicionPelotaX, posicionPelotaY), 20, 20)



        posicionPelotaX += velocidadX
        posicionPelotaY += velocidadY


        # si la bola golpea al jugador 1 
        if posicionPelotaX > 30 and posicionPelotaX < 40 and  posicionPelotaY > mouse_x-tamanoRectangulo/2 and posicionPelotaY < mouse_x+tamanoRectangulo/2 :
            velocidadX = velocidadX * -1
            velocidadY = velocidadY * -1

        # si la bola golpea al jugador 2 
        if  posicionPelotaX > ancho-40 and posicionPelotaX < ancho -30 and posicionPelotaY > mouse_y-tamanoRectangulo/2 and posicionPelotaY < mouse_y+tamanoRectangulo/2 :
            velocidadX = velocidadX * -1
            velocidadY = velocidadY * -1

        # evaluar si se golpea una pared
        if  posicionPelotaY > alto or posicionPelotaY < 0 :
            velocidadY *= -1

        # evaluar puntos jugador 1:

        if posicionPelotaX < -10:
            posicionPelotaX = ancho/2
            posicionPelotaY = alto/2
            velocidadX = (-velocidadX/velocidadX) * random.randint(5, 10) 
            velocidadY = (-velocidadY/velocidadY) * random.randint(5, 10)
            puntosJugador2+=1
        if posicionPelotaX > ancho+10:
            posicionPelotaX = ancho/2
            posicionPelotaY = alto/2
            velocidadX = (-velocidadX/velocidadX) * random.randint(5, 10)
            velocidadY = (-velocidadY/velocidadY) * random.randint(5, 10)
            puntosJugador1+=1

    text("P1:"+str(puntosJugador1), (50, 10))
    text("P2:"+str(puntosJugador2), (500, 10))
    rect((20, mouse_x-tamanoRectangulo/2), 10, tamanoRectangulo)    # Jugador 1
    rect((ancho-30, mouse_y-tamanoRectangulo/2), 10, tamanoRectangulo) # Jugador 2
 

run()

