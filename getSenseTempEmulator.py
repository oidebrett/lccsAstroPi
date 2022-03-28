#Use the builtin emulator
#See: https://sense-emu.readthedocs.io/en/v1.1/

from sense_emu import SenseHat
from time import sleep
sense = SenseHat()

while True:
    t = sense.get_temperature()
    t = round(t,1)
    print(t)
    sense.show_message(str(t))
    sleep(1)

