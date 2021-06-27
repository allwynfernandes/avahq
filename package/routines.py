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

