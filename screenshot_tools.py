"""Utilities to construct a proper screenshot image file."""
import pyautogui
from datetime import datetime
from win32gui import GetWindowText, GetForegroundWindow
from win32api import GetSystemMetrics
from gdrive_api_tools import get_authorization, upload_file
from PySimpleGUI import SystemTray

def take_screenshot() -> None:
    """Takes a screenshot of the current active window."""
    fname = build_filename()
    img = pyautogui.screenshot()
    img.save(fname, 'PNG')
    #status_msg = upload_screenshot(fname)
    notify(status_msg)

def upload_screenshot(screenshot : str) -> str:
    gdrive = get_authorization()
    status_msg = upload_file(gdrive, screenshot)
    gdrive.close()

    return status_msg

def notify(msg : str) -> None:
    """Notifies the user of the success or failure of uploading the screenshot.
    """
    DURATION = 1000  # In milliseconds.
    FADE_IN = 125
    # We're placing the notification in a set spot relative to resolution.
    width = int(GetSystemMetrics(0) * .8)
    height = int(GetSystemMetrics(1) * .9)

    SystemTray.notify('Moments', msg, alpha=1, location=(width, height), display_duration_in_ms=DURATION, fade_in_duration=FADE_IN)

def build_filename() -> str:
    """Generates a naming convention for screenshot files."""
    application_name = GetWindowText(GetForegroundWindow()).split(' - ')[-1]
    if not application_name or application_name == '':
        # Maybe means the user screenshotted the desktop.
        application_name = 'Desktop'
    dt_format = '%y-%m-%d_%H-%M-%S'
    current_time = datetime.now().strftime(dt_format)
    return '%s %s.png' % (application_name, current_time)