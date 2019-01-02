#!/bin/sh
if ps -ef | grep -v grep | grep twitter_agg.py; then
        true
else
        /usr/bin/python /home/mcrouse/SideProjects/slackbot/twitter_agg.py &
fi

echo "here"

if ps -ef | grep -v grep | grep greg_response_boy.py; then
        true
else
        /usr/bin/python /home/mcrouse/SideProjects/slackbot/greg_response_boy.py &
fi

exit 0

