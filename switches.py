import time
import RPi.GPIO as GPIO
from toggleTime import toggleTimers
from switch import switch

#initialise a previous input variable to 0 (assume button not pressed last)
prev_input = 0

#list for button objs
swtichObjList = []

#Setup button
switchPins = [27, 17, 4, 18]

#init button pin objects
timerIndex = 0
for switchPin in switchPins:
  switchobj = switch(switchPin, timerIndex)
  swtichObjList.append(switchobj)
  timerIndex += 1

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
for pin in switchPins:
  GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pins to be input pins and set initial value to be pulled low (off)

tt = toggleTimers()

while True:
  for switch in swtichObjList:
    input = GPIO.input(switch.pinNumber)
    switchState = switch.checkInput(input)
    if switchState is not None:
      tt.setTimer(switch.timerIndex, switchState)

  time.sleep(0.5)
