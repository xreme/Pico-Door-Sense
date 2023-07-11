  # Pico-Door-Sense

<!-- LOGO GOES HERE
<br />
 -->
<a name="readme-top"></a>
<div align="center">
  <!--
  <a href="https://github.com/xreme/Pico-Door-Sense">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

 <!--<h3 align="center">Pico Door Sense</h3>-->

 <p align = "left">  Pico Door Sense leverages the power of a Raspberry Pi Pico and the LM393 3144 Hall effect sensor module to host a web server on the local Wi-Fi network; it offers real-time updates about the status of the specific door.
 </p>
</div>  

 <details>
   <summary>Table of Contents</summary>
   <ol>
     <li>
       <a href="#about-the-project">About The Project</a>
     </li>
     <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#parts-list">Parts List</a></li>
        <li><a href="#software-installation">Software Installation</a></li>
        <li><a href="#wiring">Wiring</a></li>
        <li><a href = "#testing">Testing</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href = "#further-development">Further Development</a></li>
   </ol>
 </details>

<!--ABOUT THE PROJECT -->
## About The Project
It happens all too often, someone forgets to close a door, garage, or gate, and it is not only until sometime after that the mistake is discovered; this was the problem facing my household. There are many ways to solve this solution, such as buying commercial products, but I decided to t develop a custom solution.

The principle of this project was to use a Hall effect--magnetic field-- sensor & magnet to detect whether a given door is open or closed. The Hall effect sensor would remain stationary, while a magnet would be attached to a door. When the door is closed, the magnet would be within range of the Hall effect sensor, indicating to the Raspberry Pi that the door is closed. Once the door is opened, the magnet moves away from the sensor, indicating that the door has been opened.

Users connect to the server hosted by the Raspberry Pi Pico using its local IP address, where they are served a webpage displaying real-time information about the door. Clients may also request the raw JSON data for ease of further development.

<!-- Getting Started -->
## Getting Started
Some code may need to be modified to fit specific use cases.

## Parts List
The required parts can be easily sourced from component retailers such as amazon, or aliexpress. Make sure to use the Pico W (the wireless variant), as the wireless functionality is vital to the project.
<ol>
  <li>Main Components</li>
  <ul>
      <li><a href = "https://www.raspberrypi.com/products/raspberry-pi-pico/?variant=raspberry-pi-pico-w" target="_blank">Raspberry Pi Pico W (wireless is important)<a></li>
      <li>Hall Effect Sensor (LM393 3144)</li>
      <li>Strong Magnets</li>
  </ul>
  <li>Other Items</li>
  <ul>
    <li>Solder(optional)</li>
    <li>Wire (3 different colors reccomended)</li>
    <li>MicroUsb Cable</li>
  </ul>
  <li>Tools</li>
  <ul>
      <li>Soldering Iron(optional)</li>
      <li>Wire Cutter & Stripper(optional)</li>
  </ul>
</ol>

## Software Installation

1. **Setup the Pico** -  Install the Micropython firmware onto the Raspberry Pi Pico. (<a href="https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/3">Tutuorial</a>)

2. **Install the required library** - Through Thonny, install the picozero library. (<a href="https://picozero.readthedocs.io/en/latest/gettingstarted.html">documentation</a>)

3. **Load the software** -  Download the repository and copy all the files from the "pico-door-sense" folder onto the root directory of the Raspberry Pi Pico.

4. **Fill in network information** - Edit the "config.txt" file and replace "SSID" with your network's name and "PASSWORD" with the network password. Ensure that the network name is on the first line and the password is on the second without any spaces. 

5. **Test the connection** - Run "main.py" on the pico through Thonny. The green LED should flash as it attempts to connect to your local network. If it is successful, the green LED will turn off. If the led continues to blink after one minute, ensure that the network information is correct and try again.

6. **Save the information** - If the connection is successful, the Pico will print out its IP address; take note of the address, as it is how devices will connect to it.

7. **Connect to the Pico** - Enter the IP address of the Raspberry Pi Pico W on a browser; if all is successful, the browser will display a green webpage.


## Wiring

!! Ensure the Raspberry Pi pico is unplugged from any power before wiring.

|Raspberry Pi PICO W| Hall effect sensor|
|:-----------------:|:-----------------:|
|3.3 V              | VCC               |
|GND                | GND               |
|GPIO 28            | D0                |

Depending on the chosen Hall effect sensor module, an led may glow when the module is powered. On the LM393 3144 Hall effect sensor, one green LED will turn on once it receives power from the Pico, and a second will turn on when it senses a magnetic field.

## Testing

The system can be tested once the wiring is complete and the software has been installed. Connect the pico to a power source, and it should automatically attempt to connect the network specified in the config file. 

Upon successful connection, the LED of the Raspberry Pi Pico W should turn off. Use a device connected to the same network and enter the IP address of the Raspberry Pi Pico W. 

Once connected, users should see the current status of the Hall effect sensor and a timestamp for that status. Users can move a magnet back and forth from the Hall effect; users should see the webpage being dynamically updated, and if so, the system is operational.

## Usage

This system can be used anywhere that household members see fit for monitoring. A magnet can be placed on the door of choice, and the Hall effect sensor can be placed in a position of choice where it detects the magnet while the door is closed with the pico nearby. The Raspberry Pi Pico W can then be powered, giving all users on the network access to the status of the door by connecting to the Pico W using its IP address.

## Further Development

By default clients will be served an Webpage containing the information. 

The raw data in JSON form can be requested with the following query:
```
PICO.W.IP.ADDSRESS/data
```
This information can be used to implement the status of this door in other developements.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
