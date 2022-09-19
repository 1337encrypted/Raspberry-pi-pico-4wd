<h1><b><center>OMNIDIRECTIONAL ROBOT</center></b><h1>
<h2>FUNCTIONS</h2>
<pre>
<b>front:</b> Moves the robot forward in y axis.
<b>back:</b> Moves the robot backward in the y axis.
<b>left:</b> Turns the robot in the left direction.
<b>rightDiagonalFront:</b> Moves diagonally in positive X axis and positive Y axis
<b>rightDiagonalBack:</b> Moves diagonally in positive X and negative Y axis
<b>leftDiagonalFront:</b> Moves diagonally in negative X and positive Y axis
<b>leftDiagonalBack:</b> Moves diagonally in negative X and negative Y axis
<b>right:</b> Turns the robot in the right direction.
<b>rightShift:</b> Slides the robot to right in the x axis.
<b>printInfo:</b> Prints system name and embedded operating system name
<b>changeSpeed:</b>  Updates the global speed variable ranging from 1-10 speeds
<b>stop:</b> Stop all the motors
</pre>

<h2>HARDWARE</h2>
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
</table>

<h2>METHODOLOGY</h2>
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

<h2>ALGORITHM</h2>
<pre>
Step1: Start                                            
Step2: Print system info
Step3: Initialise global variables and uart objects
Step4: while True
Step5: if uart.any()
Step4: data <= uart.read()
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
</pre>
