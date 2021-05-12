from bot import chatbot

update_id = None


def bot_reply(userMessage):
    if userMessage is not None:
        reply = "Okay"
    return reply

while True:
    print("...")
    updates = get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
            except:
                message = None

            fromUserId = item["message"]["from"]["id"]
            fromUserName = item["message"]["from"]["first_name"]
            reply = bot_reply(message)
            bot.send_message(reply, fromUserId)



