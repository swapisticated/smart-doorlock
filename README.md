## Smart Door Lock with RFID and Firebase Integration

This project implements a smart door lock system using an RFID reader, Raspberry Pi Pico W, and Firebase Realtime Database. Authorized users with RFID tags can unlock the door, and access logs are stored in the cloud database for real-time monitoring.

### Features

* RFID tag authentication for secure access.
* Raspberry Pi Pico W for efficient processing and wireless connectivity.
* Firebase Realtime Database for storing access logs with timestamps.
* Easy to understand code written in MicroPython.

### Hardware Required

* Raspberry Pi Pico W
* RFID reader module (e.g., MFRC522)
* RFID tags (compatible with your reader)
* Relay module to control the door lock
* Breadboard and jumper wires
* Power supply for Raspberry Pi Pico

### Software Required

* Thonny IDE ([https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/2](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/2))
* MicroPython ([https://www.raspberrypi.com/documentation/microcontrollers/](https://www.raspberrypi.com/documentation/microcontrollers/)) libraries for RFID reader and Firebase ([https://pypi.org/project/python-rfid/](https://pypi.org/project/python-rfid/))
* Firebase account ([https://console.firebase.google.com/](https://console.firebase.google.com/))

### Setup Instructions

1. **Install MicroPython on Raspberry Pi Pico:** Follow the official guide ([https://www.raspberrypi.com/documentation/microcontrollers/](https://www.raspberrypi.com/documentation/microcontrollers/)) to set up MicroPython on your Pico W.
2. **Connect Hardware:** Wire the RFID reader, relay module, and other components to the Pico following the specific pinout for your modules.
3. **Install Libraries:** Use Thonny IDE to install the required MicroPython libraries for RFID and Firebase.
4. **Configure Firebase:** Create a Firebase project and set up a Realtime Database. Obtain the necessary configuration details (project ID, database URL, and API key) for your code.
5. **Write the Code:** Modify the `main.py` script to match your hardware connections and Firebase configuration. 

**Note:** Due to security concerns, we recommend not including the Firebase configuration details directly in the code. You can implement environment variables or other secure methods to store these details.

### Circuit Diagram
<img src="https://github.com/swapisticated/smart-doorlock/blob/main/assets/Pasted%20image%20(3).png" width=600/>

### Usage

1. **Upload the Code:** Upload the `main.py` script to your Raspberry Pi Pico.
2. **Register Tags:** Use the code functionality (or a separate script) to register authorized RFID tags in the system.
3. **Unlocking the Door:** Present a registered RFID tag to the reader. The code will verify the tag and trigger the relay to unlock the door. Additionally, it will log the access event with a timestamp in the Firebase database.

### Additional Notes

* This is a basic implementation and can be extended with features like user management, access logs with user details, and notifications.
* Remember to follow safe coding practices and secure your Firebase configuration details.
* Consider incorporating visual or audio feedback mechanisms for user interaction.

### Contributing

We welcome contributions to improve this project. Feel free to submit pull requests with bug fixes, enhancements, or additional functionalities.
