# ESP32 MORSE CODE WEB SERVER (MICROPYTHON)
 
============================================================

This project turns an ESP32 into a simple web server that lets
you control an LED and send Morse code messages directly from
a web browser. The ESP32 serves an external HTML page, handles
GET requests, and blinks Morse code using a Python module.

------------------------------------------------------------
 ## FEATURES
------------------------------------------------------------

 - LED ON/OFF control from a web browser
 - Displays current LED GPIO state on the webpage
 - Text input field for sending Morse code messages
 - External HTML file (web.html) served by the ESP32
 - Morse code handled by morse.py (blink function)
 - WebREPL enabled at boot for wireless file access
 - Debug output disabled for cleaner logs

------------------------------------------------------------
 ## FILES
------------------------------------------------------------

 boot.py      - Enables uPyCraft IDE and disables debug output
 
 main.py      - Web server, GPIO control, Morse input logic
 
 morse.py     - Morse code dictionary + blink() function
 
 web.html     - HTML page served to the browser
 
 README.md   - This file
 

------------------------------------------------------------
 ## HOW IT WORKS
------------------------------------------------------------

1. ESP32 boots and runs boot.py:
      - Debug output disabled
      - WebREPL started

2. main.py starts a socket server on port 80.

3. A browser connects to the ESP32 and requests the webpage.

4. The ESP32 loads web.html and replaces {{STATE}} with the
   current LED state (ON/OFF).

5. The browser can send commands:
      /?led=on     -> LED turns ON
      /?led=off    -> LED turns OFF
      /?name=TEXT  -> TEXT is blinked in Morse code

6. The ESP32 parses the request, performs the action, and
   returns the updated webpage.

------------------------------------------------------------
 ## REQUIREMENTS
------------------------------------------------------------

 - ESP32 board
 - MicroPython firmware
 - Thonny, WebREPL, uPyCraft or similar tool
 - LED + resistor (or onboard LED)

------------------------------------------------------------
 ## INSTALLATION
------------------------------------------------------------

1. Flash MicroPython to the ESP32.
2. Upload the following files:
      boot.py
      uPyMain.py (rename it to main if needed)
3. Reset the ESP32 (EN button)
4. Connect to the ESP32 Wi-Fi or your home network.
5. Open the ESP32 IP address in a browser.

------------------------------------------------------------
## POSSIBLE BUGS / TROUBLESHOOTING
------------------------------------------------------------

- Port 80 blocked → unblock in Windows Firewall
- Browser hangs → main.py not running or missing socket import
- “Unable to connect” → ESP32 not on the same Wi‑Fi network
- Serial port locked → close COM port properly or reset ESP32
- Missing files → ensure web.html and morse.py are uploaded
- Wi‑Fi credentials wrong → ESP32 never reaches main.py


------------------------------------------------------------
## RESULT - FULL-ON MORSE WEB SERVER
------------------------------------------------------------

------------------------------------------------------------
 END OF FILE
============================================================
