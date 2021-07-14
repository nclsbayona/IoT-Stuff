from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_led import GroveLed
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from time import sleep
try:
    CounterFitConnection.init()
    light_sensor=GroveLightSensor(1)
    led=GroveLed(5)
    sense=GroveLightSensor(2)
    while(sense.light>300):
            light=light_sensor.light
            print ("Light level on the sensor is:", light)
            if (light>=300):
                led.off()
            else:
                led.on()
            sleep(1)
except:
    print ("Bye")