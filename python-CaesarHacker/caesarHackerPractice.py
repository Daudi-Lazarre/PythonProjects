#!/usr/bin/env python3

# This program hacks messages encrypted with the Caesar Cipher algorithm by doing a brute force attack against every possible key.

# Let the user specify the message to hack.

print("Enter the encrypted Caesar cipher message to hack.")
message = input("> ")

# Every possible symbol that can be encrypted/decrypted.
# This must watch the letters used when encrypting the message.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ,.?;:"

for key in range(len(letters)): # Loop through every possible key
    translated = "" # empty variable for storage

    # Decrypt each symbol in the message.
    for letter in message: # key value pair
        if letter in letters:
            num = letters.find(letter) # Get the letter address
            num -= key # Decrypt the number

            # Handle the wrap-around if num is less than 0.
            if num < 0:
                num += len(letters)

            # Store decrypted number's address
            translated += letters[num] 
        else:
            # Add the letter without decrypting.
            translated += letter

    # Display the key being tested
    # Display the decrypted text.
    print("Key #{}: {}".format(key, translated))