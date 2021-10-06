from pynput import keyboard
from screenshot_tools import notify, upload_screenshot

class ListenerException(Exception): pass

class ScreenshotListener:
    """Basically a wrapper class for pynput.keyboard.Listener.
    
    On setup, a pynput.Keyboard.Listener object is set to listen for the hotkey
    combination <Ctrl>+<PrnSc>. When the hotkey is pressed, the user-provided
    callable is called.

    To use:
    >>> l = ScreenshotListener(callable_f)
    >>> l.setup()
    >>> l.start()
    """
    def __init__(self):
        self.listener = None
        self.action = None
        self.sc_stack = []

    def _on_activate(self) -> None:
        screenshot = self.action()
        self.sc_stack.append(screenshot)
        print('Hotkey: <ctrl><prtsc> pressed.')

    def _for_canonical(self, f):
        return lambda k: f(self.listener.canonical(k))

    def setup(self, action) -> None:
        hotkey = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+<print_screen>'), self._on_activate)

        if self.listener and self.listener.running:
            self.listener.stop()
        self.listener = keyboard.Listener(on_press=self._for_canonical(hotkey.press), on_release=self._for_canonical(hotkey.release))
        self.action = action

    def start(self) -> None:
        if not self.listener.running:
            self.listener.start()
        else:
            print('The listener is already running!')

    def stop(self) -> None:
        if self.listener.running:
            self.listener.stop()

    def upload_stack(self) -> None:
        while (len(self.sc_stack)):
            fname = self.sc_stack.pop()
            status_msg = upload_screenshot(fname)
            notify(status_msg)

    def has_uploadable(self) -> bool:
        if len(self.sc_stack):
            return True
        return False