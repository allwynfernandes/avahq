# Functions for all special functions and abilities
import re


def extract_keywords(message, kwtype):
    if kwtype == 'hashtag':
        pattern = re.compile(r"#(\w+)")
    if kwtype == 'mention':
        pattern = re.compile(r"@(\w+)")               
    elif kwtype == 'number':
        pattern = re.compile(r"\d+")
    else:
        print("No keyword found")
        # keywordList = None


    keywordList = pattern.findall(message)
    return keywordList



def money_tracker():
    # Accepts the message string as an argument
    # Picks up the first mention of a number as total expense for the message
    # Picks up any category tags mentioned in message.
    pass


def journal_letter():
    # Fetch all entries of specified date from db
    # Turn them into a html string along with beautiful css
    # Convert html to PDF
    # Send pdf to user
    pass