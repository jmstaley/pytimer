import frontend_curses as frontend
import activity
import database

if __name__ == "__main__":
    display = frontend.Display()
    display.menu()
    obj = None
    while 1:
        x = display.screen.getch()

        if x == ord('n'):
            description = display.get_param("enter activity description")
            obj = activity.Activity()
            obj.start_activity(description)
            display.show_current(description)
        if x == ord("l"):
            display.list_activities([], schema=['Start', 'End', 'Activity'])
        if x == ord("q"):
            if obj:
                obj.end_activity()
                obj.save()
            break
        if x == ord('f'):
            if obj:
                obj.end_activity()
                obj.save()
                message = "last activity: %s %s" % (obj.description, 
                                                    obj.duration(formatted=True))
            display.menu()
            if obj:
                display.show_last(obj)
            display.screen.refresh()
    display.exit()

