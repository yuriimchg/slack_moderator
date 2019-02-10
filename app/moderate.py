from datetime import datetime, timedelta
import os
from app import app


# All users must post
# All posts should have at least N the same reactions last week
# If today is [day], select all users and check their posts reactions
# If some user did not post, [action] him


class User:

    def __init__(self, name, list_of_posts):
        self.name = name
        self.posts = list_of_posts

    def has_enough_reactions(self, min_count):
        # Loop through the posts
        # If there is more, than min_count, exact reactions
        return True

    def kick(self):
        if not self.has_enough_reactions():
            # WTF bot kick user
            pass


def today_is_monday():
    if datetime.now().weekday() == 0:
        return True


def today_is_friday():
    if datetime.now().weekday() == 4:
        return True


def send_notification(people, event):
    if today_is_friday():
        pass

def kick_the_violator():
    """ Drop not interesting users """

    pass


