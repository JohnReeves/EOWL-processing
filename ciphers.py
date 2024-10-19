# Define the standard alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
m = len(alphabet)

class SubstitutionCipher:
    def __init__(self, cipher_type, a=None, b=None, shift=None):
        """
        Initializes the cipher with the type of cipher and relevant parameters.
        :param cipher_type: The type of cipher ("affine" or "caesar")
        :param a: Multiplier for the affine cipher
        :param b: Shift for the affine cipher
        :param shift: Shift for the caesar cipher
        """
        self.cipher_type = cipher_type
        if cipher_type == "affine":
            if a is None or b is None:
                raise ValueError("Affine cipher requires both 'a' and 'b' parameters.")
            self.substitution_alphabet = self.generate_affine_alphabet(a, b)
        elif cipher_type == "caesar":
            if shift is None:
                raise ValueError("Caesar cipher requires a 'shift' parameter.")
            self.substitution_alphabet = self.generate_caesar_alphabet(shift)
        else:
            raise ValueError(f"Unsupported cipher type: {cipher_type}")
        
        # Generate substitution dictionaries
        self.substitution_dict = self.generate_substitution_dict(self.substitution_alphabet)
        self.reverse_substitution_dict = self.generate_reverse_substitution_dict(self.substitution_alphabet)

    def generate_affine_alphabet(self, a, b):
        """Generates the substitution alphabet for the affine cipher."""
        substitution_alphabet = ""
        for i in range(m):
            substitution_alphabet += alphabet[(a * i + b) % m]
        return substitution_alphabet

    def generate_caesar_alphabet(self, shift):
        """Generates the substitution alphabet for the caesar cipher."""
        substitution_alphabet = ""
        for i in range(m):
            substitution_alphabet += alphabet[(i + shift) % m]
        return substitution_alphabet

    def generate_substitution_dict(self, substitution_alphabet):
        """Creates a dictionary that maps normal alphabet to substitution alphabet."""
        return dict(zip(alphabet, substitution_alphabet))

    def generate_reverse_substitution_dict(self, substitution_alphabet):
        """Creates a reverse dictionary to map substitution alphabet back to normal alphabet."""
        return dict(zip(substitution_alphabet, alphabet))

    def encode(self, text):
        """Encodes the text using the substitution dictionary."""
        result = ""
        for char in text:
            if char in self.substitution_dict:
                result += self.substitution_dict[char]
            else:
                result += char  # Non-alphabet characters remain unchanged
        return result

    def decode(self, text):
        """Decodes the text using the reverse substitution dictionary."""
        result = ""
        for char in text:
            if char in self.reverse_substitution_dict:
                result += self.reverse_substitution_dict[char]
            else:
                result += char  # Non-alphabet characters remain unchanged
        return result


# --------------------------------
# Example usage
# --------------------------------
if __name__ == "__main__":
    plaintext = "AFFINE CIPHER EXAMPLE"
    
    # Affine Cipher example
    a = 5  # Must be coprime with 26
    b = 8  # Shift value for affine cipher
    affine_cipher = SubstitutionCipher(cipher_type="affine", a=a, b=b)
    affine_encrypted = affine_cipher.encode(plaintext)
    affine_decrypted = affine_cipher.decode(affine_encrypted)
    print("Affine Cipher Encrypted:", affine_encrypted)
    print("Affine Cipher Decrypted:", affine_decrypted)

    # Caesar Cipher example
    shift = 3  # Shift value for Caesar cipher
    caesar_cipher = SubstitutionCipher(cipher_type="caesar", shift=shift)
    caesar_encrypted = caesar_cipher.encode(plaintext)
    caesar_decrypted = caesar_cipher.decode(caesar_encrypted)
    print("Caesar Cipher Encrypted:", caesar_encrypted)
    print("Caesar Cipher Decrypted:", caesar_decrypted)
