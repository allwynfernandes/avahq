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
# [[2021-05-31]] DONE:
# * Added bookmark hook to HOOKLIST, made Message class and put in its own module,
# NEXT:
# pretty much worthless using others pybot modules, instead make your own framework for fun
# * Study official python API https://core.telegram.org/bots/api
# * https://core.telegram.org/bots/api#deletemessage; 
# * watch own framework TG bot https://www.youtube.com/watch?v=5nhdxpoicW4
# * pure api bot https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/rawapibot.py
# * watch https://www.youtube.com/watch?v=PTAkiukJK7E; https://www.youtube.com/watch?v=NwBWW8cNCP4




import os
import logging
import datetime
import parsedatetime

from messageobj import Message
from feature_functions import *
from common_functions import *
from constants import *

from telegram.ext import Updater




logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)








print(f"Bot started at {str(datetime.datetime.now())}") 




























# bot = telegram.Bot(token=TOKEN)
# print(bot.get_me())



# Testing 
# try:
# while True:
#     m = input("Message: ")
#     message = Message('23', '@kaf23', m)
#     message.extract_hook(HOOKLIST, INTENTLIST)
#     print(message.hook, message.body, message.intentFound )
# except (KeyboardInterrupt):
# print("Bye")
# # print('\b\b\b \nbye')
# Testing
