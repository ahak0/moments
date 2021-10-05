from gdrive_api_tools import get_authorization, upload_file
from PySimpleGUIQt import SystemTray, DEFAULT_BASE64_ICON
from ScreenshotListener import ScreenshotListener
from screenshot_tools import take_screenshot

def main():
    MENU_LAYOUT = ['BLANK', ['&Screenshot', '&Exit']]
    tray = SystemTray(menu=MENU_LAYOUT, data_base64=DEFAULT_BASE64_ICON)

    scl = ScreenshotListener()
    scl.setup(take_screenshot)
    
    while True:  # Main loop to listen for screenshot command
        # The system tray allows for users to manually take a screenshot without
        # inputting the global hotkey command. It also enables the user to exit
        # the program and stop having it listen for the hotkey.
        menu_item = tray.Read(timeout=0)
        scl.start()
        if menu_item == 'Exit':
            break
        elif menu_item == 'Screenshot':
            print('screenshot')

def upload_screenshot(screenshot) -> None:
    gdrive = get_authorization()
    upload_file(gdrive, screenshot)
    gdrive.close()

if __name__ == '__main__':
    main()