from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

r = (255,0,0)
w = (255,255,255)

small_heart = [
    w,w,w,w,w,w,w,w,
    w,r,r,w,w,r,r,w,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    w,r,r,r,r,r,r,w,
    w,w,r,r,r,r,w,w,
    w,w,w,r,r,w,w,w,
    w,w,w,w,w,w,w,w
]

big_heart = [
    w,r,r,w,w,r,r,w,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    w,r,r,r,r,r,r,w,
    w,w,r,r,r,r,w,w,
    w,w,w,r,r,w,w,w
]
while True:
    sense.set_pixels(small_heart)
    sleep(.5)
    sense.set_pixels(big_heart)
    sleep(.5)

