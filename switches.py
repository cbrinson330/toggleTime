import time
import RPi.GPIO as GPIO
from toggleTime import toggleTimers
from switch import switch
from config import config

#list for button objs
swtichObjList = []

#init button pin objects
timerIndex = 0
for switchPin in config.switchPins:
  switchobj = switch(switchPin, timerIndex)
  swtichObjList.append(switchobj)
  timerIndex += 1

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
for pin in switchPins:
  # Set pins to be input pins and set initial value to be pulled low (off)
  GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

tt = toggleTimers()

while True:
  for switch in swtichObjList:
    input = GPIO.input(switch.pinNumber)
    switchState = switch.checkInput(input)
    if switchState is not None:
      tt.setTimer(switch.timerIndex, switchState)

  time.sleep(0.5)
