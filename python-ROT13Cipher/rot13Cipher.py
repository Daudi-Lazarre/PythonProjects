#!/usr/bin/env python3

try:
    import pyperclip
except ImportError:
    pass

# Set up constants
upperLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerLetters = "abcdefghijklmnopqrstuvwxyz"

# main loop
while True:
    print("\nEnter a message to encrypt/decrypt.")
    print("Type 'QUIT' to exit.")

    message = input("> ")

    if message == "QUIT":
        break

    # Rotate 13 spaces.
    translated = ""

    for character in message:
        if character.isupper():
            transCharIndex = (upperLetters.find(character) + 13) % 26
            translated += upperLetters[transCharIndex]
        if character.islower():
            transCharIndex = (lowerLetters.find(character) + 13) % 26
            translated += lowerLetters[transCharIndex]
        else:
            translated += character
            
    # Display translation
    print("\nHere is your translated message: ")
    print(translated)

# Copy the message
    try:
        pyperclip.copy(translated)
    except:
        pass

    print("\nFor your convenience, the message has been copied to your clipboard.")