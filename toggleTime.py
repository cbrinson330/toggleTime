import os
import json
import urllib.request
import datetime
from config import config

class toggleTimers:
    def __init__(self):
        self.config = config()
        #Set the time entries
        self.timeEntries = []
        self._getTimeEntries()
        print('Switch is controlling timer for: ')
        print(self.timeEntries[0]['client']['name'])

    def _getTodaysDate(self):
        today = datetime.datetime.now()
        yearString = str(today.year)
        monthString = str(today.month)
        dayString = str(today.day)

        #Add leading 0
        if(today.day < 10):
            dayString = '0' + dayString

        if(today.month < 10):
            monthString = '0' + monthString

        date = yearString + '-' + monthString + '-' + dayString
        return date

    
    def _getHeaders(self):
        headers = {
            "User-Agent": "ToggleTimer",
            "Authorization": "Bearer " + self.config.token,
            "Harvest-Account-ID": self.config.accountId
        }
        return headers

    def _getTimeEntries(self):
        url = self.config.baseurl + '?from=' + self._getTodaysDate()
        print(url)
        timeEntryHolder = []
        entries = self._makeRequest(url=url, isPatch=False)
        i = 0 
        while i < len(entries['time_entries']):
            timeEntry = entries['time_entries'][i]
            #only clients get swiches
            if(timeEntry != "LookThink"):
                timeEntryHolder.append(timeEntry)
            i += 1 

        self.timeEntries = timeEntryHolder
        return timeEntryHolder

    def _makeRequest(self, url, isPatch=False):
        request = urllib.request.Request(url=url, headers=self._getHeaders())
        if(isPatch):
            request.get_method = lambda: 'PATCH'

        try: 
            response = urllib.request.urlopen(request, timeout=5)
            responseBody = response.read().decode("utf-8")
            jsonResponse = json.loads(responseBody)
            return jsonResponse

        except urllib.error.URLError as e:
            print(e.reason)

    def setTimer(self, index, turnOn):
        #Ensure index is within bounds it's pssoible there 
        #will be more switches than time entries
        if(index < len(self.timeEntries)):
            url = self.config.baseurl + '/'+ str(self.timeEntries[index]['id'])
            if(turnOn):
                url += '/restart'
            else:
                url += '/stop'

            self._makeRequest(url, True)
