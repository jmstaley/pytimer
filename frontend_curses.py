import curses

class Display:
    """
    """

    def __init__(self):
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.max_y, self.max_x = self.screen.getmaxyx()

    def set_screen(self):
        """ clear screen ready for new display
        """
        self.screen.clear()
        self.screen.border(0)

    def get_param(self, prompt_string):
        """ get user input from screen
        """
        self.set_screen()
        self.add_str(prompt_string, x=2, y=2)
        self.screen.refresh()
        curses.echo()
        input = self.screen.getstr(10, 10, 60)
        curses.noecho()
        return input

    def add_str(self, string, x=0, y=0):
        self.screen.addstr(y, x, string)

    def show_current(self, display_string):
        """ display the current task on screen
        """
        self.set_screen()
        self.add_str('Current task:', x=2, y=2)
        self.add_str(display_string, x=4, y=5)
        self.screen.hline((self.max_y-3), 1, curses.ACS_HLINE, (self.max_x-2))
        self.add_str('f - [Finish task]', x=2, y=(self.max_y-2))
        self.screen.refresh()

    def show_last(self, obj):
        self.add_str('Last activity:', y=7, x=5) 
        self.add_str('Description: %s' % obj.description, y=9, x=6)
        self.add_str('Start: %s' % obj.start.strftime('%d/%m/%Y %H:%M'), 
                      y=10, 
                      x=6)
        self.add_str('End: %s' % obj.end.strftime('%d/%m/%Y %H:%M'), 
                     y=11, 
                     x=6)
        self.add_str('Duration: %s' % (obj.end - obj.start),
                     y=13,
                     x=8)

    def menu(self, message=''):
        """ display main menu
        """
        self.set_screen()
        self.add_str("Please select an option...", x=2, y=2)
        self.add_str("1 - Start new task", x=4, y=4)
        self.add_str("2 - View activities", x=4, y=6)
        self.add_str("Q - Exit", x=4, y=8)

    def exit(self):
        """ reset curses and exit
        """
        curses.echo()
        curses.nocbreak()
        curses.endwin()

    def list_activities(self, results, schema=[]):
        """ display a list of results
        """
        self.set_screen()
        header = ''
        if schema:
            for title in schema:
                header += '%s\t' % title
            self.add_str(header, x=1, y=1)
        self.screen.hline((2), 1, curses.ACS_HLINE, (self.max_x-2))
        self.screen.refresh()
