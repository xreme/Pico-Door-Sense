import local_web_socket
from picozero import pico_led
import server
import machine



try:
    #make a new local socket instance
    local_socket = local_web_socket.LocalWebSocket()

    pico_led.on()

    # make a new server RequestHandler instance
    server_instance = server.RequestHandler(local_socket.connection)

    pico_led.off()

    #start serving the client requests
    while True:
        server_instance.serve()

except:
    machine.reset()