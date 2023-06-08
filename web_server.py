import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine
import json
from machine import Pin
import server


#Connect to the Wi-Fi
def connect():
    #open the file containing the ssid and password
    config_info_file = open('config.txt', 'r')

    #read the ssid and password
    config_info = config_info_file.readlines()
    ssid = config_info[0].strip()
    password = config_info[1].strip()

    #close the file
    config_info_file.close()
    
    #create an instance of the WLAN class
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    #continue to send requests to connect to the network
    #until the connection is successful
    #FUTUTRE: add a timeout
    count = 0
    while not wlan.isconnected():
        turn_led_off()
        print('Waiting for Connection ' + str(count))
        count +=1
        turn_led_on()
        sleep(1)
    
    turn_led_off()
    #get the pico's local IP address
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

#Opening a socket for web traffic
def open_socket(ip):
    address = (ip, 80) #create a tuple
    connection = socket.socket() #create a socket and storing it in connection
    connection.bind(address)  #linking the created socket with the address info
    connection.listen(1)  #start listening for connections (1 at a time)
    print(connection)
    return connection

#Serve the client requests
def serve(connection):
    turn_led_on()
    # make a new server RequestHandler instance
    server_instance = server.RequestHandler(connection)
    turn_led_off()

    #start serving the client requests
    while True:
        server_instance.serve()

def turn_led_on():
    pico_led.on()
    
def turn_led_off():
    pico_led.off()

try:
    turn_led_on()

    #connect to the network
    ip = connect()

    turn_led_on()
    #open a socket
    connection = open_socket(ip)
    turn_led_off()

    #start serving the client requests
    serve(connection)
except KeyboardInterrupt:
    machine.reset()