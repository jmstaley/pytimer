import frontend_curses as frontend
import activity
import database

if __name__ == "__main__":
    db = database.Database()
    display = frontend.Display()
    display.menu()
    while 1:
        x = display.screen.getch()

        if x == ord('1'):
            description = display.get_param("Enter activity description")
            obj = activity.Activity()
            obj.start_activity(description)
            display.show_current(description)
        if x == ord('f'):
            obj.end_activity()
            message = "Last activity: %s %s" % (obj.description, 
                                                obj.duration(formatted=True))
            display.menu()
            display.show_last(obj)
            display.screen.refresh()
        if x == ord("2"):
            break
    display.exit()

