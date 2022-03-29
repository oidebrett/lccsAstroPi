#Use the builtin emulator
#See: https://sense-emu.readthedocs.io/en/v1.1/

from sense_emu import SenseHat
from time import sleep
sense = SenseHat()

#set up the predefined colours (letters now):
black=(0,0,0)
b=(0,0,255)
g=(0,255,0)
r=(255,0,0)

while True:
    t = sense.get_temperature()
    t = round(t,1)
    print(t)
    if (t>18.3):


elif (t>26.7):
        sense.show_message(str(t), text_colour = b, back_colour=r, scroll_speed=0.05)
    else:
        sense.show_message(str(t), text_colour = b, back_colour=g, scroll_speed=0.05)
    
    sleep(1)
