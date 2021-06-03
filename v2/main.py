# # Actions:
# [[2021-05-31]] DONE:
# * HOOKLIST, DIAPROMPTS, hook_extractor, date_extractor  
#
# NEXT:
# * Implement message receval
# * watch https://www.youtube.com/watch?v=PTAkiukJK7E
# * then https://www.youtube.com/watch?v=NwBWW8cNCP4
# * fianal implementation https://www.youtube.com/watch?v=KRn2xb1bxXM
# * Consider changing word hook to intent since negative tone
# * Functional reminder feature, first create send_to_db()
# * Implement a friendly id system that will be useful for dealing with reminders. Add this as column in collection and in the fucntion. (reminderId = 2393242) simple increamtor.
# * Implement: execute_intent() it does the actual activity mentioned in intent hook
# * Message storing in mongo
# * Implement: serviceMessage = "No intent found, saved message as default"
#
# [[2021-06-01]] DONE:
# * Added bookmark hook to HOOKLIST, made Message class and put in its own module,
# NEXT:t
# pretty much worthless using others pybot modules, instead make your own framework for fun
# * Study official python API https://core.telegram.org/bots/api
# * https://core.telegram.org/bots/api#deletemessage; 
# * watch own framework TG bot https://www.youtube.com/watch?v=5nhdxpoicW4
# * pure api bot https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/rawapibot.py
# * watch https://www.youtube.com/watch?v=PTAkiukJK7E; https://www.youtube.com/watch?v=NwBWW8cNCP4

# [[2021-06-03]] DONE:
#  * Bot now accepts and stores messages in mongodb. Created mongodb collection for responses. Details in env. Added save_to_db to message class.
# NEXT:
# Work on the bot class
# * Read for fuzzy contact names search https://docs.atlas.mongodb.com/reference/atlas-search/text/#fields ; https://stackoverflow.com/questions/44833817/mongodb-full-and-partial-text-search

API_KEY = ""
MONGO_CONNECTION = ""

import logging
import datetime
import parsedatetime
from pymongo import MongoClient


from constants import *
from messageobj import Message
# from feature_functions import *
# from common_functions import *


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)



# Set constants and creds and initiate variables
client = MongoClient(MONGO_CONNECTION)
RESPONSES = ""
CONTACTS = ""


print(f"Bot started at {str(datetime.datetime.now())}") 


# Testing 

try:
    while True:
        m = input("Message: ")
        message = Message('23', '@kaf23', m, HOOKLIST, INTENTLIST, RESPONSES)
        # print(message.hook,"|", message.body,"|", message.title, "|", message.intentFound, message.hookFound )
        print(message.dbDocument)
        [print(x) for x in message.searchResult]
except (KeyboardInterrupt):
    print("Bye")

# Testing
