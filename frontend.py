import curses
import activity

class Display:
    """
    """

    def __init__(self):
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()

    def set_screen(self):
        self.screen.clear()
        self.screen.border(0)

    def get_param(self, prompt_string):
        self.set_screen()
        self.screen.addstr(2, 2, prompt_string)
        self.screen.refresh()
        curses.echo()
        input = self.screen.getstr(10, 10, 60)
        curses.noecho()
        return input

    def show_current(self, display_string):
        self.set_screen()
        self.screen.addstr(2, 2, 'Current task:')
        self.screen.addstr(5, 4, display_string)
        self.screen.hline(15, 1, curses.ACS_HLINE, 77)
        self.screen.addstr(16, 2, 'f - Finish task')
        self.screen.refresh()

    def menu(self, message=''):
        self.set_screen()
        self.screen.addstr(2, 2, "Please enter a number...")
        self.screen.addstr(4, 4, "1 - Start new task")
        self.screen.addstr(5, 4, "2 - Exit")
        if message:
            self.screen.addstr(7, 2, message)
        self.screen.refresh()

    def exit(self):
        curses.echo()
        curses.nocbreak()
        curses.endwin()
