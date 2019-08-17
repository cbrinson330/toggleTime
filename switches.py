import time
import RPi.GPIO as GPIO
from toggleTime import toggleTimers
from switch import switch

#initialise a previous input variable to 0 (assume button not pressed last)
prev_input = 0

#list for button objs
swtichObjList = [SimpleClass(count) for count in range(4)]

#Setup button
switchPins = [2, 3, 4, 14]

#init button pin objects
timerIndex = 0
for switchPin in switchPins:
  switchobj = switch(switchIndex, timerIndex)
  switchObjList.append(switchobj)
  timerIndex += 1

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
for pin in switchPins:
  GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pins to be input pins and set initial value to be pulled low (off)

tt = toggleTimers()

while True:
  for swtich in switchObjList:
    input = GPIO.input(switch.pinNumber)
    switchState = switch.checkInput(input)
    if switchState is not None:
      tt.setTimer(switch.timerIndex, switchState)


  #take a reading
  # GPIO Pin 10 = index 0
  #input = GPIO.input(10)

  # if ((not prev_input) and input):
  #  tt.setTimer(0, True)
  #  print("On")
  # elif (prev_input and (not input)):
  #  tt.setTimer(0, False)
  #  print("Off")

  #update previous input
  #prev_input = input
  #slight pause to debounce
  time.sleep(0.5)
