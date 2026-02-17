📡 ESP32 Web‑Controlled Morse Code Server

A MicroPython project that turns an ESP32 into a fully functional webserver for controlling GPIO pins and blinking Morse code messages sent from a browser.

This project demonstrates how to combine networking, hardware control, and text parsing on a microcontroller — all through a clean HTML interface served directly from the ESP32.
🚀 Features
🔘 LED Control

The webpage provides two buttons:

    ON — sets the LED pin HIGH

    OFF — sets the LED pin LOW

The current GPIO state is displayed dynamically using a placeholder in web.html.
🔤 Morse Code Input

The webpage includes a text field where the user can enter a message.
When submitted:

    The ESP32 receives the HTTP request

    Extracts the name= parameter

    Cleans and uppercases the text

    Sends it to the blink() function in morse.py

    The LED blinks the message in Morse code

🌐 External HTML Page

The webpage is stored in web.html and loaded at runtime.
A placeholder {{STATE}} is replaced with "ON" or "OFF" before sending the page to the browser.

This keeps the Python code clean and makes the UI easy to edit.
🧵 WebREPL Support

The boot.py file enables WebREPL at startup:
python

import esp
esp.osdebug(None)

import webrepl
webrepl.start()

This allows:

    Wireless file uploads

    Remote REPL access

    Debugging without USB

📁 Project Structure
Code

/
├── boot.py        # Enables WebREPL and disables debug output
├── main.py        # Webserver + GPIO control + Morse input
├── morse.py       # Morse dictionary + blink() function
├── web.html       # External HTML page served to clients
└── README.md      # This file

🧠 How It Works
1. ESP32 starts a socket server

main.py opens port 80 and listens for incoming HTTP connections.
2. Browser sends a request

Examples:
Code

GET /?led=on HTTP/1.1
GET /?led=off HTTP/1.1
GET /?name=HELLO HTTP/1.1

3. The server parses the request

    /led=on → LED turns on

    /led=off → LED turns off

    name=... → text extracted and sent to Morse blinker

4. The webpage is loaded from web.html

The placeholder {{STATE}} is replaced with the current LED state.
5. The page is sent back to the browser

The connection closes and the loop waits for the next request.
🛠 Requirements

    ESP32 board

    MicroPython firmware

    Thonny, WebREPL, or another uploader

    LED + resistor (or onboard LED)

📦 Installation

    Flash MicroPython to your ESP32

    Upload these files to the device:

        boot.py

        main.py

        morse.py

        web.html

    Reset the ESP32

    Connect to its Wi‑Fi network or your home network

    Open the ESP32’s IP address in a browser

🧩 Customization Ideas

    Add more GPIO controls

    Display the last Morse message sent

    Add non‑blocking blinking so the server stays responsive

    Add CSS or JavaScript for a richer UI

    Serve multiple pages

    Add Wi‑Fi credentials to run on your home network
