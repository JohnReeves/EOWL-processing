alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
m = len(alphabet)

# calculate the modular inverse of 'a' modulo 'm' 
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

# --------------------------------
# Affine Cipher Functions
# --------------------------------
def affine_encrypt(text, a, b):
    result = ""
    for char in text:
        if char in alphabet:
            x = alphabet.index(char)
            encrypted_char = (a * x + b) % m
            result += alphabet[encrypted_char]
        else:
            result += char
    return result

def affine_decrypt(text, a, b):
    result = ""
    a_inv = mod_inverse(a, m)
    if a_inv is None:
        raise ValueError(f"No modular inverse for a={a}, m={m}")

    for char in text:
        if char in alphabet:
            y = alphabet.index(char)
            decrypted_char = (a_inv * (y - b)) % m
            result += alphabet[decrypted_char]
        else:
            result += char
    return result

# --------------------------------
# Caesar Cipher Functions
# --------------------------------
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char in alphabet:
            x = alphabet.index(char)
            encrypted_char = (x + shift) % m
            result += alphabet[encrypted_char]
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char in alphabet:
            y = alphabet.index(char)
            decrypted_char = (y - shift) % m
            result += alphabet[decrypted_char]
        else:
            result += char
    return result

# --------------------------------
# Vigenère Cipher Functions
# --------------------------------
def vigenere_encrypt(text, key):
    result = ""
    key_index = 0

    for char in text:
        if char in alphabet:
            x = alphabet.index(char)
            k = alphabet.index(key[key_index % len(key)])
            encrypted_char = (x + k) % m
            result += alphabet[encrypted_char]
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    result = ""
    key_index = 0

    for char in text:
        if char in alphabet:
            y = alphabet.index(char)
            k = alphabet.index(key[key_index % len(key)])
            decrypted_char = (y - k) % m
            result += alphabet[decrypted_char]
            key_index += 1
        else:
            result += char
    return result


if __name__ == "__main__":
    plaintext = "AFFINE CIPHER EXAMPLE"
    a = 5  # Must be coprime with 26
    b = 8  # Shift value for affine cipher
    shift = 3  # Shift value for Caesar cipher
    key = "KEY"  # Key for Vigenère cipher

    # Affine Cipher
    affine_encrypted = affine_encrypt(plaintext, a, b)
    affine_decrypted = affine_decrypt(affine_encrypted, a, b)
    print("Affine Cipher Encrypted:", affine_encrypted)
    print("Affine Cipher Decrypted:", affine_decrypted)

    # Caesar Cipher
    caesar_encrypted = caesar_encrypt(plaintext, shift)
    caesar_decrypted = caesar_decrypt(caesar_encrypted, shift)
    print("Caesar Cipher Encrypted:", caesar_encrypted)
    print("Caesar Cipher Decrypted:", caesar_decrypted)

    # Vigenère Cipher
    vigenere_encrypted = vigenere_encrypt(plaintext, key)
    vigenere_decrypted = vigenere_decrypt(vigenere_encrypted, key)
    print("Vigenère Cipher Encrypted:", vigenere_encrypted)
    print("Vigenère Cipher Decrypted:", vigenere_decrypted)
