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
        print("Specify the key to use...")
        if myMode == "encrypt":
            print(" or enter RANDOM to have one generated for you.")
            response = input("> ").upper()
            if response == "RANDOM":
                myKey = generateRandomKey()
                print("The key is '{}'. KEEP THIS SECRET.".format(myKey))
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
    
    # Display the results
    print("The %sed message is:" % (myMode))
    print(translated)

    try:
        pyperclip.copy(translated)
        print("Full %sed text copied to clipboard." % (myMode))
    except:
        pass # Do nothing if pyperclip is not installed

def checkKey(key):
    """" Return True if key is valid. Otherwise return False."""
    keyList = list(key)
    lettersList = list(letters)
    keyList.sort()
    if keyList!= lettersList:
        print("There is an error in the key or symbol set.")
        return False
    return True

def encryptMessage(message, key):
    """ Encrypt the message using the key."""
    return(translateMessage(message, key, "encrypt"))

def decryptMessage(message, key):
    """ Decrypt the message using the key."""
    return(translateMessage(message, key, "decrypt"))

def translateMessage(message, key, mode):
    """ Encrypt or decrypt the message using the key."""
    translated = ""
    charsA = letters
    charsB = key

    if mode == "decrypt":
        # same code is used for encryption
        # We only have to swap where the letter and key are used.

        charsA, charsB = charsB, charsA

        # Loop through each symbol in the message
        for symbol in message:
            if symbol.upper() in charsA:
                # Encrypt/decrypt the symbol
                symIndex = charsA.find(symbol.upper())
                if symbol.isupper():
                    translated += charsB[symIndex].upper()
                else:
                    translated = charsB[symIndex].lower()
            else:
                # Add symbol unchanged if it is not in letters
                translated += symbol

            return translated

def generateRandomKey():
    """ Generate and return a random encryption key."""
    key = list(letters) # Get a list from the letters string
    random.shuffle(key) # Randomize the list
    return "".join(key) # Get a string from the list

# If this program was run (instead of imported), run the program:
if __name__ == '__main__':
    main()