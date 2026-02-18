"""
This whole file you use when you want to run your webserver through uPyCraft IDE.
It really likes when all the data is presentented in one file.
"""



from machine import Pin
from time import sleep
import socket


#----MORSE CODE DICTIONARY----

MORSE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',
    'T': '-',     'U': '..-',   'V': '...-',  'W': '.--',
    'X': '-..-',  'Y': '-.--',  'Z': '--..',

    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----'
}
# special characters like . , ? / are not included


#----MAIN FUNCTION DEFINITION----

def blink_morse(led, message, dot=0.2): # we use physical LED, the Message string and DOT as the unit to contol speed of Morse Code
    dash = dot * 3
    gap_letter = dot * 3
    gap_word = dot * 7

    message = message.upper() # converts whatever you type automatically into uppercase

    for char in message:
        if char == ' ':
            sleep(gap_word)
            continue

        code = MORSE.get(char) # this line helps to make sure that the Morse Code pattern exists for current character
        if not code:
            continue  # skip unknown characters

        for symbol in code:
            if symbol == '.':
                led.value(1)  # LED turned ON (1)
                sleep(dot) # this keeps LED on for the duration of a DOT
            elif symbol == '-':
                led.value(1)
                sleep(dash)

            led.value(0)  # LED turned OFF (0)
            sleep(dot)  # gap between words

        sleep(gap_letter)  # gap between letters
      

#----PHYSICAL PIN DEFINED----

led = Pin(2, Pin.OUT)


#----WEB PAGE----
def web_page():
  if led.value() == 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"
  


  html = """
  <html>
  <head> 
    <title>ESP Web Server</title> <!--Name of the Web Server -->
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,"> 
    <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
    h1{color: #49003d; padding: 2vh;}p{font-size: 1.5rem;}
    .button{display: inline-block; background-color: #26d703; border: none; 
    border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
    .button2{background-color: #2d5723;}
    .button3{display: inline-block; background-color: #017258; border: none; border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 20px; margin: 2px; cursor: pointer;}
    </style> <!--Styling for buttons -->
  </head>
  
  <body> 
    <h1>ESP Web Server</h1> 
    <p><a class="button" href="/?led=on">ON</a></p>
    <p><a class="button button2" href="/?led=off">OFF</a></p>

    
    <form> <!--To submit your string -->
      <label for="name">Your Morse Code (max 16 char.):</label>
      <p>
        <input
          type="text"
          id="name"
          name="name"
          required
          minlength="3"
          maxlength="16"
          size="16" />
      </p>
      <p>
        <input type="submit" value="Send Request" class="button3"/>
      </p>
    </form>
  </body>
  
</html> """
  return html # returns a variable that contains html document to build the page

#----SOCKET----
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80)) # empty string '' is for ip address
s.listen(5) # 5 is maximum number of queued connections

#----LOOP CONNECTIONS FOR ON/OFF BUTTONS----
while True:
  conn, addr = s.accept()
  print(f"Got a connection from {addr}")
  request = conn.recv(1024)
  request = request.decode()
  print(f"Content = {request}")
  
  
  if '/?led=on' in request:
    print('LED ON')
    led.value(1)
  if '/?led=off' in request:
    print('LED OFF')
    led.value(0)
  response = web_page()
  #----MORSE I/O----
  if "name=" in request:
    start = request.find("name=") + len("name=")
    end = request.find(" ", start)
    morse_text = request[start:end]
    
    morse_text = morse_text.replace("%20", " ")
    morse_text = morse_text.upper()
    
    blink_morse(led, morse_text)
  
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
