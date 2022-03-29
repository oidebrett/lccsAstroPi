from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

#set up the predefined colours:
blue=(0,0,255)
yellow=(255,255,0)
red=(255,0,0)

#set colours and scroll speed
sense.show_message("Hello_Earth", text_colour = blue, back_colour=yellow, scroll_speed=0.05)

#Show letter
sense.show_letter('J')
sleep(1)
sense.show_letter('P')
sleep(1)

#Clear the screen
sense.clear()

#Show pixels
#(0,0) (1,0) (2,0)
#(0,1) (1,1) (2,1)
#(0,2) (1,2) (2,2)
#(0,3) (1,3) (2,3)
sense.set_pixel(0,3,red)

#set up the predefined colours (letters now):
b=(0,0,255)
y=(255,255,0)
r=(255,0,0)

#create image
image =[
    y,y,y,y,y,y,y,y,
    y,b,b,y,y,b,b,y,
    y,b,b,y,y,b,b,y,
    y,y,y,y,r,y,y,y,
    y,y,y,r,r,y,y,y,
    y,b,y,y,y,y,b,y,
    y,y,b,y,y,b,y,y,    
    y,y,y,b,b,y,y,y    
]
sense.set_pixels(image)


#exit()
