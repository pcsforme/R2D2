import time 
import random
from gpiozero import PWMLED
import buzztone

blue = PWMLED(14)
red = PWMLED(15)
buzzer = buzztone.Buzzer()

while True:
    tone = random.randint(1,5)
    delay = (random.randint(0,10))/10
    delay2 = (random.randint(0,30))/10
    red.on()
    blue.on()
    buzzer.play(tone)
    time.sleep(delay)
    blue.off()
    red.off()
    time.sleep(delay2)
    

