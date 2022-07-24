from machine import Pin, Timer
import time
led = Pin(25, Pin.OUT)
led1 = Pin(15, Pin.OUT)
led2 = Pin(9, Pin.OUT)
led3 = Pin(10, Pin.OUT)
timer = Timer()

def blink(timer):
    led.value(0)
    led1.value(0)
    led2.value(0)
    led3.value(0)
    for i in range(0,16,1):
        if (i%2 >= 1):
            led.value(1)
        else:
            led.value(0)
        if (i%4 >= 2):
            led1.value(1)
        else:
            led1.value(0)
        if (i%8 >= 4):
            led2.value(1)
        else:
            led2.value(0)
        if (i%16 >= 8):
            led3.value(1)
        else:
            led3.value(0)
            
        time.sleep(2)
    

timer.init(freq=1.5, mode=Timer.PERIODIC, callback=blink)

