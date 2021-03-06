from mycroft import MycroftSkill, intent_file_handler
import RPi.GPIO as GPIO
import time
from time import sleep

#Python scripts execute sequentially, meaning one line right after the other.
#The method for DC motor movement that worked in this script is to:
# 1. set the correct pins for motions
# 2. wait 3 seconds
# 3. then turn the pins all to "low", effectively killing the power at the right time.

#this is a permutation of the Python test script to drive the motors with a wireless gamepad. This takes a chunk of that code and makes it work by voice.

in1 = 17 # R Motor GPIO address
#GPIO 17 = wPi , BCM 8, phys addr = 18
in2 = 27 # R Motor GPIO address
#GPIO 27 = wPi 14, BCM 11, phys addr = 16
in3 = 23 # L Motor GPIO address
#GPIO 17 = wPi 0, BCM 17, phys addr = 11
in4 = 24 # L Motor GPIO address
#GPIO 27 = wPi 2, BCM 27, phys addr = 13
en = 25 #L motor gpio
#GPIO 8 = wPi  , BCM 
en2 = 22 #R MOTOR GPIO
#GPIO 22 = wPi 3, BCM 22, phys addr = 15
temp1=1


class TankEndo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('endo.tank.intent')
    def handle_endo_tank(self, message):
        self.speak_dialog('endo.tank')


        
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(in1,GPIO.OUT)
        GPIO.setup(in2,GPIO.OUT)
        GPIO.setup(en,GPIO.OUT)
        GPIO.setup(in3,GPIO.OUT)
        GPIO.setup(in4,GPIO.OUT)
        GPIO.setup(en2,GPIO.OUT)
        p=GPIO.PWM(en,1000)
        p2=GPIO.PWM(en2,1000)
        # tank forward
        # Motor power setup here. Just one speed.
        p.start(90)
        p2.start(95) # l motor is a little weaker on my setup.
        # Compensate with slightly more juice going to the weaker motor to help it drive straighter.
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)

        time.sleep(1.5) #This finally worked.

        #We then set all of the GPIO outputs to "low" to kill the power.
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        p.stop()
        p2.stop()
def create_skill():
    return TankEndo()

