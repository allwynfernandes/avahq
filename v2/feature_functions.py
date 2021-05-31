import os
import datetime
import parsedatetime

API_KEY = os.getenv('API_KEY')

def testFF():
    print("testing feature functions")

def general_reminder():
    pass

def birthday_reminder():
    pass

def message_saved():
    pass



def date_extractor(message):
    '''
    On input of string, returns extracted date in string format
    '''
    cal = parsedatetime.Calendar()
    now = datetime.datetime.now()
    extracted_date = cal.parseDT(message)[0].strftime("%Y-%m-%d, %H:%M:%S")
    return extracted_date

