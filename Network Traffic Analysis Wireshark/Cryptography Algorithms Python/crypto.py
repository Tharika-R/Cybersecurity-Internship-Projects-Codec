# Simple Cryptography Project
# Caesar Cipher + SHA-256 Hashing

import hashlib

# ---------------------------
# PART 1: CAESAR CIPHER
# ---------------------------

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# ---------------------------
# PART 2: SHA-256 HASHING
# ---------------------------

def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

# ---------------------------
# MAIN PROGRAM
# ---------------------------

print("---- Caesar Cipher ----")
message = input("Enter message: ")
shift = int(input("Enter shift value: "))

encrypted = caesar_encrypt(message, shift)
print("Encrypted:", encrypted)

decrypted = caesar_decrypt(encrypted, shift)
print("Decrypted:", decrypted)

print("\n---- SHA-256 Hash ----")
msg = input("Enter text to hash: ")
print("SHA-256:", sha256_hash(msg))
