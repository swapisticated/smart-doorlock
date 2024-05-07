import network
from wlan import do_connect
import socket
from machine import Pin

led = Pin(19, Pin.OUT)

lock = Pin(28, Pin.OUT)


def webpage(message):
    html = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>RFID Door Lock Control</title>
    </head>
    <body style="font-family: 'Arial', sans-serif; background-color: #f7efd2; text-align: center; padding: 50px;">
        <h1 style="color: #475c6c;">RFID Door Lock System</h1>
        <form action="/lockon?" style="margin: 10px;">
            <input type="submit" value="Unlock Door" style="background-color: #8a8583; border: none; color: white; padding: 20px 40px; font-size: 16px; cursor: pointer; transition-duration: 0.4s; border-radius: 50px; box-shadow: 4px 4px 8px #cd8b62;"/>
        </form>
        <form action="/lockoff?" style="margin: 10px;">
            <input type="submit" value="Lock Door" style="background-color: #8a8583; border: none; color: white; padding: 20px 40px; font-size: 16px; cursor: pointer; transition-duration: 0.4s; border-radius: 50px; box-shadow: 4px 4px 8px #cd8b62;"/>
        </form>
        <p style="color: #555;">Response from server is "Hello" and received from client is {message}</p>
    </body>
</html>

                """
    return html

def open_socket(ip):
    address = (ip,80)
    connection=socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def serve(connection):
    while True:
        client=connection.accept()[0]
        request = client.recv(1024)
        request=str(request)
        try:
            request=request.split()[1]
            print("request",request)
        except KeyboardInterrupt:
            pass
        message = request
        if message =='/lockon?':
            lock.value(1)
            led.value(1)
        if message =='/lockoff?':
            lock.value(0)
            led.value(0)
        
        html = webpage(message)
        client.send(html)
        client.close() 
        
    
try:
    ip=do_connect()
    print('ip address is:',ip)
    connection = open_socket(ip)
    serve(connection)
    
except KeyboardInterrupt:
    pass