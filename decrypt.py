#!/usr/bin/python3
import os
from cryptography.fernet import Fernet

#Files to be decrypted...
files = []
for file in os.listdir():
    if ((file != "encrypt.py")and(file != "theKey.key")and(file != "decrypt.py")and(file != "main.py")):
        if os.path.isfile(file):
            files.append(file)

#The KEY...
with open("theKey.key", "r") as the_key:
    key = the_key.read()

#Decrypting...
for file in files:
    with open(file, "rb") as theFile:
        content = theFile.read()
        decrypted_content = Fernet(key).decrypt(content)
        with open(file, "wb") as theFile:
            theFile.write(decrypted_content)

print("Files at the location " + os.getcwd() + " are decrypted..!")