from pynput import keyboard

class ScreenshotListener:

    def __init__(self) -> None:
        self.listener = None

    def on_activate(self):
        print('Hotkey: <ctrl><prtsc> pressed.')

    def for_canonical(self, f):
        return lambda k: f(self.listener.canonical(k))

    hotkey = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+<print_screen>'), on_activate)

    l = keyboard.Listener(on_press=for_canonical(hotkey.press), on_release=for_canonical(hotkey.release))

    print('Starting listener.')
    l.start()

    print('Performing join?')
    l.join()
