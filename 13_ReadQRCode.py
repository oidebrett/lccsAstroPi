#
# This program uses the PI Camera to take a photo at regular intervals
# and uses Open CV (image processing) to decode the QR code data
# This program assumes the data is a URL and when data is found a
# browser is opened to the url
#

# Import the modules
import os
from time import time
from time import sleep
from picamera import PiCamera
from pathlib import Path
import cv2


base_folder = Path(__file__).parent.resolve()

print("base folder data", base_folder)

camera = PiCamera()
camera.resolution = (1296,972)
camera.start_preview(alpha=200, fullscreen=False, window=(150, 150, 640, 480))
# Camera warm-up time
sleep(2)

data = ''
for i in range(0,1000):
    # time() function is multiplied with 
    # 1000 to convert seconds into milliseconds.
    milliseconds = int(time() * 1000)
    camera.capture("tempqrcodeimage.jpg")
    #sleep(0.01)
    # read the QRCODE image
    image = cv2.imread('./tempqrcodeimage.jpg')

    # initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()

    # detect and decode
    data, bbox, straight_qrcode = detector.detectAndDecode(image)

    print('.')
    if data != "":
        print("Got data")
        break
        
print(data)
cmd = "/usr/bin/chromium-browser --start-fullscreen " + data
os.system(cmd)

camera.stop_preview()
