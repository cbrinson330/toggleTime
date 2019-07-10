import time
import RPi.GPIO as GPIO
import toggleTime

#initialise a previous input variable to 0 (assume button not pressed last)
prev_input = 0

#Setup button
buttonPin = 10

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

tt = toggleTimers()

while True:
  #take a reading
  # GPIO Pin 10 = index 0
  #TODO create dictionary for pins/index
  input = GPIO.input(10)

  if ((not prev_input) and input):
    tt.setTimer(0, True)
    print("On")
  elif (prev_input and (not input)):
    tt.setTimer(0, False)
    print("Off")

  #update previous input
  prev_input = input
  #slight pause to debounce
  time.sleep(0.5)