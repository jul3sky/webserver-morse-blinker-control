"""
The original code taken from 
https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/
and modified by jul3sky
"""


#----WEB PAGE----
def web_page():
  if led.value() == 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"
  
  with open("web.html") as f: # external html for web server
    html = f.read()

  html = html.replace("{{STATE}}", gpio_state)
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
  request = str(request)
  print(f"Content = {request}")
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')
  if led_on == 6:
    print('LED ON')
    led.value(1)
  if led_off == 6:
    print('LED OFF')
    led.value(0)
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()

#----MORSE I/O----
import morse
from morse import blink

conn, addr = s.accept()
print(f"Got a connection from {addr}")
request = conn.recv(1024)

if "name=" in request:
  start = request.find("name=") + len("name=")
  end = request.find(" ", start)
  morse_text = request[start:end]
  
  morse_text = morse_text.replace("%20", " ")
  morse_text = morse_text.upper()

blink(morse_text)


