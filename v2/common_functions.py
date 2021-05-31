

def testCF():
    print("testing common functions")


def save_to_db():
    pass

def fetch_from_db():
    pass

def send_message():
    pass

def hook_extractor(message, HOOKLIST):
    '''
    Separates hook and body via partition.
    Returns None if hook not found and same message.
    '''
    hookFound = 0
    for x in list(HOOKLIST.values()):        
        if message.startswith(tuple(x)):
            hook = x[0].split(' ')[1]
            for i in x:
                if message.startswith(i):
                    hookId = i
                    body = message.partition(i)[-1]
                    hookFound = 1
            break
        else:
            hook = "default"
            hookId = "dsave"
            body = message

    return (hook, hookId, body, hookFound)


def execute_intent(hook, body):
    pass
