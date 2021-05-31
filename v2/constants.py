#  First item of hook value should also be 'ava x' where x is the action.
HOOKLIST = {
    'read' : ['ava read ', '.ar '],
    'unique' : ['ava unique ', '.au ' ],
    'word' : ['ava word ', '.aw '],
    'score': ['ava score ', '.as '],
    'cause' : ['ava cause', '.ay '],
    'awesome' : ['ava awesome ', '.aa '],
    'upset' : ['ava upset ', '.ap '],
    'regret' : ['ava regret ', '.ar '],
    'impove' : ['ava improve ', '.ai '],
    'myself' : ['ava myself ', '.am'],
    'grateful' : ['ava grateful ', '.ag ' ],
    'forgive' : ['ava forgive ', '.af '],
    'connect' : ['ava connect ', '.ac '],



    'do' : ['ava do ', '/do ', '/d '],
    'save' : ['ava save ', '/save ', '/s ', ],
    'bookmark' : ['ava bookmark ', '/bookmark ', '/b ', 'http', 'file:', 'www'], # Not sure about bookmark, wont work with play.io etc 
    'show' : ['ava show ', '/show ', '/o '],
    'remind' : ['ava remind  ', '/remind ', '/r ']
}

INTENTLIST = ['do', 'save', 'show', 'bookmark', 'remind']


DIAPROMPTS = {
"read" : "Which article did you read today?",
"unique" : "What was unique about today?",
"words" : "Describe the day in 3 words?",
"score" : "What's today's sentiment score vs yesterday?",
"feel" : "Why do you feel this way?",
"awesome" : "What was awesome about today?",  
"upset" : "Upset of the day?",
"regret" : "What did you regret today?",
"difftomorrow" : "What would you want to do differently tomorrow?",
"impove" : "What would you want to improve tomorrow?",
"dotomorrow" : "Top activity of tomorrow?",
"presence" : "Today's realization of presence?",
"self" : "Today's realization about self?",
"grateful" : "5 things you are grateful for today?",
"forgive" : "Who would you like to forgive today?",
"connect" : "Who did you connect with today and what did you speak?",
"bookmark" : "Any attachments you would like to share?",
}





