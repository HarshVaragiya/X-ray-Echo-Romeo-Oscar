# X-ray-Echo-Romeo-Oscar
Xero - My Keylogger that implements hybrid cryptosystem to protect logs, and is platform independent.
Still uses Text-book cryptography.It generates 256Bit AES Key for Encrypting logs and secures the AES Key with a 4096 Bits RSA Encryption. so to Decrypt all logs, we need Private Key,Encrypted Logs,RSA-Encrypted-AES-KeyFile and we can get the logs.
The important thing is,the Private Key,Even if the Encrypted logs and RSA-Encrypted-AES-KeyFile are stored on the host computer,Logs cannot be recovered without the Private Key which is Safe, as it is not used anywhere.It does not require root or administrative access to track the keystrokes of the current user. Hence it works on Windows Systems on non-administrator accounts ann linux on non root users too.

# Crypto-Structure
## While Encrypting:
1. Keys are Detected and logs are in form of string in plaintext
2. A Random 256Bit AES Key is generated and a AES Object is Created
3. The RSA Public Key is used to Encrypt the AES Key, and the encrypted key is then exported 
4. The plaintext logs are encoded(utf-8 encoding) and Encrypted using the AES Object
5. The Logging Goes onn.!
## While Decrypting:
1. The RSA Priavte key object is made that can be used to decrypt AES Keyfile to get AES Key back
2. AES-key is recovered using RSA Decryption using private key from the AES-Key-File
3. AES Object is made using the recovered AES Key,and it can be used to decrypt Data Encrypted using same key
4. The Encrypted Logs are Loaded,and decoded into memory and the AES Object is used to decrypt the Data
5. Logs are printed in any way wanted!

# Requirements :
Pycryptodome or pycrypto(not recommended) , Pyaes , Pynput libraries 

# Future : 
1. changing from pycrypto to pycryptodome for both RSA And AES implementation and not using pyaes(just)
2. transmitting logs via Sockets , Google Forms , Emails. 
3. upgrade to standard implementations of cryptography(not textbook but deployable system)

# Warning Before Using :
1. This Project/Code/Script is provided "AS IS" Without any warranty 
2. This is done just for Educational/Research Purpose.Full Responsibility is of the user using it.
3. I am not responsible for any harm/problem/issue that may occour, due to use of this code anywhere.

# Usage :
1. Installing Required Python Packages
```bash
pip install pycryptodome
pip install pyaes
pip install pynput
```
2. Record Keylogs using WatchDog.py

```bash
python3 WatchDog.py
```
3. Logs Will be Stored in Logfile and the Encrypted key will be stored in AESKey.bin (Defaults)
4. To Decrypt the logs (Assuming you have the ight RSA Key Pair):
```bash
python3 BaseServer.py 
```

# Generate a new RSA Key-Pair for the System:
1. Run Keygen.py to generate new, secure RSA Keys
```bash
python3 keygen.py
```
2. Copy the private_key.pem file to same directory as BaseServer.py and inject public_key.pem key to either WatchDog.py source or other method of public key injection.

3. Test The Configuration. if Everything Works, you should be able to decrypt the AES Key and Get all the logs correctly!
4. Cheers!
