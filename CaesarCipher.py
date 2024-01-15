import string
def encrypt(text,shiftNum):
    alphabet = string.ascii_lowercase
    alphabet_encrypted  = alphabet[shiftNum:] + alphabet[:shiftNum]
    encrypted = ""

    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            encrypted += alphabet_encrypted[index]
        else:
            encrypted += char
    return encrypted
pass

def decrypt(text,shiftNum):
    alphabet = string.ascii_lowercase
    alphabet_encrypted  = alphabet[-shiftNum:] + alphabet[:-shiftNum]
    encrypted = ""

    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            encrypted += alphabet_encrypted[index]
        else:
            encrypted += char
    return encrypted
pass
