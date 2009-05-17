from datetime import datetime

class Activity:
    """
    """

    def __init__(self, start='', end='', description='', state=''):
        self.start = start
        self.end = end
        self.description = description
        self.state = state

    def start_activity(self, description=''):
        """
        """
        self.description = description
        self.start = datetime.now()
        self.state = 'running'

    def end_activity(self):
        """
        """
        self.end = datetime.now()
        self.state = 'finished'

    def duration(self):
        """
        """
        if self.end:
            duration = self.end - self.start
        else:
            duration = datetime.now() - self.start
        return duration.seconds
