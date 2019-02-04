from datetime import datetime, timedelta
from app import app


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
