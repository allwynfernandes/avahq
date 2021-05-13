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
