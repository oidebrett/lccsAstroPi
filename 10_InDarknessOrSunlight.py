from time import sleep
from orbit import ISS
from skyfield.api import load

ephemeris =load('de421.bsp')
timescale = load.timescale()

for i in range (1,5):
    t =timescale.now()
    if ISS.at(t).is_sunlit(ephemeris):
       print("In sunlight")
    else:
       print ("in darkness")
