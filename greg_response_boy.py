import time
import random
from slackclient import SlackClient

token = "fill in"
sc = SlackClient(token)

img_urls = {'kd': 'http://i.imgur.com/1zABkKu.jpg',
            'hospital': 'http://i.imgur.com/Q3wQP8K.jpg',
            'tube': 'http://i.imgur.com/OSV2Hf1.jpg',
            'suit': "http://i.imgur.com/xjQWQdS.png",
            'awful': 'http://i.imgur.com/EiOpCuo.jpg',
            'jersey': 'http://i.imgur.com/l9B5a6B.jpg',
            'muscles' : 'https://imgur.com/a/3Pb8m',
            'smile' : 'https://imgur.com/a/04CXM',
            'euro' : 'https://imgur.com/a/x8jbt'
}

emojiis = ["japanese_ogre",
           "male_zombie", "dancer",
          "unicorn_face", 
          "mushroom",
          "snowman_without_snow", 
          "eggplant", 
          "fried_shrimp",
          "woman-lifting-weights", "gun", 
          "put_litter_in_its_place",
          "face_with_rolling_eyes",
          "face_with_cowboy_hat",
          "selfie",
          "bomb", 
          "hankey"
]



greg_responses = [#"You know what, %s? There's a jet stream of bullshit coming out of your mouth, you are busted buddy!",
                #"%s, you are such a schmohawk.",
                #"%s, i'm sad\n"+img_urls['awful'],
                "%s, I hate trash people.",
                #"Ugh",
                #"I just pulled my ass bowling",
                "%s, Don't be a dipshit.",
                "I think we keep Jaylen Brown here",
                #"I have nipples, %s, could you milk me?!",
                "eh, I don't think so, %s (walks away)", 
                "Marcus smart and Devin booker about equal",
                #"ahhhhh",
                "ughhhhhh",
                ":zany_face: :face_with_thermometer:",
                ":frowning: :sneezing_face:",
                ":nauseated_face: :face_vomiting:",
                #":face_with_cowboy_hat: :selfie::skin-tone-2:",
                #"CANNONBALL :sweat_drops::man-running::skin-tone-2:",
                "You wanna ruin this chat? I'll ruin this chat", 
                "I see what you're tryin to do, %s, and I'm not impressed",
                #"%s..........did Dirk put you up to this",
                #"%s..........did Eric put you up to this",
                #"%s..........did Buckets put you up to this",
                #"https://media0.giphy.com/media/8kqrtQiz9YqnS/giphy-downsized.gif",
                #"https://media.giphy.com/media/3oEduKw6b2PEA4KH6g/giphy.gif",
                #"https://media.giphy.com/media/UB2plibLoLkME/giphy.gif",
                #":smiley::cookie:",
                ":kissing::wine_glass:",
                ":angry::raised_hand_with_fingers_splayed::skin-tone-2::basketball:",
                "Cigs taste better I think",
                #"Ollie's are the easiest trick, tough to be legendary. %s get real", 
                "I'm team koc",
                "don't listen to this :point_up::skin-tone-2:", 
                "was this a jokic flex @Pow?",
                #"http://gph.is/1RQAYNI",
                #"http://gph.is/194ML2c", 
                "%s, find a new slant",
                "Vantine, the hawks are fucking terrible.", 
                "Anyone know how to snooze the chat?",
                "Are you kidding me??",
                "did that feel good, %s", 
                "guys, live a little",
                #"https://media0.giphy.com/media/u4leCTZfHAmxW/giphy-downsized.gif?cid=6104955e5bf03fbb31715641670d2ae8",
                "I'm not that frustrated by it",
                "Leaving this channel if anymore gbbs spoilers",
                "https://giphy.com/gifs/santa-bad-QIpSB9yTqCjWo",
                "getting chilly in here",
                "*sips eggnog*, *spits out eggnog*",
                "spoken like a true Sand %s",
                ":hammer: GREG SMASH",
                "Go eat a salad at Oracle and leave regular people alone ESPN"
                "Narc ass article",
                #"merry fucking chuckmas",
                "today's Tommy points go to.... %s!",
                "https://giphy.com/gifs/test-jess-home-video-curb-your-enthusiasm-SkOHoAarPEoHC",
                
                

]


def sendGregism(chan):
    text_idx = random.randint(0,len(greg_sayings)-1)
    sc.api_call(
        "chat.postMessage", channel=chan, text=greg_sayings[text_idx],
        username='SandGreg',
        icon_url="http://i.imgur.com/xjQWQdS.png"
    )

def sendGregResponse(chan, user_str):
    text_idx = random.randint(0,len(greg_responses)-1)
    if greg_responses[text_idx].find("%s") == -1:
      response = greg_responses[text_idx]
    else:
      response = greg_responses[text_idx] % (user_str)
    #if random.randint(0,100) > 75:
    #  response = response.upper()
    sc.api_call(
        "chat.postMessage", channel=chan, text=response,
        username='SandGreg',
        icon_url="http://i.imgur.com/rw68aGx.jpg"
    )

base_name_list = ['greg', 'gsj', 'johnson', 'wurst',  'gerg', 'Greg', 'also', 'anyone', 'thoughts', "celtics"]
punctuation = [',', '.', "?", "!"]

name_list = []
for n in base_name_list:
  for p in punctuation:
    name_list.append(n+p)

name_list = name_list + base_name_list

slash_names = ['/'+name for name in name_list]

def getUsersList():
    res = sc.api_call("users.list")
    print res
    users = {}
    for user in res['members']:
        if not user['is_bot']:
            #users[user['id']] = user['profile']['last_name']
            users[user['id']] = user['profile']['display_name']

    return users

def isGreg(msg):
    msgs = msg.split()
    for msg in msgs:
        if msg.lower() in name_list:
            return True
    return False

def isSlashGreg(msg):
  msgs = msg.split()
  for m in msgs:
    #if msg.lower() == "/greg":
    if m.lower() in slash_names:
      return True

  return False

def sendGregImg(chan):
  idx = random.randint(0,len(img_urls.keys()) )
  #response = "http://i.imgur.com/xjQWQdS.png"
  response = img_urls[img_urls.keys()[idx]]
  sc.api_call(
        "chat.postMessage", channel=chan, text=response,
        username='SandGreg',
        icon_url="http://i.imgur.com/rw68aGx.jpg"
    )

filter_chan = "CA2KL36BG"
if sc.rtm_connect():
  users = getUsersList()
  #print users
  while True:
    last_read = sc.rtm_read()
    if last_read:
      try:
          parsed = last_read[0]['text']
          user = last_read[0]['user']
          print last_read
          print users[user], parsed
          #reply to channel message was found in.
          message_channel = last_read[0]['channel']
          if parsed and isGreg(parsed):
            sendGregResponse(message_channel, users[user])
          elif parsed and isSlashGreg(parsed):
            sendGregImg(message_channel)
          elif parsed and message_channel == filter_chan:
            print "in general"
            if random.random() <= 1./100.:
              sc.api_call(
                    "chat.postMessage", channel=filter_chan, text="_"+parsed+"_",
                    username='SandGreg',
                    icon_url="http://i.imgur.com/xjQWQdS.png"
                )         
            elif random.random() <= 1./50.:
              print "here in response mojiis"
              sc.api_call("reactions.add", channel=filter_chan, name=emojiis[random.randint(0,len(emojiis)-1)],  timestamp=last_read[0]['event_ts'])
              pass
            

      except:
          print "something not found!!!!!!!!!!!"
          print last_read
          pass
      time.sleep(1)

else:
    print "Connection Failed, invalid token?"
