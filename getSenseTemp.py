from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

t = sense.get_temperature()
t = round(t,1)
print(t)

sense.show_message(str(t))