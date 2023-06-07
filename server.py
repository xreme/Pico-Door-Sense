import json
from picozero import pico_temp_sensor, pico_led
from machine import Pin

#Led Connected to Pin 15 // HE Sensor Connected to Pin 28
#led = Pin(15,Pin.OUT)
he_sensor = Pin(28,Pin.IN)

class RequestHandler:
    def __init__(self,connection):
        self.connection = connection
        self.state = 'OFF'
        self.temperature = 0
        pico_led.off()
    
    def serve(self):
        #accept requests from users
        client = self.connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        
        #print the request
        print(request)
        
        #parse the request
        try:
            request = request.split()[1]
        except IndexError:
            pass

        self.handle_request(request,client)
        client.close()
    
    def handle_request(self,request,client):
        #handle the request
        #FUTURE: add a 404 page
        #FUTURE: change into switch case
        if request == '/lighton?':
            #change the state of the led
            self.turn_led_on()
            self.send_webpage(client)
        
        elif request == '/lightoff?':
            #change the state of the led
            self.turn_led_off()
            self.send_webpage(client)
        
        elif request == '/data':
            #send the data to the client
            self.send_data(client)
        
        elif request == '/':
            #send the main page to the client
            self.send_webpage(client)
        
        elif request == '/main.js':
            #send the main.js file to the client
            self.send_main_js(client)
        
        else:
            #send the main page to the client
            self.send_webpage(client)
    
    
    def turn_led_on(self):
        pico_led.on()
        self.state = 'ON'
    
    def turn_led_off(self):
        pico_led.off()
        self.state = 'OFF'
    
    def send_data(self,client):
        #update the temperature variable
        self.update_data()
        
        #create a dictionary to store the data
        data = {
            'he_sensor_value': he_sensor.value(),
            'state': self.state,
            'temperature': self.temperature
        }
        
        #send the the HTTP header
        client.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        
        #convert the dictionary into a json string
        data = json.dumps(data)
        
        #send the data to the client
        client.send(data)
    
    def send_main_js(self,client):
        
        javascript = self.read_main_js()

        #send the the HTTP header
        client.send("HTTP/1.1 200 OK\r\nContent-Type: text/javascript\r\n\r\n")

        #send the main page
        client.send(javascript)

    def send_webpage(self,client):
        #update the temperature variable
        self.update_data()
        webpage = self.webpage()

        client.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        client.send(webpage)

    def update_data(self):
        #update the temperature variable
        self.temperature = pico_temp_sensor.temp
        
        #update the state variable
        if pico_led.value == 1:
            self.state = 'ON'
        else:
            self.state = 'OFF'
        
        #update the he sensor value
        self.he_sensor_value = he_sensor.value()

    def webpage(self):
        #open & read HTML file
        index_html_file = open('index.html', 'r')
        index_html = index_html_file.read()

        #replace the placeholders with the values
        html = index_html.format(temperature=self.temperature, state=self.state)
        
        #close the file
        index_html_file.close()
        return str(html)
    
    def read_main_js(self):
        #open & read javascript file
        main_js_file = open('main.js', 'r')
        main_js = main_js_file.read()
        
        #close the file
        main_js_file.close()
        return str(main_js)