# The caesar cipher is a shift cipher that uses addition and subtraction to code a message.

try:
    import pyperclip # copies text to the clipboard
except ImportError:
    pass # if pyperclip is not installed, do nothing.

# (!) You can add numbers and punctuation marks to encrypt symbols.

symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("\nWelcome to the caesar cipher.")
print("This algorithm encrypts messages by shifting the letters over by a certain length.")
print("This length is called a key. For example, if the key is three,")
print("then the letter A will be D.\n")

# Ask user: encrypt or decrypt?

while True: # Keep asking until the user enters encrypting or decrypting
    print("Do you want to (encrypt) or (decrypt)?")
    
    response = input('> ').lower()
    
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print("Enter the letter e or d.")

# User enters their choice.

while True: # Keep asking until the user enters something valid
    maxKey = len(symbols) - 1 # if it were 26, it'd be the same.
    print("Please enter the key (0 to {}) to use.".format(maxKey))
    response = input("> ").upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(symbols):
        key = int(response)
        break

# User enters the message to encrypt or decrypt.

print("Enter the message to {}.".format(mode))
message = input("> ")

# Caesar Cipher only works on uppercase letters.

message = message.upper()

# Stores encrypted/decrypted message.

translated = ""

# Encrypt/decrypt each symbol in the message.

for symbol in message:
    if symbol in symbols:
        # Get encrypted/decrypted number for this symbol.
        num = symbols.find(symbol) # Get the number of the symbol
        if mode == "encrypt":
            num += key
        elif mode == "decrypt":
            num -= key
        
        # Handle wrap-around if num is larger than the length of symbols or less than 0.

        if num >= len(symbols):
            num -= len(symbols)
        elif num < 0:
            num += len(symbols)

        # Add encrypted/decrypted number's symbol to translated.
        translated += symbols[num]
    else:
        # Add symbol without encrypting or decrypting.
        translated += symbol

# Display the encrypted/decrypted string to the screen:
print(translated)

try:
    pyperclip.copy(translated)
    print("Full {}ed text copied to clipboard.".format(mode))
except:
    pass # Do nothing if pyperclip is not installed.
            
