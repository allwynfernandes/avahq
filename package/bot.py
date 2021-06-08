import os
import requests
import json

API_KEY = os.getenv("TG_BOT_TOKEN_AVAHQ")


class Bot:
    def __init__(self):
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
