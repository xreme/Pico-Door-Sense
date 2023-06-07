import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine
import json
from machine import Pin

#Led Connected to Pin 15 // HE Sensor Connected to Pin 28
#led = Pin(15,Pin.OUT)
he_sensor = Pin(28,Pin.IN)

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
        print('Waiting for Connection ' + str(count))
        count +=1
        sleep(1)
    
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

#Generate the requested webpage
def webpage(temperature, state ):
    #open & read HTML file
    index_html_file = open('index.html', 'r')
    index_html = index_html_file.read()

    #replace the placeholders with the values
    html = index_html.format(temperature=temperature, state=state)
    
    #close the file
    index_html_file.close()
    return str(html)

#Read the main.js file and return it as a string
def read_main_js():
    #open & read javascript file
    main_js_file = open('main.js', 'r')
    main_js = main_js_file.read()
    
    #close the file
    main_js_file.close()
    return str(main_js)

#Serve the client requests
#FUUTRE: Turn into a class
def serve(connection):
   
   #initalize the states of the variables
    state = "OFF"
    pico_led.off()
    temperature = 0

    #start serving the client requests
    while True:
        
        #accept requests from users
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        
        #print the request
        print(request)
        
        #parse the request
        try:
            request = request.split()[1]
        except IndexError:
            pass
        
        #handle the request
        #FUTURE: add a 404 page
        #FUTURE: change into switch case
        

        if request == '/lighton?':
            #change the state of the led
            pico_led.on()
            #update the state variable
            state = 'ON'
        
        elif request == '/lightoff?':
            #change the state of the led
            pico_led.off()
            #update the state variable
            state = 'OFF'
        
        elif request == '/data':
            #update the temperature variable
            temperature = pico_temp_sensor.temp
            
            #create a dictionary to store the data
            data = {
                'he_sensor_value': he_sensor.value(),
                'state': state,
                'temperature': temperature
            }
            
            #send the the HTTP header
            client.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
            
            #send the data
            client.send(json.dumps(data))
            
            #send the data
            client.close()

            continue #make sure to only send the json data
        
        elif request == '/main.js':
            #read the javascript file
            javascript =  read_main_js()

            #send the the HTTP header
            client.send("HTTP/1.1 200 OK\r\nContent-Type: text/javascript\r\n\r\n")
            
            #send the javascript
            client.send(javascript)
            
            #send the data
            client.close()
            continue
            
        #generate webpage
        html = webpage(temperature, state)
        
        #pretened that the http header is sent
        client.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")

        #send webpage
        client.send(html)

        #close the connection
        client.close()

try:
    #connect to the network
    ip = connect()

    #open a socket
    connection = open_socket(ip)

    #start serving the client requests
    serve(connection)
except KeyboardInterrupt:
    machine.reset()
