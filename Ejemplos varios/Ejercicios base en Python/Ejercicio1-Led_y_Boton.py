#!/usr/bin/env python
# -*- coding: utf-8 -*- 


import RPi.GPIO as GPIO       		# Con esta libreria, traemos las herramientas necesarias para poder utilizar las conexiones fisicas de K3OS            
import time							# Con esta libreria, traemos las herramientas necesarias, para poder esperar una cantidad de tiempo determinada dentro de nuestro programa


#Configuramos los pines externos

GPIO.setwarnings(False)				# Deshabilitar la alertas de GPIO
GPIO.setmode(GPIO.BCM)  			# Esta linea es requerida para numerar los pines, de acuerdo a los rotulos de K3OS
LED1 = 12							# Nombramos al pin GPIO 12 como LED1, el pin donde se encuentra conectado el LED
BUT1 = 13							# Nombramos al pin GPIO 13 como BUT1, el pin donde se encuentra conectado el boton
GPIO.setup(LED1,GPIO.OUT)			# Configuramos el pin del led como salida
GPIO.setup(BUT1,GPIO.IN)			# Configuramos el pin del boton como entrada	

def revisarBoton():					# Declaramos una funcion para revisar el estado del boton, y encender el Led, en caso de que el boton este oprimido
	if(GPIO.input(BUT1)==1):		# Evaluar el estado del boton, y ejecutar las siguientes lineas de codigo, en caso de que el boton este presionado
		GPIO.output(LED1, True)		# Encender el LED
		sleep(5)					# Esperar 5 segundos
		GPIO.output(LED1, True)		# Apagar el LED
	
	
while(True):						# Este bloque se ejecutara de manera ciclica hasta que el programa sea detenido
	revisarBoton()					# Ejecutar la funcion revisarBoton
