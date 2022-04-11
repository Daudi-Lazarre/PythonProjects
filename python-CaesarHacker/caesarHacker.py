#!/usr/bin/env python3

# This program hacks messages encrypted with the Caesar Cipher algorithm by doing a brute force attack against every possible key.

# Let the user specify the message to hack.
print("Enter the message you'd like to decrypt:")
message = input("> ")

# Loop thru every possible letter that can be encrypted/decrypted.
# This must watch the letters used when encrypting the message.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ,.?;:"

for key in range(len(letters)): # Loop through every possible key
    translated = "" # empty variable for storage
    
    # Decrypt each symbol in the message.    
    for letter in message: # Key value pair
        if letter in letters:
            num = letters.find(letter) # Get the letter address
            num -= key # Decrypt the number
            
            # Handle the wrap-around if number is less than zero
            if num < 0:
                num += len(letters)

        # Store encrypted number's address
            translated += letter

        # Add letter without decrypting.
        else:
            translated += letter

# Display the key
# Display the decrypted message
    print("\nKey #{}: {}".format(key, translated))