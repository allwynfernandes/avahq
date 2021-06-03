#  First item of hook value should also be 'ava x' where x is the action.
HOOKLIST = {
    'read' : ['ava read ', '.ak '], 
    'unique' : ['ava unique ', '.au ' ],
    'word' : ['ava word ', '.aw '],
    'dayscore': ['ava dayscore ', '.ad '],
    'cause' : ['ava cause', '.ay '],
    'awesome' : ['ava awesome ', '.aa '],
    'upset' : ['ava upset ', '.ap '],
    'regret' : ['ava regret ', '.ar '],
    'impove' : ['ava improve ', '.ai '],
    'myself' : ['ava myself ', '.am '], # Self-introspection / self-realization
    'grateful' : ['ava grateful ', '.ag ' ],
    'forgive' : ['ava forgive ', '.af '],
    'connect' : ['ava connect ', '.ac '],
    'save' : ['ava save ', '.as ', '/save ', '/s '],



    'do' : ['ava do ', '/do ', '/d '],
    'bookmark' : ['ava bookmark ', '/bookmark ', '/b ', 'http', 'file:', 'www'], # Not sure about bookmark, wont work with play.io etc 
    'show' : ['ava show ', '/show ', '/o '],
    'remind' : ['ava remind ', '/remind ', '/r ', 'ava remind me '],
    'timeit' : ['ava timeit ', '/timeit ', '/t '],
    'shorten' : ['ava shorten ', 'ava short ' ] # shorten url
}

INTENTLIST = ['do', 'show', 'bookmark', 'remind', 'timeit']


DIAPROMPTS = {
"read" : "Which article did you read today?",
"unique" : "What was unique about today?",
"words" : "Describe the day in 3 words?",
"dayscore" : "What's today's sentiment score vs yesterday?",
"cause" : "Why do you feel this way? Whats the cause?",
"awesome" : "What was awesome about today?",  
"upset" : "Upset of the day?",
"regret" : "What did you regret today?",
"difftomorrow" : "What would you want to do differently tomorrow?",
"impove" : "What would you want to improve tomorrow?",
"dotomorrow" : "Top activity of tomorrow?",
"presence" : "Today's realization of presence?",
"myself" : "Today's realization about self?",
"grateful" : "5 things you are grateful for today?",
"forgive" : "Who would you like to forgive today?",
"connect" : "Who did you connect with today and what did you speak?",
"bookmark" : "Any attachments you would like to share?",
}





