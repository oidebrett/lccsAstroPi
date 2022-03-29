import sys
from urllib.request import urlopen

dummyTemp = 1

while True:
    dummyTemp += 1
    if dummyTemp == 100:
        dummyTemp = 1
    print(dummyTemp)
    f=urlopen("https://api.thingspeak.com/update?api_key=W6KNF9AQE600Q6WQ&field1="+str(dummyTemp))
    print(f.read())
    f.close()
