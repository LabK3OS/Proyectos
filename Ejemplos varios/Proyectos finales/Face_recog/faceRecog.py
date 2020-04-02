
import picamera
import numpy as np
import face_recognition
import threading
from gpiozero import LED
import time


camera = picamera.PiCamera()
camera.resolution = (320, 240)


obama_image = face_recognition.load_image_file("/home/pi/Desktop/obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    
led = LED(20)
led.off()
output = np.empty((240, 320, 3), dtype=np.uint8)

# Load a sample picture and learn how to recognize it.

print("Loading known face image(s)")


# Initialize some variables
face_locations = []
face_encodings = []


camera.start_preview()
caras_detectadas=0
while True:
        
        
    print("Capturing image.")
    # Grab a single frame of video from the RPi camera as a numpy array
    camera.capture(output, format="rgb")

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(output)
    print("Found {} faces in image.".format(len(face_locations)))
    face_encodings = face_recognition.face_encodings(output, face_locations)

    # Loop over each face found in the frame to see if it's someone we know.
        
    caras_detectadas=0
    for face_encoding in face_encodings:
        caras_detectadas=1
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces([obama_face_encoding], face_encoding)
        name = "<Unknown Person>"
        if match[0]:
            camera.stop_preview()
           
            name = "Barack Obama"
            print("Veo a Obama")
            led.on()
        else:
            
            led.off()
            print("Veo a un desconocido")
        
    if not caras_detectadas:
        print("No veo a nadie")
        led.off()
        camera.start_preview()
 
        



        
        
        
        