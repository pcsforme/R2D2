import time 
import random
from gpiozero import LED
import buzztone

leds = LED(14)
buzzer = buzztone.Buzzer()

while True:
    tone = random.randint(1,5)
    delay = (random.randint(0,10))/10
    delay2 = (random.randint(0,30))/10
    leds.on()
    buzzer.play(tone)
    time.sleep(delay)
    leds.off()
    time.sleep(delay2)
    

