# Simon Game written in the style of Day 3 from the advent calendar

# Imports
from machine import Pin
import time
import random

# Set up our button names and GPIO pin numbers
# Also set pins as inputs and use pull downs
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Set up our LED names and GPIO pin numbers
red = Pin(20, Pin.OUT)
amber = Pin(21, Pin.OUT)
green = Pin(19, Pin.OUT)

#Timeout for reading the buttons
timeout=30

while True: # Loop forever
    sequence = []
    red.value(0) # red LED off
    amber.value(0) # amber LED off
    green.value(0) # green LED off
    print("\nPress any button to start a new game")
    while True:
        if button1.value() == 1 or button2.value() == 1 or button3.value() == 1:
            break;
    endgame=False
    
    while endgame==False:
        sequence.append(random.randint(1, 3)) # Add to sequence each iteration
        duration = 1 - len(sequence) * 0.05 # Randomise sleep between each LED being lit
        if duration < 0.1:
            duration = 0.1
        for led in sequence: # Display LED sequence

            if led == 1:
                print('Red')
                red.value(1) # red LED on
            elif led == 2:
                print('Amber')
                amber.value(1) # amber LED on             
            elif led == 3:
                print('Green')
                green.value(1) # green LED on
            time.sleep(duration)
            red.value(0) # red LED off
            amber.value(0) # amber LED off
            green.value(0) # green LED off
        print("\nYour Turn\n")

        for expectedbutton in sequence: # Read buttons and check if they are in the correct sequence
            buttonval = 0
            start_time = time.time()
            while time.time() - start_time < timeout:
                if button1.value() == 1:
                    red.value(1) # red LED on
                    buttonval = 1
                    time.sleep(.3)
                    red.value(0) # red LED off
                    break
                elif button2.value() == 1:
                    amber.value(1) # amber LED on
                    buttonval = 2
                    time.sleep(.3)
                    amber.value(0) # amber LED off
                    break
                elif button3.value() == 1:
                    green.value(1) # green LED on
                    buttonval = 3
                    time.sleep(.3)
                    green.value(0) # green LED of
                    break

            if buttonval != expectedbutton: # Check if button matches
                print("Wrong Button")
                endgame = True
                if expectedbutton == 1:
                    print("Expected Red")
                elif expectedbutton == 2:
                    print("Expected Amber")
                else:
                    print("Expected Green")

                if buttonval == 1:
                    print("You pressed Red")
                elif buttonval == 2:
                    print("You pressed Amber")
                else:
                    print("You pressed Green")
                break
            else:
                print("Correct")        
        time.sleep(1)
