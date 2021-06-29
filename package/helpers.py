import re
import parsedatetime
import datetime



def extract_keywords(message, kwtype):
    if kwtype == 'hashtags':
        pattern = re.compile(r"#(\w+)") 
    elif kwtype == 'jourtags': #plan B
        pattern = re.compile(r"^(.*?)\s.*")
    elif kwtype == 'actions':
        pattern = re.compile(r"-(\w+)")
    elif kwtype == 'mentions':
        pattern = re.compile(r"@(\w+)")               
    elif kwtype == 'numbers':
        pattern = re.compile(r"\d+")
    elif kwtype == 'requestedMessageIds':
        pattern = re.compile(r"i(\d+)")
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



def query_db(coll, conditionDict, columnsDict, limit=0, sortBy="_id"):
    result = coll.find(conditionDict, columnsDict).sort(sortBy, -1).limit(limit)
    return list(result)

