b1 = None
i = None
r = None
j = None
g = None
b = None


from p5 import * # your own code
from gpiozero import *
import time
import random
import psonic as ps
import threading# your own code
b1 = Button(20)
i = 0
r = 0
def setup():
    size(640,360)
    no_stroke()# your own code
    background(204)
def draw():
    if not b1.is_pressed:
        i = random.randint(0,639)
        j = random.randint(0,359)
        g = random.randint(0,256)
        r = random.randint(0,256)
        b = random.randint(0,256)
        fill(r,g,b)
        ellipse((i,j),20,20)
def graph():
    run()
def sound():
    while True:
        if not b1.is_pressed:
            ps.sample(ps.DRUM_HEAVY_KICK)
            time.sleep(0.5)
        
        
          

T1=threading.Thread(target=graph, name="Graph")# your own code
T2=threading.Thread(target=sound, name="Sound")# your own code
T1.start()# your own code
T2.start()# your own code
