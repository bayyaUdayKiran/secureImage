#!/usr/bin/python3
import os
from cryptography.fernet import Fernet


#Error check..
with open("stat.st", "rb") as state:
    stat = state.read()
if (stat == b'encrypted'):
    #Files to be decrypted...
    files = []
    for file in os.listdir():
        if ((file != "encrypt.py")and(file != "theKey.key")and(file != "decrypt.py")and(file != "main.py")and(file!="stat.st")and(file!="requirements.txt")):
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

    #Updating stat file..
    with open("stat.st", "wb") as stat:
        stat.write(b'decrypted')

    print("Files at the location " + os.getcwd() + " are decrypted..!")


else:
    print("Files at " + os.getcwd() + " are unable to decrypt, make sure that they are'nt already decrypted or unencrypted.")