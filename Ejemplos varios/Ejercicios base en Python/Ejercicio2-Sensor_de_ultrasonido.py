#!/usr/bin/env python
# -*- coding: utf-8 -*- 


import RPi.GPIO as GPIO       				# Con esta libreria, traemos las herramientas necesarias para poder utilizar las conexiones fisicas de K3OS            
import time									# Con esta libreria, traemos las herramientas necesarias, para poder esperar una cantidad de tiempo determinada dentro de nuestro programa


#Configuramos los pines externos

GPIO.setwarnings(False)						# Deshabilitar la alertas de GPIO
GPIO.setmode(GPIO.BCM)  					# Configuracion inicial de pines
LED1 = 12									# pin GPIO 12 como LED1, el pin donde se encuentra conectado el LED
TRIG = 23                           		# pin GPIO 23 como TRIG, conectado al sensor de ultrasonido
ECHO = 24                           		# pin GPIO 24 como ECHO, conectado al sensor de ultrasonido
V    = 34300			    				# Velocidad del sonido 34300cm/s, este valor es requerido para calcular la distancia a la que se encuentra el objeto detectado

GPIO.setup(LED1,GPIO.OUT)					# Configuramos el pin del led como salida
GPIO.setup(TRIG,GPIO.OUT)           		# TRIG como salida
GPIO.setup(ECHO,GPIO.IN)            		# ECHO como entrada

# Iniciar sensor
GPIO.output(TRIG, False)            		# TRIG en estado bajo
time.sleep(2)                       		# Esperar 2 segundos, para que el sensor se estabilice


	
def distancia():
	# Mandar pulso de 0.00001 segundos
	GPIO.output(TRIG, True)          		# TRIG en estado alto
	time.sleep(0.00001)               		# Delay de 0.00001 segundos
	GPIO.output(TRIG, False)          		# TRIG en estado bajo
  
	# Medir pulso
  
	while GPIO.input(ECHO)==0:        		# Comprueba si ECHO está en estado bajo
		tiempoInicial = time.time()    		# Guarda el tiempo actual en tiempoInicial
  
	while GPIO.input(ECHO)==1:        		# Comprueba si ECHO está en estado alto
		tiempoFinal = time.time()      		# Guarda el tiempo actual, en tiempo Final
  
	# Calculo de distancia
	
	tiempoPulso = tiempoFinal-tiempoInicial	# Se obtienen la duración del pulso, calculando la diferencia entre tienpoFinal y tiempoInicial
	distancia = t * (V/2)                   # Se multiplica la duración del pulso, por la velocidad del sonido para obetener la distancia 
	distancia = round(distancia, 2)        	# Se redondea a dos decimales
	
	# Nota: La distancia se divide en  2, para tener en cuenta el tiempo deida y vuelta

	return distancia


	
while(True):								# Este bloque se ejecutara de manera ciclica hasta que el programa sea detenido
	dt=distancia()
	print("distancia"+dt)
	if(dt<400):
		GPIO.output(LED1, True)				# Encender el LED
	else:
		GPIO.output(LED1, True)				# Apagar el LED

