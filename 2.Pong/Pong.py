from p5 import *
import random
x=0
y=0
speedX=0
speedY=0
diam = 10;
rectSize = 200;
def setup():
    size(800,600)
    fill(0, 255, 0)
    reset()
    font=create_font("Memorial Lane.otf", 32);
    text_font(font,20)
    
    

def reset():
    global x,y, speedX, speedY
    x = width/2
    y = height/2
    speedX = random.randint(3, 20)
    speedY = random.randint(3, 20)
def draw():

    global x,y, speedX, speedY
    background(0);
    
    text("Temp", (400, 400))
    ellipse( (x, y), diam, diam)
    rect((0, 0), 20, height)
    rect((width-30, mouse_y-rectSize/2), 10, rectSize)
    x += speedX
    y += speedY
    # if ball hits movable bar, invert X direction
    if  x > width-30 and x < width -20 and y > mouse_y-rectSize/2 and y < mouse_y+rectSize/2 :
        speedX = speedX * -1
    # if ball hits wall, change direction of X
    if x < 25:
        speedX *= -1.1
        speedY *= 1.1
        x += speedX
    # if ball hits up or down, change direction of Y   
    if  y > height or y < 0 :
        speedY *= -1
def mousePressed():
    reset()
run()
#37 bloques
