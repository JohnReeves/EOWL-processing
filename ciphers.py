alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
m = len(alphabet) 

# --------------------------------
# encode and decode using a substitution alphabet
# --------------------------------
def encode(text, substitution_alphabet):
    result = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            result += substitution_alphabet[index]
        else:
            result += char  
    return result

def decode(text, substitution_alphabet):
    result = ""
    for char in text:
        if char in substitution_alphabet:
            index = substitution_alphabet.index(char)
            result += alphabet[index]
        else:
            result += char  
    return result

# --------------------------------
# Functions to generate substitution alphabets
# --------------------------------
def generate_affine_alphabet(a, b):
    substitution_alphabet = ""
    for i in range(m):
        substitution_alphabet += alphabet[(a * i + b) % m]
    return substitution_alphabet

def generate_caesar_alphabet(shift):
    substitution_alphabet = ""
    for i in range(m):
        substitution_alphabet += alphabet[(i + shift) % m]
    return substitution_alphabet

# returns a shifting key!
def generate_vigenere_alphabet(key):
    return key 

# --------------------------------
# Vigenère Cipher Functions
# --------------------------------
def vigenere_encode(text, key):
    result = ""
    key_index = 0

    for char in text:
        if char in alphabet:
            x = alphabet.index(char)
            k = alphabet.index(key[key_index % len(key)])
            encrypted_char = alphabet[(x + k) % m]
            result += encrypted_char
            key_index += 1
        else:
            result += char
    return result

def vigenere_decode(text, key):
    result = ""
    key_index = 0

    for char in text:
        if char in alphabet:
            y = alphabet.index(char)
            k = alphabet.index(key[key_index % len(key)])
            decrypted_char = alphabet[(y - k) % m]
            result += decrypted_char
            key_index += 1
        else:
            result += char
    return result

# --------------------------------
# Example usage
# --------------------------------
if __name__ == "__main__":
    plaintext = "AFFINE CIPHER EXAMPLE"
    a = 5  # Must be coprime with 26
    b = 8  # Shift value for affine cipher
    shift = 3  # Shift value for Caesar cipher
    key = "KEY"  # Key for Vigenère cipher (must be uppercase)

    # Affine Cipher
    affine_alphabet = generate_affine_alphabet(a, b)
    affine_encrypted = encode(plaintext, affine_alphabet)
    affine_decrypted = decode(affine_encrypted, affine_alphabet)
    print("Affine Cipher Encrypted:", affine_encrypted)
    print("Affine Cipher Decrypted:", affine_decrypted)

    # Caesar Cipher
    caesar_alphabet = generate_caesar_alphabet(shift)
    caesar_encrypted = encode(plaintext, caesar_alphabet)
    caesar_decrypted = decode(caesar_encrypted, caesar_alphabet)
    print("Caesar Cipher Encrypted:", caesar_encrypted)
    print("Caesar Cipher Decrypted:", caesar_decrypted)

    # Vigenère Cipher (handled dynamically with key)
    vigenere_encrypted = vigenere_encode(plaintext, key)
    vigenere_decrypted = vigenere_decode(vigenere_encrypted, key)
    print("Vigenère Cipher Encrypted:", vigenere_encrypted)
    print("Vigenère Cipher Decrypted:", vigenere_decrypted)
