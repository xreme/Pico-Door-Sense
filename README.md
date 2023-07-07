  # Pico-Door-Sense

<!-- LOGO GOES HERE -->
<br />

<a name="readme-top"></a>
<div align="center">
  <!--
  <a href="https://github.com/xreme/Pico-Door-Sense">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

 <h3 align="center">Pico Door Sense</h3>

 <p align = "left"> Pico Door Sense leverages the power of a Raspberry Pi Pico and the LM393 3144 Hall effect sensor Module to host a web server on the local Wi-Fi network; it offers real-time updates about the status of the specific door.
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
        <li><a href="#installation">Software Installation</a></li>
        <li><a href="#wiring">Wiring</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
   </ol>
 </details>

<!--ABOUT THE PROJECT -->
## About The Project
It happens all too often, someone forgets to close a door,garage, or gate and it is not only until sometime after that the mistake is discovered; this was the problem facing my household. There are many of going about solving this solution such as buying commercial products, but I decided take shot at devloping a custom solution.

The principle of this project was to use a Hall effect--magnetic field-- sensor & magnet to detect whether a given door is open or closed. The Hall effect sensor would remain staionary, while a magnet would be attatched to a door. When the door is closed the magnet would be within range of the Hall effect sesnor indicating to the Raspberry Pi that the door is closed. Once the door is opened the magnet would move away from the sensor, indcating that the door has been opened.

Users connect to the server hosted by the Raspberry Pi Pico using it's local IP adress where they are served a webpage that displays the real time information about the door. Clients may also simply request the raw JSON data, for ease of further development.

<!-- Getting Started -->
## Getting Started
Some code may need to be modified to fit a specific use cases.

## Parts List
Very simple parts are used for this project, they can be found on many large electronics componenent stores. Ensure to use the Pico W, as the wireless functioanlty is a vital part of the project.
<ol>
  <li>Main Components</li>
  <ul>
      <li><a href = "https://www.raspberrypi.com/products/raspberry-pi-pico/?variant=raspberry-pi-pico-w" target="_blank">Raspberry Pi Pico W (wireless is important)<a></li>
      <li>Hall Effect Sensor (LM393 3144)</li>
      <li>Strong Magnets</li>
  </ul>
  <li>Other Items</li>
  <ul>
    <li>Solder</li>
    <li>Wire (3 different colors reccomended)</li>
    <li>MicroUsb Cable</li>
  </ul>
  <li>Tools</li>
  <ul>
      <li>Soldering Iron</li>
      <li>Wire Cutter & Stripper</li>
  </ul>
</ol>

## Software Installation

1. Install the Micropython firmware onto the Raspberry Pi Pico. (<a href="https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/3">Tutuorial</a>)
2. Through Thonny, install the picozero library. (<a href="https://picozero.readthedocs.io/en/latest/gettingstarted.html">documentation</a>)
3.  Download the repository and copy all the files from the "pico-door-sense" folder onto the root directory of the Raspberry Pi Pico.
4.  Edit the "config.txt" file and replace "SSID" with your network's name, and "PASSWORD" with the network passowrd. Ensure that the network is on the first line and the password is on the second without any spaces. 
5.  Run "main.py" on the pico through thonny. The green LED should flash as it attempts to connect to your local network. If it is successful the green LED will turn off.
6.  If the conncection was successful the Pico will print out its IP address, take note of that as it is how you will connect to the it.
7. Enter in the IP address of the Raspberry Pi Pico on a browser, if all is successful it will display a green webpage.



<p align="right">(<a href="#readme-top">back to top</a>)</p>
