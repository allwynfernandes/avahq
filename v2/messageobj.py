import logging
import datetime
import parsedatetime
from pymongo import MongoClient
from constants import *

class Message:
    '''
    Input::
    Message ID: Unique ID of the message
    User ID: User from whom message received
    Message: message as received
    Hooklist: For hook lookup
    
    Returns::
    messageId: str,
    fromUserId: str,
    message: str,
    dtCreated: datetime,
    hook: str,
    hookId: str,
    body: str,
    hookFound: Boolean,
    intentFound: Booleen
    '''

    def __init__(self, chatId, messageId, fromUserId, username, message, HOOKLIST, INTENTLIST, collection, dbSearchQuery=None):
        self.chatId = chatId
        self.messageId = messageId
        self.fromUserId = fromUserId
        self.username = username
        self.message = message
        self.dtCreated = datetime.datetime.now()
        self.hookFound = False
        self.intentFound = False
        self.isReminder = False
        self.dtExtracted = datetime.datetime(1970,1,1) # Default value for date to satisfy mongoDB insert command


        self.extract_hook(HOOKLIST, INTENTLIST)
        self.execute_hook(collection, dbSearchQuery=None)

    def extract_hook(self, HOOKLIST, INTENTLIST):
        '''
        Separates hook and body via partition.
        Returns None if hook not found and same message.
        '''
        # Extract a hook from the message
        for x in list(HOOKLIST.values()):        
            if self.message.lower().startswith(tuple(x)):
                self.hook = x[0].split(' ')[1].lower()
                for i in x:
                    if self.message.lower().startswith(i):
                        self.hookId = i
                        self.body = self.message.lower().partition(i)[-1]
                        self.hookFound = True
                break
        
        # Assign default values if hook not found
            else: 
                self.hook = "default"
                self.hookId = "dsave"
                self.body = self.message

        # Assign True if hook is an intent False if not
        self.intentFound = True if self.hook in INTENTLIST else False

        # First sentence is title if valid hook found. Else no title.
        if self.hookFound:
            self.title = self.message.partition(". ")[0].replace(self.hookId, "").title()
        else:
            self.title = ""

        
        return None
    





    def execute_hook(self, collection, dbSearchQuery=None):
        if not self.intentFound:
            self.save_to_db(collection)
            self.serviceReply = "💌" # If no intent then just save the message to db and send a 'message saved' service message to user
        else: # Note to self: maybe I'll create an intent class that lives in another file and I just call it here. 
            if self.hook == 'bookmark':
                pass
            elif self.hook == 'show':
                if 'reminders' in self.message.lower():
                    dbSearchQuery = {"isReminder" : "True"}
                    self.searchResult = self.search_db(collection, dbSearchQuery, {'_id':0, 'title':1, 'dtExtracted':1})
                    
            elif self.hook == 'remind':
                self.isReminder = True
                self.dtExtracted =  self.extract_date()
                self.save_to_db(collection)
                self.serviceReply = "⏰" # If no intent then just save the message to db and send a 'message saved' service message to user

            elif self.hook == 'timeit':
                pass
            elif self.hook == 'help':
                self.serviceReply = "This is a help text"
            else:
                pass

            # Once intent is executed a service message ("jobs done") message needs to be sent to the user
            # Im not sure if this should be done by the message class or the bot class. As on [[2021-06-03]]
            # self.send_service_message("The x intent has been executed")
        return None



    def extract_date(self):
        '''
        On input of string, returns extracted date in string format
        Extracts date by comparing string to current time in parseDT
        '''
        cal = parsedatetime.Calendar()
        return  cal.parseDT(self.message, self.dtCreated)[0]


    def search_db(self, collection, dbSearchQuery, projection):
        return collection.find(dbSearchQuery, projection)
        

    def save_to_db(self, collection):
        self.dbDocument = {
            'messageId' : self.messageId,
            'body' : self.body,
            'title' : self.title,
            'hook' : self.hook,
            'hookId' : self.hookId,
            'dtCreated' : self.dtCreated,
            'dtExtracted' : self.dtExtracted,
            'isReminder' : self.isReminder
        }

        self.dbInsertId = collection.insert_one(self.dbDocument).inserted_id






