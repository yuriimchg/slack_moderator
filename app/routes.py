import os
from app import app
from app import moderate
import slackclient
from datetime import datetime

token = os.environ.get('SLACK_TOKEN')
msg_receiver = os.environ.get('BOT_SEND_TO')
wtf_id = os.environ.get('SLACK_CHANNEL_ID')

clt = slackclient.SlackClient(token, channel=wtf_id)

wtf_resp = clt.api_call('groups.list')

members = clt.api_call('groups.info', channel=wtf_id)['group']['members']
posts = clt.api_call('groups.history', channel=wtf_id)['messages']
names = clt.api_call('users.list', channel=wtf_id)
id_to_name_dict = {n['id']:n['profile']['real_name'] for n in names['members']}


@app.route('/judgement_day', methods=['GET', 'POST'])
def judge():
    if os.environ['SLACK_MESSAGE_SENT'] != '1': #@and datetime.now().weekday() == 0:
        reactions = moderate.count_reactions(posts, id_to_name_dict)
        not_posted = moderate.check_who_did_not_post(members, posts, id_to_name_dict)
        message = moderate.create_message(not_posted, reactions)
        moderate.send_report(clt, message, msg_receiver)
        os.environ['SLACK_MESSAGE_SENT'] = '1'

        return f'Message sent to {msg_receiver}'
    return 'Sorry, try next Monday'


