import time
import random
from slackclient import SlackClient

#token = "xoxp-56736860833-56736860881-56726044192-a32f372d44"# found at https://api.slack.com/web#authentication
##token = "xoxb-341846637154-UUgcMU2QMRkPa5bDCHYsKcvC"
#token = "xoxb-341846637154-GSUp1zUQ1tWVZ1v3bzxN5Hni"
#token = "xoxp-341969025893-341136014432-341299356833-d4c647cc1ab923f34819197b35de730e"
token = "xoxb-341846637154-GSUp1zUQ1tWVZ1v3bzxN5Hni"
sc = SlackClient(token)

img_urls = {'kd': 'http://i.imgur.com/1zABkKu.jpg',
            'hospital': 'http://i.imgur.com/Q3wQP8K.jpg',
            'tube': 'http://i.imgur.com/OSV2Hf1.jpg',
            'jersey': 'http://i.imgur.com/l9B5a6B.jpg'
}

greg_sayings = [#"I'm the WURST! " + img_urls['jersey'],
                #"i'm sad", 
                #"prettayyy prettayyy pretty good",
                "Just remember all caps when you spell the GREG's name",
                "Trying on pants is one of the most humiliating things a man can suffer that doesn't involve a woman.",
                "Marcus smart and Devin booker about equal",
                #"Powers, you are such a schmohawk.",
                #"Guys, stop being such schmohawks.",
                "DANNY AINGE SUBPAR DRAFTER?!",
                #"I'm literally the most undesirable man at Wake Forest.",
                #"Not a big sun guy. :sun:",
                #"I hate trash people.",
                "Anyone tryna get into some real ass shit tonight?  I'm bored and want to pour alcohol onto my brain.",
                "First beer of the day just cracked. :beer:",
                #"I just pulled my ass bowling",
                "I can't go on the Dan because I don't want people to see me with no shirt on",
                #"I control Kappa Delta with an invisible hand",
                #"Seacrest.... OUT",
                #"Freedarko store closes on Friday.  I'm pondering a last minute purchase of some of those prints.  Any thoughts?",
                #"You know what? There's a jet stream of bullshit coming out of your mouth my friend, you are busted buddy!" + img_urls['tube'],
                #"I'll have a vanilla...one of those vanilla bullshit things. You know, whatever you want, some vanilla bullshit latte cappa thing. Whatever you got.",
                "Nice disappearing act last night, Powers",
                "Nice disappearing act last night, Chuck",
                "Beautiful weather today....I hate it",
                "Awful weather today....I love it", 
                #"Ugh",
                #"Ugh",
                #"Ugh",
                #"I think I failed that test.",
                "Tun, I think I failed that test.",
                #":zany_face: :face_with_thermometer:",
                #":frowning: :sneezing_face:",
                #":nauseated_face: :face_vomiting:",
                #":face_with_cowboy_hat: :selfie::skin-tone-2:",
                "CANNONBALL :sweat_drops::man-running::skin-tone-2:",
                "talk to me Dirk",
                "Aren't like 80% of high schoolers juulheads",
                #"Windys had a great couple months guys", 
                "@Eric Johnson :point_right::hamburger:",
                #":smiley::cookie:",
                ":kissing::wine_glass:",
                #":angry::raised_hand_with_fingers_splayed::skin-tone-2::basketball:",
                "Cigs taste better I think",
                "Ollie's are the easiest trick, tough to be legendary dirk get real",
                #"I wonder what Tom's up to", 
                #"thinking about Tom......",
                "Chuck, guess what i'm thinking right now :expressionless:",
                "Ac green a HOFer if he fucked",
                "http://gph.is/1RQAYNI",
                "http://gph.is/194ML2c", 
                "Eric, just eat the damn hamburger",
                "*spits out beer* what is this a goddamn GOSE!?",
                "Rondo reformed and now the best teammate in the nba now",
                "Was this a jokic flex @Pow?",
                "Anyone know how to snooze the chat?",
                "Guess it's gonna be another one of those days huh Mo",
                #"Leaving this channel if anymore gbbs spoilers",
                #"Crouse, Mo, Eric... just reviewing my naughty list for Christmas",
                #"Dirk, you in the holiday spirit yet?",
                #"you get me a gift yet Eric?",
                "Eric wake up",
                "Crushed cheeseburgers both days then was never the same",
]


def sendGregism(chan):
    text_idx = random.randint(0,len(greg_sayings)-1)
    tom_bit = ["I wonder what Tom's up to", "thinking about Tom......"]
    sc.api_call(
        "chat.postMessage", channel=chan, text=greg_sayings[text_idx],
        username='SandGreg',
        icon_url="http://i.imgur.com/rw68aGx.jpg"
    )
    
    #time.sleep(60*60*1.5)
    #sc.api_call(
    #    "chat.postMessage", channel=chan, text=tom_bit[random.randint(0,len(tom_bit)-1)],
    #    username='SandGreg',
    #    icon_url="http://i.imgur.com/rw68aGx.jpg"
    #)

    print "sending message"
#print sc.api_call(
#        "chat.postMessage", channel="D1NMG45K9", text="Hello from Python! :tada:",
#        username='SandGreg',
#        icon_url="http://i.imgur.com/xjQWQdS.png"
#    )

num_hours = 24  
if sc.rtm_connect():
    while True:
        #sendGregism("D1NMG45K9")
        #time.sleep(10)
        time.sleep(60*60*num_hours)
        sendGregism("#general")
else:
    print "Connection Failed, invalid token?"
