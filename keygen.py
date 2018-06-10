from Crypto.PublicKey import RSA
from Crypto import Random
import hashlib

random_gen = Random.new().read                    # Cryptographically Secure Random Number Generator

new_key = RSA.generate(4096,random_gen,e=65537)   # 4096 Bits Key

private_key = new_key.exportKey('PEM')            # export in PEM Format
public_key = new_key.publickey().exportKey('PEM') 

#print(hashlib.sha256(private_key).hexdigest())   # if you want to check hash of keys to see 
#print(hashlib.sha256(public_key).hexdigest())    # performance of random number generator 

fw = open('private_key.pem','wb')                 
print(private_key.decode('utf-8'))
fw.write(private_key)
fw.close()

fw = open('public_key.pem','wb')
print(public_key.decode('utf-8'))
fw.write(public_key)
fw.close()
