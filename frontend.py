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
        self.screen.addstr(2, 2, prompt_string)
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
        self.screen.addstr(2, 2, 'Current task:')
        self.screen.addstr(5, 4, display_string)
        self.screen.hline((self.max_y-3), 1, curses.ACS_HLINE, (self.max_x-2))
        self.screen.addstr((self.max_y-2), 2, 'f - [Finish task]')
        self.screen.refresh()

    def menu(self, message=''):
        """ display main menu
        """
        self.set_screen()
        self.add_str("Please enter a number...", x=2, y=2)
        self.add_str("1 - Start new task", x=4, y=4)
        self.add_str("2 - Exit", x=4, y=5)

    def exit(self):
        """ reset curses and exit
        """
        curses.echo()
        curses.nocbreak()
        curses.endwin()
