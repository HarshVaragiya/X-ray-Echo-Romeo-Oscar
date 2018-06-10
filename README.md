# X-ray-Echo-Romeo-Oscar
Xero - My Keylogger that implements hybrid cryptosystem to protect logs, and is platform independent.
Still uses Text-book cryptography . 

Go to [usage][] [**remark**][Usage].

# Requirements :
Pycrypto , Pyaes , Pynput libraries 

# Future : 
1. changing from pycrypto to pycryptodome for both RSA And AES implementation and not using pyaes(just)
2. transmitting logs via Sockets , Google Forms , Emails. 
3. upgrade to standard implementations of cryptography(not textbook but deployable system)

# Warning Before Using :
1. This Project/Code/Script is provided "AS IS" Without any warranty 
2. This is done just for Educational/Research Purpose.Full Responsibility is of the user using it.
3. I am not responsible for any harm/problem/issue that may occour, due to use of this code anywhere.

## Usage :
1. Installing Required Python Packages
```bash
pip install pycrypto
pip install pyaes
pip install pyaes
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
