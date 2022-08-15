from machine import Pin, PWM, UART
from utime import sleep
import uos

#create the uart
#uart = UART(id,baudrate,tx,rx)
uart0 = UART(0, baudrate=9600, tx=Pin(12), rx=Pin(13))
    
#defining pins
led = Pin(25,Pin.OUT)

LPWM1 = PWM(Pin(2))
RPWM1 = PWM(Pin(3))
L_EN1 = Pin(4,Pin.OUT)
R_EN1 = Pin(5, Pin.OUT)

LPWM2 = PWM(Pin(18))
RPWM2 = PWM(Pin(19))
L_EN2 = Pin(20,Pin.OUT)
R_EN2 = Pin(21, Pin.OUT)


RPWM1.freq(1000)
LPWM1.freq(1000)
RPWM2.freq(1000)
LPWM2.freq(1000)

L_EN1.value(1)
R_EN1.value(1)
L_EN2.value(1)
R_EN2.value(1)
    
speed = 65536

def printinfo():
    #Print system name
    print("-"*50)
    print("picoTerm>")
    print(uos.uname())
    led.value(1)

def front():
    #Applying voltage to the motor using pulse width modulation (PWM)
    RPWM1.duty_u16(0)
    LPWM1.duty_u16(speed)
    RPWM2.duty_u16(0)
    LPWM2.duty_u16(speed)
    
def back():
    #Applying voltage to the motor using pulse width modulation (PWM)
    RPWM1.duty_u16(speed)
    LPWM1.duty_u16(0)
    RPWM2.duty_u16(speed)
    LPWM2.duty_u16(0)

def left():
    #Applying voltage to the motor using pulse width modulation (PWM)
    RPWM1.duty_u16(0)
    LPWM1.duty_u16(speed)
    RPWM2.duty_u16(speed)
    LPWM2.duty_u16(0)
    
def right():
    #Applying voltage to the motor using pulse width modulation (PWM)
    RPWM1.duty_u16(speed)
    LPWM1.duty_u16(0)
    RPWM2.duty_u16(0)
    LPWM2.duty_u16(speed)

def sharpRightFront():
    #Applying voltage to the motor using pulse width modulation (PWM)
    RPWM1.duty_u16(0)
    LPWM1.duty_u16(0)
    RPWM2.duty_u16(0)
    LPWM2.duty_u16(speed)
    
def sharpRightBack():
    #Applying voltage to the motor using pulse width modulation (PWM)
    RPWM1.duty_u16(0)
    LPWM1.duty_u16(speed)
    RPWM2.duty_u16(0)
    LPWM2.duty_u16(0)

def sharpLeftFront():
    #Applying voltage to the motor using pulse width modulation (PWM)
    RPWM1.duty_u16(0)
    LPWM1.duty_u16(speed)
    RPWM2.duty_u16(0)
    LPWM2.duty_u16(0)
    
def sharpLeftBack():
    #Applying voltage to the motor using pulse width modulation (PWM)
    RPWM1.duty_u16(0)
    LPWM1.duty_u16(0)
    RPWM2.duty_u16(speed)
    LPWM2.duty_u16(0)
    

def stop():
    #Applying voltage to the motor using pulse width modulation (PWM)
    RPWM1.duty_u16(0)
    LPWM1.duty_u16(0)
    RPWM2.duty_u16(0)
    LPWM2.duty_u16(0)
    print("Stop: 0")

#def setup_uart():             #setup the uart for bluetooth connection
    

def main():
    printinfo()                 #printing the board details
    global speed
    while True:
        if uart0.any():         #Checking if data available
            data = uart0.read() #Getting data
            #data = str(data)
            #stop()             #Stop
            #print(data)
            if('F' in data):    #Forward
                front()
                print("Front:",speed)
            elif('B' in data):  #Backward
                back()
                print("Back: ",speed)
            elif('L' in data):  #Turn Left
                left()
                print("Left: ",speed)
            elif('R' in data):  #Turn Right
                right()
                print("Right: ",speed)
            elif('G' in data):  #Sharp Left Front
                sharpLeftFront()
                print("Sharp Left Front: ",speed)
            elif('H' in data):  #Sharp Left Back
                sharpLeftBack()
                print("Sharp Left Back: ",speed)
            elif('I' in data):  #Sharp Right Front
                sharpRightFront()
                print("Sharp Right Front: ",speed)
            elif('J' in data):  #Sharp Right Back
                sharpRightBack()
                print("Sharp Right Back: ",speed)
            elif('0' in data):  #speed = 115
                speed = 0
            elif('1' in data):  #speed = 130
                speed = 6553
            elif('2' in data):  #speed = 143
                speed = 13107
            elif('3' in data):  #speed = 157
                speed = 19660
            elif('4' in data):  #speed = 170
                speed = 26214
            elif('5' in data):  #speed = 185
                speed = 32768
            elif('6' in data):  #speed = 200
                speed = 39321
            elif('7' in data):  #speed = 213
                speed = 45875
            elif('8' in data):  #speed = 227
                speed = 52428
            elif('9' in data):  #speed = 240
                speed = 58982
            elif('q' in data):  #speed = 255
                speed = 65536
            else:
                stop()          #Stop
            
if __name__=='__main__':
    main()
