
# Clip
Learn regex:
https://cheatography.com/davechild/cheat-sheets/regular-expressions/



https://www.youtube.com/watch?v=0Vy-x6YRFGw
PYBOT tute automagic: 
https://www.youtube.com/watch?v=KRn2xb1bxXM

https://dev.to/lordghostx/building-a-telegram-bot-with-python-and-fauna-494i


https://www.youtube.com/watch?v=NwBWW8cNCP4


https://www.youtube.com/watch?v=7qJFtGi0hNQ


https://api.telegram.org/bot1730449786:AAEOwWFBxxy7YqLpOc6mFsSHLfNhc-CFQCU/getUpdates?offset=0

# Flow
## Storage
- User sends a message to Ava bot on telegram. `ava remind me to call joshua on tuesday`
- The message is read by the bot, sent through the `which command` test to route the message to the right command channel.
- The message is broken into its constituent parts: `from_user_id`, `question_hook`, `body`, `dt_extracted`, `dt_created`
- If the message is of ava type `ava remind` its remind date is extracted and stored in `dt_extracted` in the `responses` collection
- A response message is sent to user `Message saved! 🐶`


## Reply
- Every day at 7:30am the responses db is filtered on `dt_extracted` for records with date of today.
- These records are made into a pretty formatted string and stored as a message in a single variable
- The variable is then sent as a message via Telegram to the user.

# Requirements

- Store data about questions, users, contacts, responses
- Integrate with some messaging api
- Receive and read messages from the api
- Send messages from the API


# Data Model

- Intent Collection
    # (List of intents)
- Question Collection
    - id
    - content
    - hook # (Simply store these response in the response collection with the extracted hook)
        - ava read
        - ava unique
        - ava word
        - ava score
        - ava reason
        - ava awesome
        - ava upset
        - ava regret
        - ava improve
        - ava presence
        - ava grateful
        - ava forgive
        - ava connect
    - intent 
        - ava do
        - ava save
        - ava show
        - ava remind me
        - ava tell
        - ava shop
        - # ( FUTURE INTENT and nice to haves)
        - ava search # (Search google for a string, returns a text body with url)
        - ava short {url} (returns shorted url) 
    - dt_created
    - dt_updated

- Response Collection
    - response_id
    - body
    - question_hook # (This is the intent of the response)
    - dt_extracted # (Date extracted from response body. Useful for reminders.)
    - from_user_id
    - mentions
    - dt_created
    - dt_updated

- Contact Collection
    - contact_id
    - first_name
    - family_name
    - short_name # (A nick or alternate name. EG: Joshua -> Josh)
    - full_name
    - collected_name # (Full name as collected from google contact)
    - phone1_value
    - first_contact_context # (Defaults to their company)
    - social_circle
    - interests
    - strength # (A single thing they are famous for, their strength)
    - isin_messaged
    - isin_wished # Boolen check as to should the person be considered for sending wishes, messages, etc
    - isin_vip # Booleen if is vip person or network
    - dt_birthday
    - dt_created
    - dt_updated


# Functions
- get_intent (hook extractor)
    - Extracts the intent from a response string.
- get_mentions
    - Returns a a list of people mentioned in the response string
    - Splits the string into single words, then looks up each word against the `full_name` column of `contacts collection`
- intent_processing
    - Main function that processes each string as per its extracted intent
    - It is a switch statement that runs through a list of things to do with a response message.
    - Failing each, it defaults to storing the response with intent "unprocessed"
- add_question
    - Adds a questions to the questions collection. add_question("text", "hook")


- Messaging API
    - Create client
    - send message
    - receive message


- Config file
    - Constants

- Runner/Server 

# Happy path Alpha
1. Server starts, reads config, initiates logger
2. Connects to db, checks if any tasks(birhtday reminder, questions due) need to be executed
3. Nofifys me of any birthday or query to be answered

# Happy path Beta
- All from alpha
4. Receives messages from me.
5. Saves response to DB in their respective question collection table

# Notes
Browser Link:
https://api.telegram.org/bot<token>/getUpdates
