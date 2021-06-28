import re
import parsedatetime
import datetime



def extract_keywords(message, kwtype):
    if kwtype == 'hashtag':
        pattern = re.compile(r"#(\w+)") 
    elif kwtype == 'jourtag': #plan B
        pattern = re.compile(r"^(.*?)\s.*")
    elif kwtype == 'action':
        pattern = re.compile(r"-(\w+)")
    elif kwtype == 'mention':
        pattern = re.compile(r"@(\w+)")               
    elif kwtype == 'number':
        pattern = re.compile(r"\d+")
    elif kwtype == 'requestedMessageId':
        pattern = re.compile(r"id(\d+)")
    else:
        print("No keyword found")
        # keywordList = None


    keywordList = pattern.findall(message)
    return keywordList



def extract_date(message):
    '''
    On input of string, returns extracted date in string format
    Extracts date by comparing string to current time in parseDT
    '''
    cal = parsedatetime.Calendar()
    return  cal.parseDT(message, datetime.datetime.now())[0]

