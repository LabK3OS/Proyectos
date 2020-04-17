from p5 import *
import random
import time
x=0
y=0
speedX=0
speedY=0
p1=0
p2=0
ancho=600
alto=400
rectSize = 150;

def setup():
    global x,y, speedX, speedY, p1, p2
    size(ancho,alto)
    fill(0, 255, 0)    
    x = ancho/2
    y = alto/2
    speedX = random.randint(3, 10)
    speedY = random.randint(3, 10)
    text_font(create_font("Memorial Lane.otf", 20),20)


def draw():
    global x,y, speedX, speedY, p1, p2
    background(0);

    if p1==4:
        text("P1 gano", (280, 200)) 
        p1+=1
    elif p2==4:
        text("P2 gano", (280, 200))
        p2+=1
    elif p1==5:
               
        x = ancho/2
        y = alto/2
        speedX = random.randint(3, 10)
        speedY = random.randint(3, 10)
        p1=0
        p2=0
        time.sleep(3)

    elif p2==5:
                
        x = ancho/2
        y = alto/2
        speedX = random.randint(3, 10)
        speedY = random.randint(3, 10)
        p1=0
        p2=0
        time.sleep(3) 
    else:


        ellipse( (x, y), 20, 20)



        x += speedX
        y += speedY


        # si la bola golpea al jugador 1 
        if x > 30 and x < 40 and  y > mouse_x-rectSize/2 and y < mouse_x+rectSize/2 :
            speedX = speedX * -1
            speedY = speedY * -1

        # si la bola golpea al jugador 2 
        if  x > ancho-40 and x < ancho -30 and y > mouse_y-rectSize/2 and y < mouse_y+rectSize/2 :
            speedX = speedX * -1
            speedY = speedY * -1

        # evaluar si se golpea una pared
        if  y > alto or y < 0 :
            speedY *= -1

        # evaluar puntos jugador 1:

        if x < -10:
            x = ancho/2
            y = alto/2
            speedX = (-speedX/speedX) * random.randint(5, 10) 
            speedY = (-speedY/speedY) * random.randint(5, 10)
            p2+=1
        if x > ancho+10:
            x = ancho/2
            y = alto/2
            speedX = (-speedX/speedX) * random.randint(5, 10)
            speedY = (-speedY/speedY) * random.randint(5, 10)
            p1+=1

    text("P1:"+str(p1), (50, 10))
    text("P2:"+str(p2), (500, 10))
    rect((20, mouse_x-rectSize/2), 10, rectSize)    # Jugador 1
    rect((ancho-30, mouse_y-rectSize/2), 10, rectSize) # Jugador 2
 

run()

