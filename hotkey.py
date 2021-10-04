from pynput import keyboard

def on_activate():
    print('Hotkey: <ctrl><prtsc> pressed.')

"""def for_canonical(f):
    return lambda k: f(l.canonical(k))


hotkey = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+<print_screen>'), on_activate)

with keyboard.Listener(on_press=for_canonical(hotkey.press), on_release=for_canonical(hotkey.release)) as l:
    l.join() """