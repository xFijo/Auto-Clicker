from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import time
import threading
from colorama import init
from colorama import Fore, Style
import os, sys, time, traceback, pickle, random, colorama, crayons

print(crayons.cyan('To use this auto clicker. Press the [S] key to start and the [N] key to stop.'))

startend_key = KeyCode(char='s')
exit = KeyCode(char='n') 
class ClickMouse_Class(threading.Thread):
    def __init__(self):
        super(ClickMouse_Class, self).__init__()
        self.delay = 0.1
        self.button = Button.left
        self.running = False
        self.program_run = True
    def start_clicking(self):
        self.running = True
    def stop_clicking(self):
        self.running = False
    def exit(self):
        self.stop_clicking()
        self.program_run = False
    def run(self):
        while self.program_run:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)
mouse = Controller()
thread = ClickMouse_Class()
thread.start() 
def fn_on_press(key):
    if key == startend_key:
        if thread.running:
            thread.stop_clicking()
        else:
            thread.start_clicking()
    elif key == exit:
        thread.exit()
        listener.stop()
with Listener(on_press=fn_on_press) as listener:
    listener.join() 
