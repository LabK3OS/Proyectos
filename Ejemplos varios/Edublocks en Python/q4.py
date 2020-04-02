b1 = None
i = None
j = None
T1 = None
r = None
T2 = None
g = None
b = None


from p5 import *
from gpiozero import *
import time
import random
import psonic as ps
import threading
b1 = Button(20)
def setup():
  size(640,360)
  no_stroke()
  background(204)
def draw():
  if not b1.is_pressed:
    i = random.randint(0,639)
    j = random.randint(0,359)
    r = random.randint(0,256)
    g = random.randint(0,256)
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
T1 = threading.Thread(target=graph, name="graph")

T2 = threading.Thread(target=sound, name="sound")

T1.start()
T2.start()
