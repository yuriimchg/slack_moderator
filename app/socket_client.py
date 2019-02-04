import os

from slackclient import SlackClient
from slackeventsapi import SlackEventAdapter

sign_in_secret = os.environ['SLACK_SIGNING_SECRET']
slack_events_adapter = SlackEventAdapter(sign_in_secret, '/slack/events')

wtfbot_token = os.environ["SLACK_BOT_TOKEN"]
slack_clt = SlackClient(wtfbot_token)

slack_events_adapter.start(port=3001)