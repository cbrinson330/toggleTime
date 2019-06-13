import os
import json
import urllib.request
import datetime
from config import config

class toggleTimers:
    def __init__(self):
        self.config = config()
        self.timeEntries = []

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
    
    def _makeRequest(self, url):
        #TODO handle data and post requetss
        request = urllib.request.Request(url=url, headers=self._getHeaders())
        try: 
            response = urllib.request.urlopen(request, timeout=5)
            responseBody = response.read().decode("utf-8")
            jsonResponse = json.loads(responseBody)

            return jsonResponse

        except urllib.error.URLError as e:
            print(e.reason)
    
    def getTodaysTimeEntries(self):
        if(len(self.timeEntries) == 0): 
            url = self.config.baseurl + '/time_entries?from=' + self._getTodaysDate()
            self.timeEntries = self._makeRequest(url=url)

        return self.timeEntries 


if __name__ == "__main__":
    tt = toggleTimers()
    print(tt.getTodaysTimeEntries())
