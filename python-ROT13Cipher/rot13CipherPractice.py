#!/usr/bin/env python3

# This is the simplest encryption program ever!

try:
    import pyperclip
except ImportError:
    pass

# Set up constants

UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"

while True: # main loop
    print("\nEnter a message to encrypt/decrypt.")
    print("Once you have your message, type 'QUIT' to exit.")
    message = input("> ")

    if message.upper() == "QUIT":
        break # break out of the main loop

    # Rotate the key by thirteen spaces.
    translated = ""
    
    for character in message:
        if character.isupper():
            # Copy uppercase translated letter
            transCharIndex = (UPPER_LETTERS.find(character) + 13) % 26
            translated += UPPER_LETTERS[transCharIndex]
        elif character.islower():
            transCharIndex = (LOWERCASE_LETTERS.find(character) + 13) % 26
            translated += LOWERCASE_LETTERS[transCharIndex]
        else:
            # Copy un-translated character
            translated += character

    # Display translation
    print("\nThe translated message is: ")
    print(translated)

    try:
        # Copy the message to clipboard
        pyperclip.copy(translated)
        print("\nCopied to clipboard.")
    except:
        pass
