# Import class time from time module
from time import time
from time import sleep
from picamera import PiCamera
from pathlib import Path

base_folder = Path(__file__).parent.resolve()

print("base folder data", base_folder)

camera = PiCamera()
camera.resolution = (1296,972)
camera.start_preview(alpha=200, fullscreen=False, window=(150, 150, 640, 480))
# Camera warm-up time
sleep(2)

for i in range(0,10):
    # time() function is multiplied with 
    # 1000 to convert seconds into milliseconds.
    milliseconds = int(time() * 1000)
    camera.capture(str(milliseconds)+"image.jpg")
    sleep(2)

camera.stop_preview()
