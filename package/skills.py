# Functions for all special functions and abilities
# import pandas as pd
from .helpers import *

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

def show_records(coll=None, conditionDict=None, columnsDict=None, limit=0 ):
    queryResult = query_db(coll, conditionDict, columnsDict, limit, sortBy="dtExtracted")
    result = dict((x.values()) for x in queryResult)
    result = str(result).replace(",", "\n").replace("{", "").replace("}", "")


    # df = pd.DataFrame(queryResult)
    # df['dtExtracted'] = df['dtExtracted'].dt.strftime("%a, %d %b %H:%M %p")
    # df = df.to_markdown
    # df = f"```{df.to_markdown}```"
    return result

