import time
import random
from slackclient import SlackClient

token = "xoxb-341846637154-UUgcMU2QMRkPa5bDCHYsKcvC"
sc = SlackClient(token)


def getChannels():
    res = sc.api_call(
            "channels.list",
            exclude_archived=1
            )
    channels = {}
    for chan in res['channels']:
        channels[chan['id']] = chan['name']
    return channels

agg_list = [u'CA1NJAN1J', u'CA1U8BDBL', u'CA7GZ0ZRC']
twitter_chan = u'GA64LDU7K'


if sc.rtm_connect():
  channels = getChannels()
  print channels
  #print users
  while True:
    last_read = sc.rtm_read()
    if last_read:
      try:
        #   parsed = last_read[0]['text']
        #   user = last_read[0]['user']
          #print users[user], parsed
          #reply to channel message was found in.
          if 'channel' in last_read[0].keys():
            message_channel = last_read[0]['channel']
          else:
            message_channel = "1"
          if message_channel in agg_list:
            print "here, sending!"
            #print last_read[0].keys()
            #print last_read[0] 
            if 'attachments' in last_read[0].keys():
                all_data = last_read[0]['attachments'][0]
                print all_data
                if all_data:
                    parsed = last_read[0]['attachments'][0]['fallback']
                    print message_channel
                    print parsed 

                sc.api_call(
                    "chat.postMessage", channel=twitter_chan, text=parsed,
                    username='TwitterAgg',
                    icon_url="https://i.imgur.com/GJn4p53.png"
                )
      except:
          print "something not found!!!!!!!!!!!"
          print last_read
          pass
      time.sleep(1)

else:
    print "Connection Failed, invalid token?"