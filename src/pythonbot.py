from machine import Pin, PWM, UART
from utime import sleep
import uos

#create the uart connection for bluetooth communication
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
    
#defining pins
led = Pin(25,Pin.OUT)

PWMA1 = PWM(Pin(10))
AIN2 = Pin(11, Pin.OUT)
AIN1 = Pin(12,Pin.OUT)

BIN1 = Pin(13,Pin.OUT)
BIN2 = Pin(14, Pin.OUT)
PWMB1 = PWM(Pin(15))


PWMA2 = PWM(Pin(16))
AIN4 = Pin(17, Pin.OUT)
AIN3 = Pin(18,Pin.OUT)

BIN3 = Pin(19,Pin.OUT)
BIN4 = Pin(20, Pin.OUT)
PWMB2 = PWM(Pin(21))

#set motor pulse width modulation (PWM) frequency to 1000 cycles/sec
PWMA1.freq(1000)
PWMB1.freq(1000)
PWMA2.freq(1000)
PWMB2.freq(1000)
    
speed = 65536

def printinfo():
    #Print system name
    print("-"*50)
    print("picoTerm>")
    print(uos.uname())
    led.value(1)
    sleep(10)

def front():
    #led indication
    led.value(1)
    #set motor direction
    AIN1.value(1)
    AIN2.value(0)
    BIN1.value(1)
    BIN2.value(0)
    AIN3.value(1)
    AIN4.value(0)
    BIN3.value(1)
    BIN4.value(0)
    #Applying voltage to the motor using pulse width modulation (PWM)
    PWMA1.duty_u16(speed)               #2^16 = 65536
    PWMB1.duty_u16(speed)
    PWMA2.duty_u16(speed)
    PWMB2.duty_u16(speed)
    
def back():
    #led indication
    led.value(1)
    #set motor direction
    AIN1.value(0)
    AIN2.value(1)
    BIN1.value(0)
    BIN2.value(1)
    AIN3.value(0)
    AIN4.value(1)
    BIN3.value(0)
    BIN4.value(1)
    #Applying voltage to the motor using pulse width modulation (PWM)
    PWMA1.duty_u16(speed)
    PWMB1.duty_u16(speed)
    PWMA2.duty_u16(speed)
    PWMB2.duty_u16(speed)

def left():
    #led indication
    led.value(1)
    #set motor direction
    AIN1.value(0)
    AIN2.value(1)
    BIN1.value(0)
    BIN2.value(1)
    AIN3.value(1)
    AIN4.value(0)
    BIN3.value(1)
    BIN4.value(0)
    #Applying voltage to the motor using pulse width modulation (PWM)
    PWMA1.duty_u16(speed)
    PWMB1.duty_u16(speed)
    PWMA2.duty_u16(speed)
    PWMB2.duty_u16(speed)
    
def right():
    #led indication
    led.value(1)
    #set motor direction
    AIN1.value(1)
    AIN2.value(0)
    BIN1.value(1)
    BIN2.value(0)
    AIN3.value(0)
    AIN4.value(1)
    BIN3.value(0)
    BIN4.value(1)
    #Applying voltage to the motor using pulse width modulation (PWM)
    PWMA1.duty_u16(speed)
    PWMB1.duty_u16(speed)
    PWMA2.duty_u16(speed)
    PWMB2.duty_u16(speed)

def leftShift():
    #led indication
    led.value(1)
    #set motor direction
    AIN1.value(0)
    AIN2.value(1)
    BIN1.value(1)
    BIN2.value(0)
    AIN3.value(1)
    AIN4.value(0)
    BIN3.value(0)
    BIN4.value(1)
    #Applying voltage to the motor using pulse width modulation (PWM)
    PWMA1.duty_u16(speed)
    PWMB1.duty_u16(speed)
    PWMA2.duty_u16(speed)
    PWMB2.duty_u16(speed)
    
def rightShift():
    #led indication
    led.value(1)
    #set motor direction
    AIN1.value(1)
    AIN2.value(0)
    BIN1.value(0)
    BIN2.value(1)
    AIN3.value(0)
    AIN4.value(1)
    BIN3.value(1)
    BIN4.value(0)
    #Applying voltage to the motor using pulse width modulation (PWM)
    PWMA1.duty_u16(speed)
    PWMB1.duty_u16(speed)
    PWMA2.duty_u16(speed)
    PWMB2.duty_u16(speed)
    
def leftDiagonalFront():
    #led indication
    led.value(1)
    #set motor direction
    AIN1.value(1)
    AIN2.value(0)
    BIN1.value(0)
    BIN2.value(0)
    AIN3.value(0)
    AIN4.value(0)
    BIN3.value(1)
    BIN4.value(0)
    #Applying voltage to the motor using pulse width modulation (PWM)
    PWMA1.duty_u16(speed)
    PWMB1.duty_u16(speed)
    PWMA2.duty_u16(speed)
    PWMB2.duty_u16(speed)
    
def rightDiagonalFront():
    #led indication
    led.value(1)
    #set motor direction
    AIN1.value(0)
    AIN2.value(0)
    BIN1.value(1)
    BIN2.value(0)
    AIN3.value(1)
    AIN4.value(0)
    BIN3.value(0)
    BIN4.value(0)
    #Applying voltage to the motor using pulse width modulation (PWM)
    PWMA1.duty_u16(speed)
    PWMB1.duty_u16(speed)
    PWMA2.duty_u16(speed)
    PWMB2.duty_u16(speed)
    
def leftDiagonalBack():
    #led indication
    led.value(1)
    #set motor direction
    AIN1.value(0)
    AIN2.value(1)
    BIN1.value(0)
    BIN2.value(0)
    AIN3.value(0)
    AIN4.value(0)
    BIN3.value(0)
    BIN4.value(1)
    #Applying voltage to the motor using pulse width modulation (PWM)
    PWMA1.duty_u16(speed)
    PWMB1.duty_u16(speed)
    PWMA2.duty_u16(speed)
    PWMB2.duty_u16(speed)
    
def rightDiagonalBack():
    #led indication
    led.value(1)
    #set motor direction
    AIN1.value(0)
    AIN2.value(0)
    BIN1.value(0)
    BIN2.value(1)
    AIN3.value(0)
    AIN4.value(1)
    BIN3.value(0)
    BIN4.value(0)
    #Applying voltage to the motor using pulse width modulation (PWM)
    PWMA1.duty_u16(speed)
    PWMB1.duty_u16(speed)
    PWMA2.duty_u16(speed)
    PWMB2.duty_u16(speed)


def stop():
    #led indication
    led.value(0)
    #set motor direction
    AIN1.value(0)
    AIN2.value(0)
    BIN1.value(0)
    BIN2.value(0)
    AIN3.value(0)
    AIN4.value(0)
    BIN3.value(0)
    BIN4.value(0)
    led.value(0)
    #Applying voltage to the motor using pulse width modulation (PWM)
    PWMA1.duty_u16(0)
    PWMB1.duty_u16(0)
    PWMA2.duty_u16(0)
    PWMB2.duty_u16(0)

def main():
    printinfo()               #printing the board details
    global speed               #To access the global speed variable
    while True:
        if uart.any():       #Checking if data available
            data = uart.read()#Getting data
            if('F' in data):   #Front
                front()
                print("Front:",speed)
            elif('B' in data): #Back
                back()
                print("Back: ",speed)
            elif('R' in data): #Right
                right()
                print("Right: ",speed)
            elif('L' in data): #Left
                left()
                print("Left: ",speed)
            elif('I' in data): #Right Diagonal Front
                rightDiagonalFront()
                print("Right Diagonal Front: ",speed)
            elif('G' in data): #Left Diagonal Front
                leftDiagonalFront()
                print("Left Diagonal Front: ",speed)
            elif('H' in data): #Left Diagonal Back
                leftDiagonalBack()
                print("Left Diagonal Back: ",speed)
            elif('J' in data): #Right Diagonal Back
                rightDiagonalBack()
                print("Right Diagonal Back: ",speed)
            elif('W' in data): #Left shift
                leftShift()
                print("Left Shift: ",speed)
            elif('U' in data): #Right shift
                rightShift()
                print("Right Shift: ",speed)
            #speed is between 0-65536 as it has 16 bit pwm registers so 2^16 = 65536
            elif('0' in data): #speed = 115
                speed = 0
            elif('1' in data): #speed = 130
                speed = 6553
            elif('2' in data): #speed = 143
                speed = 13107
            elif('3' in data): #speed = 157
                speed = 19660
            elif('4' in data): #speed = 170
                speed = 26214
            elif('5' in data): #speed = 185
                speed = 32768
            elif('6' in data): #speed = 200
                speed = 39321
            elif('7' in data): #speed = 213
                speed = 45875
            elif('8' in data): #speed = 227
                speed = 52428
            elif('9' in data): #speed = 240
                speed = 58982
            elif('q' in data): #speed = 255
                speed = 65536
            else:
                stop()    #Stop
                print("Stop: ",speed)
            
if __name__=='__main__':
    main()

