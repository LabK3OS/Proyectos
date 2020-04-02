#!/usr/bin/env python
# -*- coding: utf-8 -*- 


import RPi.GPIO as GPIO       				# Con esta libreria, traemos las herramientas necesarias para poder utilizar las conexiones fisicas de K3OS            
import time									# Con esta libreria, traemos las herramientas necesarias, para poder esperar una cantidad de tiempo determinada dentro de nuestro programa
import max7219.led as Disp   				# con esta libreria, traemos las herramientas necesarias, para facilitar la comunicacion con la matriz 

#Configuramos los pines externos

GPIO.setwarnings(False)						# Deshabilitar la alertas de GPIO
GPIO.setmode(GPIO.BCM)  					# Configuracion inicial de pines
	

Matriz = Disp.matrix()						# Inicializar matriz


dat={'0','1','2','3','4','5','6','7','8','9'}
	
while(True):								# Este bloque se ejecutara de manera ciclica hasta que el programa sea detenido
	for x in dat:
		print(x)
		Matriz.show_message(x)
		time.sleep(1)
		Matriz.show_message("Hello world!")
		time.sleep(1)
