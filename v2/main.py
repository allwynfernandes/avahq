# # Actions:
# [[2021-05-31]] 
# DONE:
# * HOOKLIST, DIAPROMPTS, hook_extractor, date_extractor 
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





import os
import logging
import datetime
import parsedatetime
import pandas as pd

from feature_functions import *
from common_functions import *
from constants import *


# Testing 
try:
    while True:
        m = input("Message: ")
        print(hook_extractor(m, HOOKLIST))
except:
    print('\b\b\b \nbye')
# Testing


