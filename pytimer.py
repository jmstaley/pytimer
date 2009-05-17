import frontend
import activity

if __name__ == "__main__":
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
            message = "Last activity: %s %s" % (obj.description, obj.duration())
            display.menu(message)
        if x == ord("2"):
            break
    display.exit()

