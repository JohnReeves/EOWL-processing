#
ver=1.3
print(ver)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
m = len(alphabet) 

def generate_substitution_dict(substitution_alphabet):
    return dict(zip(alphabet, substitution_alphabet))

def generate_reverse_substitution_dict(substitution_alphabet):
    return dict(zip(substitution_alphabet, alphabet))

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

def generate_vigenere_alphabet(key):
    substitution_alphabet = ""
    key = key.upper() 
    for i in range(m):
        shift = alphabet.index(key[i % len(key)]) 
        substitution_alphabet += alphabet[(i + shift) % m] 
    return substitution_alphabet

# --------------------------------
# Generic encode and decode functions
# --------------------------------
def encode(text, substitution_dict):
    result = ""
    for char in text:
        if char in substitution_dict:
            result += substitution_dict[char]
        else:
            result += char 
    return result

def decode(text, reverse_substitution_dict):
    result = ""
    for char in text:
        if char in reverse_substitution_dict:
            result += reverse_substitution_dict[char]
        else:
            result += char
    return result

if __name__ == "__main__":
    plaintext = "AFFINE CIPHER EXAMPLE"
    a = 5  # Must be coprime with 26
    b = 8  # Shift value for affine cipher
    shift = 3  # Shift value for Caesar cipher
    key = "KEY"  # Key for Vigenère cipher (must be uppercase)

    # Affine Cipher
    affine_alphabet = generate_affine_alphabet(a, b)
    affine_substitution_dict = generate_substitution_dict(affine_alphabet)
    affine_reverse_substitution_dict = generate_reverse_substitution_dict(affine_alphabet)
    affine_encrypted = encode(plaintext, affine_substitution_dict)
    affine_decrypted = decode(affine_encrypted, affine_reverse_substitution_dict)
    print("Affine Cipher Encrypted:", affine_encrypted)
    print("Affine Cipher Decrypted:", affine_decrypted)

    # Caesar Cipher
    caesar_alphabet = generate_caesar_alphabet(shift)
    caesar_substitution_dict = generate_substitution_dict(caesar_alphabet)
    caesar_reverse_substitution_dict = generate_reverse_substitution_dict(caesar_alphabet)
    caesar_encrypted = encode(plaintext, caesar_substitution_dict)
    caesar_decrypted = decode(caesar_encrypted, caesar_reverse_substitution_dict)
    print("Caesar Cipher Encrypted:", caesar_encrypted)
    print("Caesar Cipher Decrypted:", caesar_decrypted)

    # Vigenère Cipher
    vigenere_alphabet = generate_vigenere_alphabet(key)
    vigenere_substitution_dict = generate_substitution_dict(vigenere_alphabet)
    vigenere_reverse_substitution_dict = generate_reverse_substitution_dict(vigenere_alphabet)
    vigenere_encrypted = encode(plaintext, vigenere_substitution_dict)
    vigenere_decrypted = decode(vigenere_encrypted, vigenere_reverse_substitution_dict)
    print("Vigenère Cipher Encrypted:", vigenere_encrypted)
    print("Vigenère Cipher Decrypted:", vigenere_decrypted)
