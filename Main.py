import datetime
from distutils.util import execute
from threading import Timer
import threading
from math import sin,cos,sqrt
from sense_hat import SenseHat
import time
from orbit import ISS
from time import sleep
with open ("dataSAFE.csv", "w") as file:
    file.write("time , latitude , longitude , elevation, acceleration \n")

def tid():
    now = datetime.datetime.now()
    print("Klokken er :")
    print(now.strftime("%y-%m-%d %H:%M:%S"))
#    threading.Timer(5.0,tid).start()
    return now.strftime("%y-%m-%d %H:%M:%S")
tid()

sense = SenseHat()
def acc():
    accelerometer_data = sense.get_accelerometer_raw()
    x1 = accelerometer_data['x']
    y1 = accelerometer_data['y']
    z1 = accelerometer_data['z']

    a_samlet = (x1**2+y1**2+z1**2)**0.5*9.82    
    print(f"X1:{x1}")
    print(f"Y1:{y1}")
    print(f"Z1:{z1}")

#    threading.Timer(5.0,acc).start()
    return a_samlet
acc()

def loc():
    location = ISS.coordinates() # Equivalent to ISS.at(timescale.now()).subpoint()
    print(f"X: {location.latitude.degrees}")
    print(f"Y: {location.longitude.degrees}")
    print(f"Z: {location.elevation.m}")
#    threading.Timer(5.0,loc).start()
    return tid(),location.latitude.degrees,location.longitude.degrees,location.elevation.m, acc()
i=0
while i<12:
    with open ("dataSAFE.csv","a") as file:
        file.write("%s,%s,%s,%s,%s \n" % (loc()))
    print('gemmer')
    sleep(5)
    i+=1
    

    

    
#posx=[]
#phi=location.latitude.degrees
#Tetha=location.longitude.degrees
#r=location.elevation.m
#print(r)
#x= r*sin(Tetha)*cos(Phi)
#posx.append(x)
#print(posx)

        