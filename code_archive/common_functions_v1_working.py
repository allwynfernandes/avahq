
import os
import logging
import datetime
import parsedatetime
import pandas as pd
from constants import *


def testCF():
    print("testing common functions")


def save_to_db():
    pass

def fetch_from_db():
    pass

def send_message():
    pass

def extract_hook(message, HOOKLIST):
    '''
    Separates hook and body via partition.
    Returns None if hook not found and same message.
    '''
    hookFound = False
    for x in list(HOOKLIST.values()):        
        if message.startswith(tuple(x)):
            hook = x[0].split(' ')[1]
            for i in x:
                if message.startswith(i):
                    hookId = i
                    body = message.partition(i)[-1]
                    hookFound = True
            break
        else:
            hook = "default"
            hookId = "dsave"
            body = message

    return (hook, hookId, body, hookFound)


def execute_hook(hook, body):
    pass


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

    def __init__(self, messageId, fromUserId, message, HOOKLIST):
        self.messageId = messageId
        self.fromUserId = fromUserId
        self.message = message
        self.dtCreated = datetime.datetime.now()
        self.hook, self.hookId, self.body, self.hookFound = extract_hook(self.message, HOOKLIST)
        self.intentFound = True if self.hook in INTENTLIST else False
        self.url = self.hookId+self.body.split(" ")[0]

    def send_to_db():
        pass



















