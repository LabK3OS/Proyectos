


from p5 import *# your own code
from gpiozero import *
b1 = Button(20)
i=0
j=0

def setup():

    print("c1")
    size(640,360)
    no_stroke()# your own code
    background(204)
def draw():
    global i,j
    if b1.is_pressed:
        if i<400:
            i=i+1
        else:
            i=0
            if j<200:
                j=j+1
            else:
                j=0 
            
        fill(0,15)
        ellipse((i,j),5,5)    
        print(i,j)

run()
