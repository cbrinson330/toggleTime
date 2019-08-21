class config:
    def __init__(self):
        self.baseurl = "https://api.harvestapp.com/v2"
        self.token = ""
        self.accountId = ""
        self.switchPins = [] #array of ints for pin input using the pin names
        self.clientBlacklist = [] #array of strings for clients to not assign toggles to