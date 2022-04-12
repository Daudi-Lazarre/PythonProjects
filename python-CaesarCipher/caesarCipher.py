#!/usr/bin/env python3

try:
    import pyperclip
except ImportError:
    pass

# Welcome the user.

print("\nHello, hacker...")
print("and welcome to Caesar's Cipher.")
print("This is an ancient form of encryption that has been lost to modern times...")
print("until now.")

# Ask user: encrypt or decrypt?

while True:
    print("\nWould you like to (e)ncrypt or (d)encrypt?")
    response = input("> ").lower()

    if response.startswith("e"):
        mode = "encrypt"
        break
    elif response.startswith("d"):
        mode = "decrypt"
        break
    print("Enter the letter e or d.")

# User enters their choice.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ,.?;:"

while True:
    maxKey = len(letters) - 1
    print("\nPlease enter a key from 0 to {} here: ".format(maxKey))
    response = input("> ").lower()
    
    if not response.isdecimal():
        continue

    if 0 <= int(response) < int(maxKey):
        key = int(response)
        break

# User enters the message to encrypt or decrypt.

print("\nEnter the message to encrypt/decrypt here.")
message = input("> ")

# Caesar Cipher only works on uppercase letters.

message = message.upper()

# Stores encrypted/decrypted message.

translated = "" # empty string to store message

# Encrypt/decrypt each letter in the message.

for letter in message:
    if letter in letters:
    # get the number for the letter
        num = letters.find(letter)
        if mode == "encrypt":
            num += key # Letter's address plus the key for encryption
        elif mode == "decrypt":
            num -= key # Letter's address minus the key for decryption

    # Handle wrap-around if num is less than 0 or bigger than letter length

        if num >= len(letters):
            num -= len(letters)
        elif num < 0:
            num += len(letters)

    # Store encrypted/decrypted number in translated

        translated += letters[num]
    else:
        # Add letter without encrypting or decrypting
        translated += letter    

# Display the encrypted/decrypted string to the screen:
print("\n" + translated)

# Auto copy feature

try:
    pyperclip.copy(translated)
    print("Your {}ed message has been copied to the clipboard.\n".format(mode))
except:
    pass
