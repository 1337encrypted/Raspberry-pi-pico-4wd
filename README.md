<h1 align="center"><strong>OMNIDIRECTIONAL ROBOT</strong><h1>
<h2>FUNCTIONS</h2>
<ol>
    <li><b>front:</b> Moves the robot forward in y axis.</li>
    <li><b>back:</b> Moves the robot backward in the y axis.</li>
    <li><b>left:</b> Turns the robot in the anti-clockwise direction.</li>
    <li><b>right:</b> Turns the robot in clockwise direction.</li>
    <li><b>rightDiagonalFront:</b> Moves diagonally in positive X axis and positive Y axis.</li>
    <li><b>rightDiagonalBack:</b> Moves diagonally in positive X and negative Y axis.</li>
    <li><b>leftDiagonalFront:</b> Moves diagonally in negative X and positive Y axis.</li>
    <li><b>leftDiagonalBack:</b> Moves diagonally in negative X and negative Y axis.</li>
    <li><b>leftShift:</b> Slides the robot to left in the x axis.</li>
    <li><b>rightShift:</b> Slides the robot to right in the x axis.</li>
    <li><b>printInfo:</b> Prints system name and embedded operating system name.</li>
    <li><b>changeSpeed:</b> Updates the global speed variable ranging from 1-10 speeds.</li>
    <li><b>stop:</b> Stop all the motors.</li>
</ol>

<h2>HARDWARE</h2>
<table>
<tr>
    <td>Name</td>
    <td>Quantity</td>
    <td><em>Description</em></td>
</tr>
<tr>
    <td>Raspberry pi pico RP2040 microcontroller</td>
    <td>1</td>
    <td><em>control the motors and sensors</em></td>
</tr>
<tr>
    <td>12v DC Geared Motors</td>
    <td>4</td>
    <td><em>300 rpm</em></td>
</tr>
<tr>
    <td>Dual tb6612fng</td>
    <td>2</td>
    <td><em>H bridge for motor control</em></td>
</tr>
<tr>
    <td>Lipo Battery</td>
    <td>1</td>
    <td><em>Power supply 2200 mah</em></td>
</tr>
<tr>
    <td>Mecanum wheels</td>
    <td>4</td>
    <td><em>Omnidirectional wheels</em></td>
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
<ul>
    <li>Step01: Start</li>                                          
    <li>Step02: Print system info</li>
    <li>Step03: Initialise global variables and uart objects</li>
    <li>Step04: while True</li>
    <li>Step05: if uart.any()</li>
    <li>Step04: data <= uart.read()</li>
    <li>Step04: If (‘F’ in data): front()</li>    
    <li>Step05: elif (‘B’ in data): back()</li>
    <li>Step06: elif (‘L’ in data): left()</li>
    <li>Step07: elif (‘R’ in data): right()</li>
    <li>Step08: elif (‘I’ in data): rightDiagonalFront()</li>
    <li>Step09: elif (‘G’ in data): leftDiagonalFront()</li>
    <li>Step10: elif (‘H’ in data): leftDiagonalBack()</li>
    <li>Step11: elif (‘J’ in data): rightDiagonalBack()</li>
    <li>Step12: elif (‘W’ in data): leftShift()</li>
    <li>Step13: elif (‘U’ in data): rightShift()</li>
    <li>Step14: elif (‘1’ in data): speed <= 10</li>
    <li>Step15: elif (‘2’ in data): speed <= 20</li>
    <li>Step16: e1if (‘3’ in data): speed <= 30</li>
    <li>Step17: elif (‘4’ in data): speed <= 40</li>
    <li>Step18: elif (‘5’ in data): speed <= 50</li>
    <li>Step19: elif (‘6’ in data): speed <= 60</li>
    <li>Step20: elif (‘7’ in data): speed <= 70</li>
    <li>Step21: elif (‘8’ in data): speed <= 80</li>
    <li>Step22: elif (‘9’ in data): speed <= 90</li>
    <li>Step23: elif (‘10’ in data): speed <= 100</li>
    <li>Step24: else(): stop()</li>
</ul>
<h2>Flowchart<h2>
<img src="/pics/Flowchart.png" alt="Flowchart.png" style="height: 1000px; width:1000px;"/>
