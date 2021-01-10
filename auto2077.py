#!/usr/bin/python3
# encoding=utf-8
import time
from pynput.mouse import Button, Controller
from pynput import keyboard
from threading import Thread

mouse = Controller()

isAuto = False

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    global isAuto
    if key == keyboard.KeyCode.from_char('h'):
        isAuto = True
        print("auto click is started")
    elif key == keyboard.KeyCode.from_char('g'):
        isAuto = False
        print("auto click is stoped")
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# # Collect events until released
# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

def threadfunc( threadName, delay):
    while True:
        if isAuto:
            mouse.press(Button.left)
            time.sleep(1.12)
            mouse.release(Button.left)
        else:
            time.sleep(delay)
 
try:
    t = Thread(target=threadfunc, args=("ThreadAuto",0.5))
    t.start()
except:
    print("Error: unable to start thread")
