import frontend
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
            display.add_str('Last activity:', y=7, x=5) 
            display.add_str('Description: %s' % obj.description, y=9, x=6)
            display.add_str('Start: %s' % obj.start.strftime('%d/%m/%Y %H:%M'), 
                            y=10, 
                            x=6)
            display.add_str('End: %s' % obj.end.strftime('%d/%m/%Y %H:%M'), 
                            y=11, 
                            x=6)
            display.screen.refresh()
        if x == ord("2"):
            break
    display.exit()

