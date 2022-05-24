#!/usr/bin/python3
import os
from cryptography.fernet import Fernet

#Files to be decrypted...
files = []
for file in os.listdir():
    if ((file != "encrypt.py")and(file != "theKey.key")and(file != "decrypt.py")and(file != "main.py")):
        if os.path.isfile(file):
            files.append(file)

#Stats of files to be decrypted...
num_of_files = len(files)
status_func = (1/num_of_files)*100
status = 0.0

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
            status+=status_func
            status = round(status, 1)
            if status <= 100:
                print(str(status)+ "% " + "done..")
            else:
                print("100% " + "done..")

print("Files at the location " + os.getcwd() + " are decrypted..!")