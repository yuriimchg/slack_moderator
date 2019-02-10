import os

from slackclient import SlackClient
from slackeventsapi import SlackEventAdapter

sign_in_secret = os.environ['SLACK_SIGNING_SECRET']
slack_events_adapter = SlackEventAdapter(sign_in_secret, '/slack/events')

wtfbot_token = os.environ["SLACK_BOT_TOKEN"]
slack_clt = SlackClient(wtfbot_token)

slack_events_adapter.start(port=3001)


class Bot:

    def __init__(self):
        self.client = SlackClient('')
        self.name = 'wtfbot'
        self.emoji = ':robot_face:'
        self.oauth = {
            'client_id': os.environ.get('SLACK_CLIENT_ID'),
            'client_secret': os.environ.get('SLACK_CLIENT_SECRET'),
            'scope': 'bot'
            }
        self.token = os.environ.get('SLACK_TOKEN')
        self.messages = {}

    def pass_authentification(self, code):
        resp = self.client.api_call(
            'oauth.access',
            client_id=self.oauth['client_id'],
            client_secret=self.oauth['client_secret'],
            code=code
        )
        team_id = resp['team_id']
        team[team_id] = {
            "bot_token": resp['bot']['bot_access_token']

        }
