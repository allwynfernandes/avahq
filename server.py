import os
import logging
import datetime
import re
import parsedatetime
from pymongo import MongoClient



from package.constants import *
from package.messageobj import Message
from package.bot import Bot
from package.routines import notification_schedule
# from feature_functions import *
# from common_functions import *

logging.basicConfig(filename="server_py_log.txt", format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# logging.disable(logging.CRITICAL)

API_KEY = os.getenv("TG_BOT_TOKEN_AVAHQ")
MONGO_CONNECTION = os.getenv("MONGO_URI")

client = MongoClient(MONGO_CONNECTION)
RESPONSES = client.get_database("avahqtest").get_collection("responses")
CONTACTS = client.get_database("avahqtest").get_collection("contacts")

logging.info("Constants and Keys loaded successfully")

# > db.responses.find({body:/shivani/i}, {_id:0, hook:1, title:1, body:1}).sort({_id:-1}).limit(3)


logging.info(f"Bot Started Successfully at: {str(datetime.datetime.now())}" )

print(f"Bot started at {str(datetime.datetime.now())}") 
bot = Bot(API_KEY)
update_id = None


def main(update_id):
    while True:
        print("...")
        updates = bot.get_updates(offset=update_id)
        logging.info(f"Update ID: {update_id}")
        logging.info(f"Update Value: {updates}")
        print(updates)
        updates = updates['result']

        logging.info("Updates received, Commence looping over elements")
        if updates:
            for item in updates:
                logging.info(f"this is item{item}")
                update_id = item['update_id']
                try:
                    messageId = item['message']['message_id']
                    message = item['message']['text']
                    username = item['message']['from']['username']
                    chatId = item['message']['chat']['id']
                    fromUserId = item['message']['from']['id']
                    fname = item['message']['from']['first_name']


                except:
                    messageId = None
                    message = None
                    username = None
                    chatId = None
                    fromUserId = None
                    fname = None

                updateId = update_id


                # Here on, call the Message class and do message stuff from main.py
                logging.info("Pushing data to database")
                if message != None:
                    order = Message(updateId, chatId, messageId, fromUserId, fname, username, message, HOOKLIST, INTENTLIST, DIAPROMPTS, RESPONSES)
                    logging.info(f"Message: {order.intentFound, order.hook, order.body, order.serviceReply} ")

                    reply = order.serviceReply
                    bot.send_message(reply,fromUserId)
                    bot.delete_message(chatId, messageId, order.deleteWaitTime, condition=order.isDeletable)
                    # notification_schedule()


if __name__ == '__main__':
    main(update_id)
