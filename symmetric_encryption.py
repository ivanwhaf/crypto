from Crypto.Cipher import DES
from Crypto.Cipher import AES

s='fuck you'
key=b'12345678'
des=DES.new(key,DES.MODE_ECB)
enc=des.encrypt(s.encode())
print(enc)