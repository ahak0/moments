from PySimpleGUIQt import SystemTray, DEFAULT_BASE64_ICON
from ScreenshotListener import ScreenshotListener
from screenshot_tools import take_screenshot

def main():
    MENU_LAYOUT = ['BLANK', ['Screenshot (Ctrl + PrtSc)', '&Exit']]
    tray = SystemTray(menu=MENU_LAYOUT, data_base64=DEFAULT_BASE64_ICON)

    scl = ScreenshotListener()
    scl.setup(take_screenshot)
    scl.start()

    while True:  # Main loop to listen for screenshot command
        # The system tray allows for users to manually take a screenshot without
        # inputting the global hotkey command. It also enables the user to exit
        # the program and stop having it listen for the hotkey.
        menu_item = tray.Read()
        if menu_item == 'Exit':
            scl.stop()
            print('Program has been terminated by user from the systray.')
            break
        elif menu_item == 'Screenshot':
            print('screenshot')

if __name__ == '__main__':
    main()