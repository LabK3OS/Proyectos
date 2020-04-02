led = None
maquina = None
Imagen1 = None
nombre = None
Imagen2 = None
output = None
face_locations = None
face_encodings = None
caras_detectadas = None
name = None
match = None


# Importar las librerías necesarias para que nuestro código funcione
from picamera import *
import time
import threading
import numpy as np
import face_recognition
from gpiozero import *

# Maquina de reconocimiento facial
class Maquina_de_reconocimiento_facial():
  camera = PiCamera()
  camera.resolution = (320,240)
  def  __init__(self, ruta1, ruta2):
    Imagen1 = face_recognition.load_image_file(ruta1)
    Imagen2 = face_recognition.load_image_file(ruta2)
    self.Rostro1=face_recognition.face_encodings(Imagen1)[0]# Tu propio codigo
    self.Rostro2=face_recognition.face_encodings(Imagen2)[0]# Tu propio codigo
  def mostrarCamara(self):
    self.camera.start_preview()# Tu propio codigo
  def ocultarCamara(self):
    self.camera.stop_preview()# Tu propio codigo
  def aQuienVeo(self):
    output = np.empty((240, 320, 3), dtype=np.uint8)
    face_locations = []
    face_encodings = []
    print("Capturando imagen.")
    self.camera.capture(output,format="rgb")# Tu propio codigo
    face_locations = face_recognition.face_locations(output)
    print("Encontré {} cara(s) en la imagen.".format(len(face_locations)))
    face_encodings = face_recognition.face_encodings(output, face_locations)
    caras_detectadas = 0
    name = "Nadie"
    for face_encoding in face_encodings:
      caras_detectadas = 1
      match = face_recognition.compare_faces([self.Rostro1,self.Rostro2], face_encoding)
      if match[0]:
        self.ocultarCamara()# Tu propio codigo
        name = "Barack Obama"
        print("Veo a Obama")
      if match[1]:
        self.ocultarCamara()# Tu propio codigo
        name = "Steve Jobs"
        print("Veo a Steve Jobs")
      else:
        name = "Desconocido"
        print("Veo a un desconocido")
    if not caras_detectadas:
      print("No veo a nadie")
      self.mostrarCamara()# Tu propio codigo
    return name

# Nuestro código
led = LED(20)
led.off()
maquina = Maquina_de_reconocimiento_facial("/home/pi/Desktop/obama.jpg","/home/pi/Desktop/jobs.jpg")
while True:
  nombre = maquina.aQuienVeo()
  if nombre == "Barack Obama":
    led.on()
  else:
    led.off()