<h1>OMNIDIRECTIONAL ROBOT<h1>
<h2>FUNCTIONS<h2>
<pre>
front: Moves the robot forward in y axis.
back: Moves the robot backward in the y axis.
left: Turns the robot in the left direction.
rightDiagonalFront: Moves diagonally in positive X axis and positive Y axis
rightDiagonalBack: Moves diagonally in positive X and negative Y axis
leftDiagonalFront: Moves diagonally in negative X and positive Y axis
leftDiagonalBack: Moves diagonally in negative X and negative Y axis
right: Turns the robot in the right direction.
leftShift: Slides the robot to left in the x axis.
rightShift: Slides the robot to right in the x axis.
printInfo: Prints system name and embedded operating system name
changeSpeed:  Updates the global speed variable ranging from 1-10 speeds
stop: Stop all the motors
<pre>

<h1>HARDWARE<h1>
<table>
<tr>
    <td>Name</td>
    <td>Quantity</td>
    <td>Description</td>
</tr>
<tr>
    <td>Raspberry pi pico RP2040 microcontroller</td>
    <td>1</td>
    <td>control the motors and sensors</td>
</tr>
<tr>
    <td>12v DC Geared Motors</td>
    <td>4</td>
    <td>300 rpm</td>
</tr>
<tr>
    <td>Dual tb6612fng</td>
    <td>2</td>
    <td>H bridge for motor control</td>
</tr>
<tr>
    <td>Lipo Battery</td>
    <td>1</td>
    <td>Power supply 2200 mah</td>
</tr>
<tr>
    <td>Mecanum wheels</td>
    <td>4</td>
    <td>Omnidirectional wheels</td>
</tr>  
<!--<tr>-->
<!--    <td></td>-->
<!--    <td></td>-->
<!--    <td></td>-->
<!--    <td></td>-->
<!--    <td></td>-->
<!--</tr>-->
</table>

<h1>METHODOLOGY<h1>
<table>
<tr>
    <th>Functions</th>
    <th>Wheel 1</th>
    <th>Wheel 2</th>
    <th>Wheel 3</th>
    <th>Wheel 4</th>
</tr>
<tr>
    <td>front</td>
    <td>↑</td>
    <td>↑</td>
    <td>↑</td>
    <td>↑</td>
</tr>
<tr>
    <td>back</td>
    <td>↓</td>
    <td>↓</td>
    <td>↓</td>
    <td>↓</td>
</tr>
<tr>
    <td>leftTurn</td>
    <td>↓</td>
    <td>↓</td>
    <td>↑</td>
    <td>↑</td>
</tr>
<tr>
    <td>rightTurn</td>
    <td>↑</td>
    <td>↑</td>
    <td>↓</td>
    <td>↓</td>
</tr>
<tr>
    <td>leftShift</td>
    <td>↓</td>
    <td>↑</td>
    <td>↑</td>
    <td>↓</td>
</tr>
<tr>
    <td>rightShift</td>
    <td>↑</td>
    <td>↓</td>
    <td>↓</td>
    <td>↑</td>
</tr>
<tr>
    <td>diagonalLeftFront</td>
    <td>↑</td>
    <td>-</td>
    <td>-</td>
    <td>↑</td>
</tr>
<tr>
    <td>diagonalRightFront</td>
    <td>-</td>
    <td>↑</td>
    <td>↑</td>
    <td>-</td>
</tr>
<tr>
    <td>diagonalLeftBack</td>
    <td>-</td>
    <td>↓</td>
    <td>↓</td>
    <td>-</td>
</tr>
<tr>
    <td>diagonalRightBack</td>
    <td>↓</td>
    <td>-</td>
    <td>-</td>
    <td>↓</td>
</tr>
<tr>
    <td>stop</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
</tr>
</table>

<h1>ALGORITHM<h1>
<pre>
Step1: Start                                            
Step2: Print system info [5][3]
Step3: Initialise global variables and uart objects    [1]
Step4: while True
Step5: if uart.any()[2]
Step4: data <= uart.read()[2]
Step4: If (‘F’ in data): front()    
Step5: elif  (‘B’ in data): back()
Step6: elif  (‘L’ in data): left()
Step7: elif  (‘R’ in data): right()
Step8: elif  (‘I’ in data): rightDiagonalFront()
Step9: elif  (‘G’ in data): leftDiagonalFront()
Step10: elif  (‘H’ in data): leftDiagonalBack()
Step11: elif  (‘J’ in data): rightDiagonalBack()
Step12: elif  (‘W’ in data): leftShift()
Step13: elif  (‘U’ in data): rightShift()
Step14: elif (‘1’ in data): speed <= 10
Step15: elif (‘2’ in data): speed <= 20
Step16: e1if (‘3’ in data): speed <= 30
Step17: elif (‘4’ in data): speed <= 40
Step18: elif (‘5’ in data): speed <= 50
Step19: elif (‘6’ in data): speed <= 60
Step20: elif (‘7’ in data): speed <= 70
Step21: elif (‘8’ in data): speed <= 80
Step22: elif (‘9’ in data): speed <= 90
Step23: elif (‘10’ in data): speed <= 100
Step24: else(): stop()
<pre>
