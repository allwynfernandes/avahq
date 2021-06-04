import logging
import configparser
import datetime
import parsedatetime




from constants import *
from messageobj import Message
from bot import Bot
# from feature_functions import *
# from common_functions import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Storing secrets


print(f"Bot started at {str(datetime.datetime.now())}") 

bot = Bot()
update_id = None

while True:
    print("...")
    updates = bot.get_updates(offset=update_id)
    updates = updates['result']
    print("this is update", updates)
    if updates:
        for item in updates:
            print("this is item", item)
            update_id = item['update_id']
            try:
                message = item['message']['text']
            except:
                message = None

            messageId = update_id
            username = item['message']['from']['username']
            chatId = item['message']['chat']['id']
            fromUserId = item['message']['from']['id']


            # Here on, call the Message class and do message stuff from main.py
            order = Message(chatId, messageId, fromUserId, username, message, HOOKLIST, INTENTLIST, RESPONSES)

            reply = order.serviceReply
            bot.send_message(reply,fromUserId)






















