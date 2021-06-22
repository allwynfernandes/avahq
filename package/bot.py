import os
import time
import requests
import json

# API_KEY = os.getenv("TG_BOT_TOKEN_AVAHQ")


class Bot:
    def __init__(self, API_KEY):
        self.token = API_KEY 
        self.base = f"https://api.telegram.org/bot{self.token}"

    def get_updates(self, offset=None):
        url = self.base +"/getUpdates?timeout=100"
        if offset:
            url = url+f"&offset={offset +1}"
        r = requests.get(url)
        return json.loads(r.content)
    
    def send_message(self, msg=None, chatId=None):
        url = self.base + f"/sendMessage?chat_id={chatId}&text={msg}"
        if msg is not None:
            requests.get(url)
    
    def delete_message(self, chatId=None, messageId=None, waitTime=5, condition=False):
        '''
        This deletes the message sent by the bot after a time interval.
        The ID of the bots's message is an increment by 1 of the ID of the message sent by the user.
        '''
        time.sleep(waitTime)
        botMessageId = messageId+1
        url = self.base + f"/deleteMessage?chat_id={chatId}&message_id={botMessageId}"
        if condition:
            requests.get(url)

