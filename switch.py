class switch:
    def __init__(self, pinNumber, timerIndex):
        self.pinNumber = pinNumber 
        self.timerIndex = timerIndex
        self.prevInput = 0

    def getPinNumber(self):
        return self.pinNumber

    def checkInput(self, input):
        isOn = None
        if((not self.prevInput) and input):
            isOn = True
        elif(self.prevInput and (not input)):
            isOn = False
        
        self.prevInput = input
        return isOn
            
