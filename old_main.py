import logging
import configparser
import datetime
import parsedatetime
from pymongo import MongoClient




from constants import *
from messageobj import Message
# from feature_functions import *
# from common_functions import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Storing secrets

API_KEY = "1730449786:AAEOwWFBxxy7YqLpOc6mFsSHLfNhc-CFQCU"
MONGO_CONNECTION = "mongodb://127.0.0.1:27017/"
client = MongoClient("mongodb://127.0.0.1:27017/")
RESPONSES = client.get_database("avahqtest").get_collection("responses")
CONTACTS = client.get_database("avahqtest").get_collection("contacts")
PAGE = "https://api.telegram.org/bot1730449786:AAEOwWFBxxy7YqLpOc6mFsSHLfNhc-CFQCU/getUpdates"






# Set constants and creds and initiate variables


print(f"Bot started at {str(datetime.datetime.now())}") 

# Testing 

try:
    while True:
        m = input("Message: ")
        message = Message('4653', '23', '@kaf23', m, HOOKLIST, INTENTLIST, RESPONSES)
        # print(message.hook,"|", message.body,"|", message.title, "|", message.intentFound, message.hookFound )
        print(message.dbDocument)
        # print(message.responseReply)
except (KeyboardInterrupt):
    print("Bye")

# Testing
