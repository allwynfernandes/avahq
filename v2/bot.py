import requests
import json

class Bot:
    def __init__(self):
        self.token = "1730449786:AAEOwWFBxxy7YqLpOc6mFsSHLfNhc-CFQCU" #self.read_config(config)
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

    # def read_config(config):
    #     parser = configparser.ConfigParser()
    #     parser.read(config)
    #     return parser.get('secrets', 'API_KEY')