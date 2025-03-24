#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

Buzzer = 32 #Define the pin of the buzzer

GPIO.setwarnings(False) #Ignore warning

REST = 0
NOTE_C4 = 262
NOTE_D4 = 294
NOTE_E4 = 330
NOTE_F4 = 349
NOTE_G4 = 392 
NOTE_A4 = 440
NOTE_AS4 = 466 
NOTE_B4 = 494

NOTE_C5 = 523
NOTE_D5 = 587
NOTE_E5 = 659
NOTE_F5 = 698
NOTE_G5 = 784
NOTE_A5 = 880
NOTE_B5 = 988

raya_song = [ 
  NOTE_F4, 8, NOTE_G4, 8, NOTE_A4, 2, NOTE_F4, 8, NOTE_G4, 8, NOTE_F4, 8, NOTE_E4, 2, NOTE_C4, 8, 
  NOTE_E4, 8, NOTE_F4, 8, NOTE_G4, 8, NOTE_F4, 8, NOTE_G4, 8, NOTE_A4, 8, NOTE_AS4, 8, NOTE_D5, 8, 
  NOTE_C5, 8, NOTE_AS4, 8, NOTE_A4, 2, REST, 2, NOTE_F4, 8, NOTE_G4, 8, NOTE_A4, 2, NOTE_F4, 8, 
  NOTE_G4, 8, NOTE_A4, 8, NOTE_C5, 4, NOTE_AS4, 4 , NOTE_G4, 8, NOTE_A4, 8, NOTE_AS4, 8, NOTE_A4, 8, 
  NOTE_F4, 8, NOTE_G4, 8, NOTE_A4, 8, NOTE_G4, 8, NOTE_E4, 8, NOTE_F4, 8, NOTE_G4, 8, NOTE_F4, 2, REST, 2, 
  NOTE_F4, 8, NOTE_G4, 8, NOTE_A4, 8, NOTE_AS4, 4, NOTE_G4, 8, NOTE_A4, 8, NOTE_AS4, 8, NOTE_C5, 8, 
  NOTE_D5, 8, NOTE_E5, 8, NOTE_F5, 8, NOTE_C5, 8, NOTE_A4, 8, NOTE_G4, 8, NOTE_F4, 4 , NOTE_E4, 8, 
  NOTE_D4, 8, NOTE_C4, 8, NOTE_D4, 8, NOTE_E4, 8, NOTE_F4, 8, NOTE_G4, 8, NOTE_A4, 8, NOTE_AS4, 8, 
  NOTE_A4, 8, NOTE_C5, 2, REST, 8, NOTE_F4, 8, NOTE_G4, 8, NOTE_A4, 8, NOTE_AS4, 4, NOTE_G4, 8, NOTE_A4, 8, 
  NOTE_AS4, 8, NOTE_C5, 8, NOTE_D5, 8, NOTE_E5, 8, NOTE_F5, 8, NOTE_C5, 8, NOTE_A4, 8, NOTE_G4, 8, 
  NOTE_F4, 4, NOTE_E4, 8, NOTE_D4, 8, NOTE_C4, 8, NOTE_D4, 8, NOTE_E4, 8, NOTE_F4, 8, NOTE_G4, 8, 
  NOTE_AS4, 8, NOTE_A4, 8, NOTE_G4, 8, NOTE_F4, 2, REST, 8, NOTE_F4, 8, NOTE_G4, 8, NOTE_A4, 2, NOTE_F4, 8, 
  NOTE_G4, 8, NOTE_F4, 8, NOTE_E4, 2, NOTE_C4, 8, NOTE_E4, 8, NOTE_F4, 8, NOTE_G4, 8, NOTE_F4, 8, NOTE_G4, 8, 
  NOTE_A4, 8, NOTE_AS4, 8, NOTE_D5, 8, NOTE_C5, 8, NOTE_AS4, 8, NOTE_A4, 2, REST, 2, NOTE_F4, 8, NOTE_G4, 8, 
  NOTE_A4, 2, NOTE_F4, 8, NOTE_G4, 8, NOTE_A4, 8, NOTE_C5, 4, NOTE_AS4, 4, NOTE_G4, 8, NOTE_A4, 8, NOTE_AS4, 8, 
  NOTE_A4, 8, NOTE_F4, 8, NOTE_G4, 8, NOTE_A4, 8, NOTE_G4, 8, NOTE_E4, 8, NOTE_F4, 8, NOTE_G4, 8, NOTE_F4, 2 
]

def setup():
	GPIO.setmode(GPIO.BOARD)      #Set the GPIO port to BIARD encoding mode    
	GPIO.setup(Buzzer, GPIO.OUT)  #The pin of the buzzer is set to output mode
	global Buzz                                            
	Buzz = GPIO.PWM(Buzzer, 440)   
	Buzz.start(50) 

def run():
	for i in range(0, len(raya_song), 2):	
		fre = raya_song[i]
		note = raya_song[i+1]
		dur = (4 / note) * 0.5
		print(i,fre,note,dur)
		if fre>0:
			Buzz.ChangeFrequency(fre)	
			time.sleep(dur)	
		else:
			Buzz.stop()
			time.sleep(dur)	
			Buzz.start(50) 

if __name__ == '__main__':		
	setup()
	try:
		run()
	except KeyboardInterrupt:  	
		GPIO.cleanup()
		print("Ending")
