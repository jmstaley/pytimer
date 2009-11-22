from datetime import datetime
from database import Database

class Activity:
    """
    """

    def __init__(self, start='', end='', description='', state=''):
        self.start = start
        self.end = end
        self.description = description
        self.state = state

    def start_activity(self, description=''):
        """ start activity
        """
        self.description = description
        self.start = datetime.now()
        self.state = 'running'

    def end_activity(self):
        """ stop activity
        """
        self.end = datetime.now()
        self.state = 'finished'

    def fmt_duration(self, seconds):
        """ return duration formatted hh:mm:ss
        """
        hours = seconds / 3600
        seconds -= 3600*hours
        minutes = seconds / 60
        seconds -= 60*minutes
        return "%02d:%02d:%02d" % (hours, minutes, seconds)

    def duration(self, formatted=False):
        """ return duration in seconds
        """
        if self.end:
            delta = self.end - self.start
        else:
            delta = datetime.now() - self.start

        if formatted:
            duration = self.fmt_duration(delta.seconds)
        else:
            duration = delta.seconds
        return duration

    def save(self):
        """ Save object to database
        """
        db = Database()
        id = db.insert_record(self)
