"""Utilities to construct a proper screenshot image file."""
import pyautogui
from datetime import datetime
from win32gui import GetWindowText, GetForegroundWindow

def take_screenshot() -> None:
    """Takes a screenshot of the current active window."""
    fname = build_filename()
    img = pyautogui.screenshot()
    img.save(fname, 'PNG')

def build_filename() -> str:
    """Generates a naming convention for screenshot files."""
    application_name = GetWindowText(GetForegroundWindow()).split(' - ')[-1]
    dt_format = '%y-%m-%d_%H-%M-%S'
    current_time = datetime.now().strftime(dt_format)
    return '%s %s.png' % (application_name, current_time)