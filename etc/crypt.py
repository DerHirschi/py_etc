# just Linux - need pycryptodome
# Quelle : https://www.youtube.com/watch?v=G8UmQn9eofI&index=11&list=PLNmsVeXQZj7onbtIXvxZTzeKGnzI6NFp_
# The Morpheus Tutorials
from Crypto import Random
from Crypto.Cipher import AES
import hashlib

def pad(string):
    while len(string) % 16 != 0:
        string = string + ' '
    return string

def enc(key, msg):
    iv = Random.new().read(16)
    msg = pad(msg)
    key = hashlib.sha256(str.encode(key))
    cipher = AES.new(key.digest(), AES.MODE_CBC, iv)
    return (cipher.encrypt(msg), iv)

def dec(key, ci_txt, iv):
    key     = hashlib.sha256(str.encode(key))
    cipher  = AES.new(key.digest(), AES.MODE_CBC, iv)
    return cipher.decrypt(ci_txt)
