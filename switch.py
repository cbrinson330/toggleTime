class switch:
    def __init__(self, pinNumber, timerIndex):
        self.pinNumber = pinNumber 
        self.timerIndex = timerIndex
        self.prevInput = 0

    def checkInput(self, input):
        if((not self.prevInput) and input):
            isOn = True
        elif(self.prev_input and (not input)):
            isOn = False
        
        self.prevInput = input
        return isOn
            
