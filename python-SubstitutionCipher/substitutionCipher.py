#!/usr/bin/env python3

import random

try:
    import pyperclip
except ImportError:
    pass

# All letters can be encrypted.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    # Let the user specify enc/dec
    while True:
        print("Would you like to (e)ncrypt or (d)ecrypt?")
        response = input("> ").lower()
        
        if response.startswith("e"):
            myMode = "encrypt"
            break

        elif response.startswith("d"):
            myMode = "decrypt"
            break
        print("Please enter the letter e or d.")
        
    # Let the user enter the key to use.
    while True: # Keep asking the user to enter a valid key
        print("Specify the key to use.")
        if myMode == "encrypt":
            print("... or enter RANDOM to have one generated for you.")
            response = input("> ").upper()
            if response == "RANDOM":
                myKey = generateRandomKey()
                print("The key is {}. KEEP THIS SECRET.".format(myKey))
                break
            else:
                if checkKey(response):
                    myKey = response
                    break
    
    # Let the user enter the message to encrypt/decrypt.
    print("Enter the message to {}.".format(myMode))
    myMessage = input("> ")

    # Perform encryption/decryption
    if myMode == "encrypt":
        translated = encryptMessage(myMessage, myKey)
    elif myMode == "decrypt":
        translated = decryptMessage(myMessage, myKey)
    #### CODE YELLOW
    
    # Display the results
    print("The %sed message is:" % (myMode))
    print(translated)

    try:
        pyperclip.copy(translated)
        print("Full %sed text sopied to clipboard." % (myMode))
    except:
        pass # Do nothing if pyperclip is not installed

def checkKey(key):
    """" Return True if key is valid. Otherwise return False."""
    keyList = list(key)
    letterslist = list(LETTERS)
    keylist.sort()
