import sys
from urllib.request import urlopen
from sense_hat import SenseHat
sense = SenseHat()

# Take readings from all three sensors
t = sense.get_temperature()
p = sense.get_pressure()
h = sense.get_humidity()
           

while True:
    t = sense.get_temperature()
    print(t)
    f=urlopen("https://api.thingspeak.com/update?api_key=W6KNF9AQE600Q6WQ&field1="+str(t))
    print(f.read())
    f.close()
