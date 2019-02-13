from datetime import timedelta, datetime
import os


def get_date(unix_date):
    unix_date = float(unix_date)
    return datetime.fromtimestamp(unix_date)


def last_7_days_(posts):
    start_date = datetime.now() - timedelta(days=7)
    return list(filter(lambda x: get_date(x['ts']) > start_date, posts))


def count_reactions(posts, id_to_name):
    d = {}
    posts = last_7_days_(posts)
    for post in posts:
        author = get_name(id_to_name, post['user'])
        if 'reactions' in post.keys():
            max_reactions = max(p['count'] for p in post['reactions'])
        else: max_reactions = 0
        if author not in d.keys() or d[author] < max_reactions:
            d[author] = max_reactions
    return dict(sorted(d.items(), key=lambda x: x[1]))


def check_who_did_not_post(members, posts, id_to_name):
    black_list = []
    posts = last_7_days_(posts)
    users_posted = count_reactions(posts, id_to_name)
    for member in members:
        member = get_name(id_to_name, member)
        if member not in users_posted.keys():
            black_list.append(member)
    return black_list


def get_name(id_to_name, uid):
    name_list = id_to_name[uid]
    return name_list


def create_message(not_posted, reactions_dict):
    black_list = []
    if len(not_posted) > 1:
        not_posted_text = f'{len(not_posted)} users did not post anything:\n {", ".join(not_posted[:-1])} and {not_posted[-1]}'
    if len(not_posted) == 1:
        not_posted_text = f'Only {not_posted} did not post anything.'
    if len(not_posted) < 1:
        not_posted_text = f'Everyone posted last week.'

    for user, reaction in reactions_dict.items():
        if reaction < 3:
            black_list.append(user)
    weak_users_msg = f'These users worth posting to #random only: {", ".join(black_list)}. They should be excluded from wtf immediately!'

    return not_posted_text + '\n' + weak_users_msg


def send_report(client, message, receiver):
    client.api_call('chat.postMessage', channel=receiver, text=message)
