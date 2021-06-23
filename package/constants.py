#  First item of hook value should also be 'ava x' where x is the action.
HOOKLIST = {
    'learn' : ['ava learn ', '.al '], # What did you learn today. Reading, watching videos online, external sources.
    'unique' : ['ava unique ', '.au ' ],
    'word' : ['ava word ', '.aw '],
    'dayscore': ['ava dayscore ', '.ad '],
    'cause' : ['ava cause', '.ay '],
    'awesome' : ['ava awesome ', '.aa '],
    'upset' : ['ava upset ', '.ap '],
    'regret' : ['ava regret ', '.ar '],
    'introspection' : ['ava introspection ', '.ai '], # Self-introspection / self-realization
    'grateful' : ['ava grateful ', '.ag ' ],
    'forgive' : ['ava forgive ', '.af '],
    'connect' : ['ava connect ', '.ac '],
    'save' : ['ava save ', '.as ', '/save ', '/s '],




    'do' : ['ava do ', '/do ', '/d '],
    'bookmark' : ['ava bookmark ', '/bookmark ', '/b ', 'http', 'file:', 'www'], # Not sure about bookmark, wont work with play.io etc 
    'show' : ['ava show ', '/show ', '/o '],
    'remind' : ['ava remind ', '/remind ', '/r ', 'ava remind me '],
    'timeit' : ['ava timeit ', '/timeit ', '/t '],
    'shorten' : ['ava shorten ', 'ava short ' ], # shorten url
    'help' : ['ava help ', 'ava help', '/help ', '/help']
}

INTENTLIST = ['do', 'show', 'bookmark', 'remind', 'timeit', 'help']


DIAPROMPTS = {
"save" : "Any attachments you would like to share?\n\n👉 .as",
"learn" : "Which article did you read today?\n\n👉 .al",
"unique" : "What was unique about today?\n\n👉 .au",
"word" : "Describe the day in 3 words?\n\n👉 .aw",
"dayscore" : "What's today's sentiment score vs yesterday?\n\n👉 .ad",
"cause" : "Why do you feel this way? Whats the cause?\n\n👉 .ay",
"awesome" : "What was awesome about today?\n\n👉 .aa",  
"upset" : "Upset of the day?\n\n👉 .ap",
"regret" : "What did you regret today?\n\n👉 .ar",
# "difftomorrow" : "What would you want to do differently tomorrow?", # removed difftomorrow
# "impove" : "What would you want to improve tomorrow?",
# "dotomorrow" : "Top activity of tomorrow?",
# "presence" : "Today's realization of presence?",
"introspection" : "Today's realization about self?\n\n👉 .ai",
"grateful" : "5 things you are grateful for today?\n\n👉 .ag",
"forgive" : "Who would you like to forgive today?\n\n👉 .af",
"connect" : "Who did you connect with today and what did you speak?\n\n👉 .ac",
}



HELPTEXT = '''
I'm Ava, your personal crm bot.
I can help you remember birthdays, set reminders and keep a general log of your day.
To start with, Here's are a few entries from the day log / journal feature:
* Journaling with tags *
`
.al today I learnt about mastery learning. 
.ac called up Joseph from school. Its been ages!
.aw slow, productive, introspective
.ag I am grateful for the rains. I love the rains.  

`
Simply precede your text with the `.ax` tag and it gets stored with that id.
The fun part is that you can download and analyse all your enties at end of the week!
For a full list of all tags click here  https://telegra.ph/Ava-Bot-06-04

* Set Reminders *
`ava remind me to call boss tomorrow at 9am`
`/r pick up the trash next friday at noon`
`/r pay the bills 3 days from now`
Either of these tags work. Also, I can read time in natural language!

* Shorten urls *
`ava shorten https://www.youtube.com/watch?v=oHg5SJYRHA0`
I instantly replies with `Here's the shortened url: https://is.gd/2aLkKB`

*Summarize Long Articles*
`ava summary https://www.economist.com/the-boundary-between-crypto-and-fiat`

For a full list of my skills, check here.
You can pin this message for quick access or to show this message again, type `ava help`

'''

JOURNALTAGS = '''
List of journal tags
.al learn? 
.au unique? 
.aw word?
.ad dayscore?
.ay cause?
.aa awesome?
.ap upset?
.ar regret?
.ai instrospection?
.ag grateful?
.af forgive?
.ac connect?
.as save?


'''


