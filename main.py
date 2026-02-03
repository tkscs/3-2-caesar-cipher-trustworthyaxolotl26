import string

def hints():
    # ----- Some Hints -----
    # This will give you a string with all the lowercase letters in the alphabet
    alphabet = string.ascii_lowercase
    print(f"{alphabet = }")

    # You can look up the index of a letter in the alphabet like this:
    index = alphabet.index("a")
    print(f"position of 'a' in the alphabet: {index}")

    # The computer already thinks of all the characters it can print out as numbers.
    # If you want to, you can look up what number a character corresponds to in
    # "ASCII" encoding:
    ascii_number = ord("a")
    print(f"ascii number representation of 'a': {ascii_number}")

    ascii_letter = chr(97)
    print(f"ascii letter at position #97: {ascii_letter}")

    print(alphabet[0])

# ----- Your Algorithm -----

def encrypt():
    alphabet = string.ascii_lowercase
    ## Your task is to encrypt this secret message into ciphertext
    plaintext = "the quick brOwn fox jumps OvER THE lazy dOg"
    #plaintext = input("what would you like to encrypt: ")
    ## Initialize your ciphertext an empty string
    ciphertext = ""
    for character in plaintext:
        if character.lower() in alphabet:
            numbers = str(alphabet.index(character.lower()))
            encrypted_character = numbers
        else: 
            encrypted_character = character
        ciphertext += encrypted_character

    print(f"{ciphertext = }")

encrypt()