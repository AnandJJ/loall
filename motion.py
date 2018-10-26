import os
import RPi.GPIO as g #import rpi.gpio module
import time
g.setmode(g.BCM) 
pirpin=2
g.setup(pirpin,g.IN)
a=1
time.sleep(1)
while a<=5:
    if g.input(pirpin):
        print("motion detected")
        os.system("fswebcam -F 4 --fps 20 -r 800*600 /home/pi/sagar/"+str(a)+".jpg")
        print("DONE")
        time.sleep(1)
        a=a+1
print("testing")
exit()            
                  

