import json
from picozero import pico_temp_sensor
from machine import Pin

#Led Connected to Pin 15 // HE Sensor Connected to Pin 28
he_sensor = Pin(28,Pin.IN)

class RequestHandler:
    #initialize the class
    def __init__(self,connection):
        self.connection = connection
        self.temperature = 0
        self.he_sensor_value = "N/R"
    
    #serve the client requests
    def serve(self):
        #accept & store requests from users
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

        #handle the request
        self.handle_request(request,client)
        client.close()
    
    #send correct information baed on request
    def handle_request(self,request,client):
        #FUTURE: add a 404 page

        if request == '/data':
            #send the data to the client
            self.send_data(client)
        
        elif request == '/':
            #send the main page to the client
            self.send_webpage(client)
        
        elif request == '/main.js':
            #send the main.js file to the client
            self.send_main_js(client)
        
        elif request == '/style.css':
            #send the style.css file to the client
            self.send_style_css(client)

        elif request == '/images/door-open.png':
            #send the open.png file to the client
            self.send_file(client,'images/door-open.png')
        
        elif request == '/images/door-closed.png':
            #send the closed.png file to the client
            self.send_file(client,'images/door-closed.png')
        
        else:
            #send the main page to the client
            self.send_webpage(client)
    
    #send a data file containing the temparature & the hall effect sensor to the client
    def send_data(self,client):

        #update the temperature variable
        self.update_data()
        
        #create a dictionary to store the data
        data = {
            'he_sensor_value': self.he_sensor_value,
            'temperature': self.temperature
        }
       
        #send the the HTTP header
        client.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        
        #convert the dictionary into a json string
        data = json.dumps(data)
        
        #send the data to the client
        client.send(data)
    
    #send javascript file to the client
    def send_main_js(self,client):

        #send the the HTTP header
        client.send("HTTP/1.1 200 OK\r\nContent-Type: text/javascript\r\n\r\n")

        #send the main page
        client.send(self.read_main_js())

    #send the main page to the client
    def send_webpage(self,client):

        #update the temperature variable
        self.update_data()
        webpage = self.webpage()

        #send the the HTTP header
        client.send("HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n")

        #send the main page
        client.send(webpage)

    #update the temperature and hall-effect variables
    def update_data(self):

        #update the temperature variable
        self.temperature = "{:.1f}".format(pico_temp_sensor.temp,1)

        #update the he sensor value
        if he_sensor.value() == 1:
            self.he_sensor_value = "OPEN"
        else:
            self.he_sensor_value = "CLOSED"

    #generate the webpage
    def webpage(self):
        
        #open & read HTML file
        index_html_file = open('index.html', 'r')
        index_html = index_html_file.read()

        #replace the placeholders with the corresponding values
        html = index_html.format(temperature=self.temperature, he_sensor_value=self.he_sensor_value)
        
        #close & return the file
        index_html_file.close()
        return str(html)
    
    #open & read javascript file
    def read_main_js(self):
        
        main_js_file = open('main.js', 'r')
        main_js = main_js_file.read()
        main_js_file.close()

        return str(main_js)
    
    #send the style.css file to the client
    def send_style_css(self,client):
        #open & read CSS file
        style_css_file = open('style.css', 'r')
        style_css = style_css_file.read()
        
        #send the the HTTP header
        client.send("HTTP/1.1 200 OK\r\nContent-Type: text/css\r\n\r\n")
        
        #send the style.css file
        client.send(style_css)
        
        #close the file
        style_css_file.close()

    #send any file to the client
    def send_file(self,client, file_name):
        
        #open & read the file
        opened_file = open(file_name, 'rb')
        file = opened_file.read()
        
        #send the the HTTP header
        client.send("HTTP/1.1 200 OK\r\nContent-Type: image/png\r\n\r\n")
        
        #send the file
        client.send(file)
        
        #close the file
        opened_file.close()