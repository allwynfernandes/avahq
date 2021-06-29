import logging
import datetime
import parsedatetime
from pymongo import MongoClient
from .constants import *
from .helpers import *
from .skills import *


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

    def __init__(self, updateId, chatId, messageId, fromUserId, fname, username, message, HOOKLIST, INTENTLIST, DIAPROMPTS, collection, dbSearchQuery=None):
        self.updateId = updateId
        self.chatId = chatId
        self.messageId = messageId
        self.fromUserId = fromUserId
        self.fname = fname
        self.username = username
        self.message = message
        self.dtCreated = datetime.datetime.now()
        self.hookFound = False
        self.intentFound = False
        self.isReminder = False
        self.dtExtracted = datetime.datetime(1970,1,1) # Default value for date to satisfy mongoDB insert command
        self.isDeletable = True
        self.deleteWaitTime = 3
        self.serviceReply = "Sorry I didn't get that but the message has been saved.\nTry typing: ```/help```"
        self.mentions = extract_keywords(self.message, 'mentions')
        self.tags = extract_keywords(self.message, 'hashtags')
        self.amount = extract_keywords(self.message, 'numbers')
        self.amount = 0 if self.amount == [] else int(self.amount[0])
        self.requestedMessageId = extract_keywords(self.message, 'requestedMessageIds')
        # self.taskStatus = None # done, archive, active


        self.extract_hook(HOOKLIST, INTENTLIST)
        self.execute_hook(DIAPROMPTS, collection, dbSearchQuery=None)

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
    





    def execute_hook(self, DIAPROMPTS, collection, dbSearchQuery=None):
        if not self.intentFound:
            self.deleteWaitTime = 10
            self.save_to_db(collection)
            # If no intent then just save the message to db and send a 'message saved' service message to user
            # self.serviceReply = "💌" 
            if self.hook in DIAPROMPTS.keys():
                hookPos = list(DIAPROMPTS).index(self.hook)
                if hookPos < len(DIAPROMPTS)-1:
                    self.serviceReply = f"👍 {self.hook.title()}\n\n☝️ {list(DIAPROMPTS.values())[hookPos+1]}"
                else:
                    self.serviceReply = "🏆 All entries made! 🏆"
            else:
                self.serviceReply="Sorry I didn't catch that but the message is saved.\nTry typing: ```/help```"
        
        
        else: # Note to self: maybe I'll create an intent class that lives in another file and I just call it here. 
            if self.hook == 'bookmark':
                self.save_to_db(collection)
                self.serviceReply = "Feature in development 💌" 

            elif self.hook == 'show':
                self.dtExtracted = extract_date(self.message)
                if 'reminders' in self.message.lower():
                    self.dbSearchOperator = "$eq" if "today" in self.message.lower() else "gte"
                    self.dbSearchQuery = {'isReminder':True, 'fromUserId':self.fromUserId, 'dtExtracted':{self.dbSearchOperator:self.dtExtracted}}
                    self.dbProjection = {'_id':0, 'messageId':1, 'body':1 } # Alert: Can extract only 2 fields at a time using dict instead of pandas
                    limit = 0
                    self.serviceReply = show_records(collection, self.dbSearchQuery, self.dbProjection, limit)
                    self.isDeletable = False
                    # working mongo query:  db.responses.find({$and: [{'isReminder':true}, {dtExtracted:{$gt:ISODate('2021-05-01')}} ]},{_id:0, title:1, dtExtracted:1})
                    # self.dbSearchQuery = db.responses.find({$and: [{'isReminder':true}, {'dtExtracted':{$gt:ISODate({self.dtCreated.isoformat()})}} ]},{'_id':0, 'title':1, 'dtExtracted':1})"
                    # self.dbProjection = {'_id':0, 'title':1, 'dtExtracted':1}
                    # self.searchResult = self.search_db(collection)
                # self.serviceReply = "Feature in development 💌" 


            elif self.hook == 'do':
                self.serviceReply = "Feature in development 💌" 

            elif self.hook == 'shorten':
                self.serviceReply = "Feature in development 💌" 

            elif self.hook == 'remind':
                self.isReminder = True
                self.dtExtracted =  extract_date(self.message)
                self.save_to_db(collection)
                self.serviceReply = "⏰" # If no intent then just save the message to db and send a 'message saved' service message to user

            elif self.hook == 'timeit':
                self.serviceReply = "Feature in development 💌" 

            elif self.hook == 'help':
                self.serviceReply = HELPTEXT
                self.isDeletable = False

            elif self.hook == 'jour':
                self.serviceReply = JOURNALTAGS
                self.isDeletable = False

            else:
                pass

            # Once intent is executed a service message ("jobs done") message needs to be sent to the user
            # Im not sure if this should be done by the message class or the bot class. As on [[2021-06-03]]
            # self.send_service_message("The x intent has been executed")
        return None




    def save_to_db(self, collection):
        self.dbDocument = {
            'updateId' : self.updateId,
            'chatId' : self.chatId,
            'messageId' : self.messageId,
            'fromUserId' : self.fromUserId,
            'username' : self.username,
            'body' : self.body,
            'title' : self.title,
            'hook' : self.hook,
            'hookId' : self.hookId,
            'dtCreated' : self.dtCreated,
            'dtExtracted' : self.dtExtracted,
            'isReminder' : self.isReminder,
            'mentions' : self.mentions,
            'tags' : self.tags,
            'amount' : self.amount


        }

        self.dbInsertId = collection.insert_one(self.dbDocument).inserted_id




