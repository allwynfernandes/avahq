import datetime
import pytz

# These are a set of routines or activities that have to be performed either
# (a) continually in parallel with other tasks. Eg: While loop checking for message from user
# (b) once a day at 00:01. Eg: refresh the daily reminder cache.
# 
# 
# 


def general_reminder():
    # At 9 query db for reminders of the day
    # Send a summary message at 9am of all the reminders for the day
    pass

def special_reminder():
    # It takes an argument 'type' specifying as birthday.
    # Query db for all birthday's today and send summary message at 10am
    # Add append a general happy birthday wishes message.
    pass


def notification_schedule(reply, fromUserId):
    # Following are your reminders for today
    # These are the birthdays today and tomorrow
    # Todays's budget for your spend categories is as follows {key:val}
    when = datetime.datetime.now().replace(hour=9, minute=1, second=0, microsecond=0)
    # things to do in mjour 1 as per standard scheudle
    # things to do in mjour 2 as per standard scheudle
    # things to do in mjour 3 as per standard scheudle
    # things to do in mjour 4 as per standard scheudle
    
    if when == datetime.datetime.now().replace(second=0, microsecond=0):
        reply = None
        if reply != None:
            bot.send_message(reply,fromUserId)
    pass
