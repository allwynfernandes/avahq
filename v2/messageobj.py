import os
import logging
import datetime
import parsedatetime
import pandas as pd
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

    def __init__(self, messageId, fromUserId, message):
        self.messageId = messageId
        self.fromUserId = fromUserId
        self.message = message
        self.dtCreated = datetime.datetime.now()

    def extract_hook(self, HOOKLIST, INTENTLIST):
        '''
        Separates hook and body via partition.
        Returns None if hook not found and same message.
        '''
        # Extract a hook from the message
        self.hookFound = False
        for x in list(HOOKLIST.values()):        
            if self.message.startswith(tuple(x)):
                self.hook = x[0].split(' ')[1]
                for i in x:
                    if self.message.startswith(i):
                        self.hookId = i
                        self.body = self.message.partition(i)[-1]
                        self.hookFound = True
                break
        
        # Assign default values if hook not found
            else: 
                self.hook = "default"
                self.hookId = "dsave"
                self.body = self.message

        # Assign True if hook is an intent
        self.intentFound = True if self.hook in INTENTLIST else False
        
        return None
    

    def execute_hook(self, HOOKLIST):
        pass



