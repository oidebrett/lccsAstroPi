from time import sleep
from picamera import PiCamera
from pathlib import Path
 
base_folder = Path(__file__).parent.resolve()
 
camera = PiCamera()
camera.resolution = (2592,1944)
camera.start_preview(alpha=200, fullscreen=False, window=(150, 150, 640, 480))
#camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture(f"{base_folder}/VHDimage.jpg")
camera.stop_preview()
