from machine import Pin
from time import sleep


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


#----A LOOP OVER THE MAIN FUNCTION CALL----

while True: 
  blink_morse(led, "I LOVE YOU") # type your message here :)
