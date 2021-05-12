#! /home/alf/pyenv/bin/activate
import requests
import json

class chatbot():
    def __int__(self, config):
        self.token = self.read_token(config)
        self.base = f"https://api.telegram.org/bot{self.token}"

    def get_updates(self, offset=None):
        url = self.base + "/getUpdates?timeout=100"
        if offset:
            url = url + "&offset={offset + 1}"
        r = requests.get(url)
        return json.loads(r.content)
    
    def send_message(self, msg, chatId):
        url = self.base + f"sendMessage?chat_id={chatId}&text={msg}"
        if msg is not None:
            requests.get(url)
    
    def read_token(self, configFile):
        token=open(configFile).readline().rstrip()
        return token