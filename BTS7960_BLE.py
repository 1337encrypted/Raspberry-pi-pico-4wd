from machine import Pin, PWM, UART
from utime import sleep
import uos

#create the uart
#uart = UART(id,baudrate,tx,rx)
uart0 = UART(0, baudrate=9600, tx=Pin(12), rx=Pin(13))

#defining pins
led = Pin(25,Pin.OUT)
redLed = Pin(0,Pin.OUT)
blueLed = Pin(28,Pin.OUT)
buzzerPin = Pin(16,Pin.OUT)

LPWM1 = PWM(Pin(2))
RPWM1 = PWM(Pin(3))
L_EN1 = Pin(4,Pin.OUT)
R_EN1 = Pin(5, Pin.OUT)

LPWM2 = PWM(Pin(18))
RPWM2 = PWM(Pin(19))
L_EN2 = Pin(20,Pin.OUT)
R_EN2 = Pin(21, Pin.OUT)

# frequency for the motors
f = 10000

RPWM1.freq(f)
LPWM1.freq(f)
RPWM2.freq(f)
LPWM2.freq(f)
    
#speed = 65536
speed = 32768

def printinfo():
    #Print system name
    print("-"*50)
    print("picoTerm>")
    print(uos.uname())
    buzzerPin.value(1)
    led.value(1)
    redLed.value(1)
    blueLed.value(1)
    sleep(1)
    buzzerPin.value(0)
    led.value(0)
    redLed.value(1)
    blueLed.value(0)

def front():
    #Color indicator for the motor
    #led.value(1)
    redLed.value(0)
    blueLed.value(1)
    #Set the directions
    L_EN1.value(1)
    R_EN1.value(1)
    L_EN2.value(1)
    R_EN2.value(1)
    #Applying voltage to the motor using pulse width modulation (PWM)
    RPWM1.duty_u16(speed)
    LPWM1.duty_u16(0)
    RPWM2.duty_u16(0)
    LPWM2.duty_u16(speed)
    
def back():
    #Color indicator for the motor
    #led.value(1)
    redLed.value(0)
    blueLed.value(1)
    #Set the directions
    L_EN1.value(1)
    R_EN1.value(1)
    L_EN2.value(1)
    R_EN2.value(1)
    #Applying voltage to the motor using pulse width modulation (PWM)
    RPWM1.duty_u16(0)
    LPWM1.duty_u16(speed)
    RPWM2.duty_u16(speed)
    LPWM2.duty_u16(0)

def leftFront():
    #Color indicator for the motor
    #led.value(1)
    redLed.value(0)
    blueLed.value(1)
    #Set the directions
    L_EN1.value(0)
    R_EN1.value(0)
    L_EN2.value(1)
    R_EN2.value(1)
    #Applying voltage to the motor using pulse width modulation (PWM)
#    RPWM1.duty_u16(0)
#    LPWM1.duty_u16(speed)
    RPWM2.duty_u16(0)
    LPWM2.duty_u16(speed)

def leftBack():
    #Color indicator for the motor
    #led.value(1)
    redLed.value(0)
    blueLed.value(1)
    #Set the directions
    L_EN1.value(0)
    R_EN1.value(0)
    L_EN2.value(1)
    R_EN2.value(1)
    #Applying voltage to the motor using pulse width modulation (PWM)
#    RPWM1.duty_u16(0)
#    LPWM1.duty_u16(speed)
    RPWM2.duty_u16(speed)
    LPWM2.duty_u16(0)



def rightFront():
    #Color indicator for the motor
    #led.value(1)
    redLed.value(0)
    blueLed.value(1)
    #Set the directions
    L_EN1.value(1)
    R_EN1.value(1)
    L_EN2.value(0)
    R_EN2.value(0)
    #Applying voltage to the motor using pulse width modulation (PWM)
    RPWM1.duty_u16(0)
    LPWM1.duty_u16(speed)
#     RPWM2.duty_u16(speed)
#     LPWM2.duty_u16(0)

def rightBack():
    #Color indicator for the motor
    #led.value(1)
    redLed.value(0)
    blueLed.value(1)
    #Set the directions
    L_EN1.value(1)
    R_EN1.value(1)
    L_EN2.value(0)
    R_EN2.value(0)
    #Applying voltage to the motor using pulse width modulation (PWM)
    RPWM1.duty_u16(speed)
    LPWM1.duty_u16(0)
#     RPWM2.duty_u16(speed)
#     LPWM2.duty_u16(0)
    
# def sharpRightFront():
#     #Color indicator for the motor
#     #led.value(1)
#     redLed.value(0)
#     blueLed.value(1)
#
#
#     #Applying voltage to the motor using pulse width modulation (PWM)
#     RPWM1.duty_u16(0)
#     LPWM1.duty_u16(0)
#     RPWM2.duty_u16(speed)
#     LPWM2.duty_u16(0)
#      
# def sharpRightBack():
#     #Color indicator for the motor
#     #led.value(1)
#     redLed.value(0)
#     blueLed.value(1)
#     #Applying voltage to the motor using pulse width modulation (PWM)
#     RPWM1.duty_u16(0)
#     LPWM1.duty_u16(0)
#     RPWM2.duty_u16(0)
#     LPWM2.duty_u16(speed)
# 
# def sharpLeftFront():
#     #Color indicator for the motor
#     #led.value(1)
#     redLed.value(0)
#     blueLed.value(1)
#     #Applying voltage to the motor using pulse width modulation (PWM)
#     RPWM1.duty_u16(0)
#     LPWM1.duty_u16(speed)
#     RPWM2.duty_u16(0)
#     LPWM2.duty_u16(0)
#     
# def sharpLeftBack():
#     #Color indicator for the motor
#     led.value(1)
#     redLed.value(0)
#     blueLed.value(1)
#     #Applying voltage to the motor using pulse width modulation (PWM)
#     RPWM1.duty_u16(speed)
#     LPWM1.duty_u16(0)
#     RPWM2.duty_u16(0)
#     LPWM2.duty_u16(0)
    

def stop():
    #Color indicator for the motor
    led.value(0)
    redLed.value(1)
    blueLed.value(0)
    #Applying voltage to the motor using pulse width modulation (PWM)
    RPWM1.duty_u16(0)
    LPWM1.duty_u16(0)
    RPWM2.duty_u16(0)
    LPWM2.duty_u16(0)
    print("Stop: ",speed)

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
                #front()
                front()
                print("Front:",speed)
            elif('B' in data):  #Backward
                back()
                print("Back: ",speed)
            elif('L' in data):  #Turn Left
                leftFront()
                print("Left Front: ",speed)
            elif('R' in data):  #Turn Right
                rightFront()
                print("Right Front: ",speed)
            elif('G' in data):  #Sharp Left Front
                rightBack()
                print("Right Back: ",speed)
#            elif('H' in data):  #Sharp Left Back
#                sharpLeftBack()
#                print("Sharp Left Back: ",speed)
            elif('I' in data):  #Sharp Right Front
                leftBack()
                print("Left Back: ",speed)
#             elif('J' in data):  #Sharp Right Back
#                 leftBack()
#                 print("Left Back: ",speed)
            elif('0' in data):  #speed = 115
                speed = 0
            elif('1' in data):  #speed = 130
                speed = 6553
                led.value(1)
                buzzerPin.value(1)
            elif('2' in data):  #speed = 143
                speed = 13107
                led.value(0)
                buzzerPin.value(0)
            elif('3' in data):  #speed = 157
                speed = 19660
                led.value(0)
                buzzerPin.value(0)
            elif('4' in data):  #speed = 170
                speed = 26214
                led.value(0)
                buzzerPin.value(0)
            elif('5' in data):  #speed = 185
                speed = 32768
                led.value(0)
                buzzerPin.value(0)
            elif('6' in data):  #speed = 200
                speed = 39321
                led.value(0)
                buzzerPin.value(0)
            elif('7' in data):  #speed = 213
                speed = 45875
                led.value(0)
                buzzerPin.value(0)
            elif('8' in data):  #speed = 227
                speed = 52428
                led.value(0)
                buzzerPin.value(0)
            elif('9' in data):  #speed = 240
                speed = 58982
                led.value(0)
                buzzerPin.value(0)
            elif('q' in data):  #speed = 255
                speed = 65536
                led.value(0)
                buzzerPin.value(0)
            elif('S' in data):
                stop()         #Stop

            
if __name__=='__main__':
    main()
