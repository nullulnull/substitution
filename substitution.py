import string

def generate_key():
    original = list(string.ascii_lowercase)
    cipher = original.copy()
    random.shuffle(cipher)
    return dict(zip(original, cipher))

def encrypt_substitution(plaintext, key):
    ciphertext = ""
    for char in plaintext.lower():
        if char in key:
            ciphertext += key[char]
        else:
            ciphertext += char
    return ciphertext

def decrypt_substitution(ciphertext, key):

    reversed_key = {v: k for k, v in key.items()}
    plaintext = ""
    for char in ciphertext:
        if char in reversed_key:
            plaintext += reversed_key[char]
        else:
            plaintext += char
    return plaintext

import random

key = generate_key()

plaintext = input("Enter text to encrypt: ")

ciphertext = encrypt_substitution(plaintext, key)
print("Encrypted text:", ciphertext)

decrypted_text = decrypt_substitution(ciphertext, key)
print("Decrypted text:", decrypted_text)