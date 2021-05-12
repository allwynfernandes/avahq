# Requirements

- Store data about questions, users, contacts, responses
- Integrate with some messaging api
- Receive and read messages from the api
- Send messages from the API


# Data Model

- Question Collection
    - id
    - content
    - hook
        - ava save
        - ava show
    - dt_created
    - dt_updated

- Response Collection
    - response_id
    - content
    - question_hook
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
    - collected_name
    - phone1_value
    - first_contact_context
    - social_circle
    - interests
    - isin_messaged
    - isin_wished # Boolen check as to should the person be considered for sending wishes, messages, etc
    - isin_vip # Booleen if is vip person or network
    - dt_birthday
    - dt_created
    - dt_updated





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