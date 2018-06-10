#/usr/bin/python3

# Warning Before Using :
# 1. This Project/Code/Script is provided "AS IS" Without any warranty 
# 2. This is done for Educational/Research Purpose ONLY.Full Responsibility is of the user using it.
# 3. I am not responsible for any harm/problem/issue that may occour, due to use of this code anywhere.
# Author : xtreme.reseach@gmail.com

# The Keygen is provided to generate Cryptographically secure RSA Key Pairs 
# For use in the given code example

from Crypto.PublicKey import RSA                  # RSA from pycrypto 
from Crypto import Random                         # Random Number Generator
import hashlib                                    # Optional, To compare hashes of generated keys

random_gen = Random.new().read                    # Cryptographically Secure Random Number Generator

new_key = RSA.generate(4096,random_gen,e=65537)   # 4096 Bits Key

private_key = new_key.exportKey('PEM')            # export in PEM Format
public_key = new_key.publickey().exportKey('PEM')  

#print(hashlib.sha256(private_key).hexdigest())   # if you want to check hash of keys to see 
#print(hashlib.sha256(public_key).hexdigest())    # performance of random number generator 

fw = open('private_key.pem','wb')                 # Write the private Key to a file
print(private_key.decode('utf-8'))
fw.write(private_key)
fw.close()

fw = open('public_key.pem','wb')                  # Write the public key to a file 
print(public_key.decode('utf-8'))
fw.write(public_key)
fw.close()
