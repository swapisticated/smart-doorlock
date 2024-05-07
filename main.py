from mfrc522 import MFRC522 
import utime
from machine import Pin
import urequests
import network
import socket

from wlan import do_connect

# Function to establish Wi-Fi connection
do_connect()

print("\nPlace Card")

lock = Pin(28, Pin.OUT)
buzzer = Pin(27, Pin.OUT)
RLed = Pin(18, Pin.OUT)
GLed = Pin(19, Pin.OUT)

lock.value(0)
buzzer.value(0)
RLed.value(0)
GLed.value(0)

def webpage(message):
    html = f"""
                <!DOCTYPE html>
                <html>
                    <head></head>
                    <body>
                    <form action ="/lockon?">
                        <input type = "submit" value="lockon" style="height:40px; width:120px" />
                    </form>
                    <form action ="/lockoff?">
                        <input type = "submit" value="lockoff" style="height:40px; width:120px" />
                    </form>
                        <p>Response from server is "Hello" and received from client is {message}</p>
                        
                    </body>
                </html>

                """
    return html

def uidToString(uid):
    mystring = ""
    for i in uid:
        mystring = "%02X" % i + mystring
    return mystring

rc522 = MFRC522(spi_id=0, sck=6, miso=4, mosi=7, cs=5, rst=22)

firebase_url = 'https://pico-w-smart-lock-default-rtdb.firebaseio.com/rfid_logs.json'  # Update with your Firebase Realtime Database URL

while True:
    (stat, tag_type) = rc522.request(rc522.REQALL)

    if stat == rc522.OK:
        (status, raw_uid) = rc522.SelectTagSN()
        if stat == rc522.OK:
            rfid_data = "{:02x}{:02x}{:02x}{:02x}".format(raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            current_time = utime.localtime()
            formatted_time = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(current_time[0], current_time[1], current_time[2], current_time[3], current_time[4], current_time[5])
            print("Card detected! UID: {}, Time: {}".format(rfid_data, formatted_time))
#             print("Card detected! UID: {}".format(rfid_data))
#             Send RFID data to Firebase
#             response = urequests.post(firebase_url, json={"rfid_data": rfid_data})
#             print(response.text)  # Print response for debugging
#             response.close()

            # Your other RFID processing code here
            if rfid_data == "13542c11":
                
                #lock.value(0)
                lock.on()
                GLed.value(1)
                utime.sleep(5)
                #lock.value(1)
                lock.off()
                GLed.value(0)
                
                
            elif rfid_data == "0848bd6a":
                
                #lock.value(0)
                lock.on()
                GLed.value(1)
                utime.sleep(5)
                #lock.value(1)
                lock.off()                
                GLed.value(0)
                
            elif rfid_data == "082db996":
                
                #lock.value(0)
                lock.on()
                GLed.value(1)
                utime.sleep(5)
                #lock.value(1)
                lock.off()                
                GLed.value(0)
                
                
            elif rfid_data == "01020304":
                
                #lock.value(0)
                lock.on()
                GLed.value(1)
                utime.sleep(5)
                #lock.value(1)
                lock.off()                
                GLed.value(0)
                

            else:
                
                buzzer.value(1)
                RLed.value(1)
                utime.sleep(1)
                buzzer.value(0)
                RLed.value(0)
                lock.value(0) 
            
            data_to_send = {"rfid_data": rfid_data, "time": formatted_time}
            response = urequests.post(firebase_url, json=data_to_send)
            print(response.text)  # Print response for debugging
            response.close()
            
            