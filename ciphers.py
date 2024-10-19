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
                result += char  
        return result

    def decode(self, text):
        """Decodes the text using the reverse substitution dictionary."""
        result = ""
        for char in text:
            if char in self.reverse_substitution_dict:
                result += self.reverse_substitution_dict[char]
            else:
                result += char  
        return result


def read_plaintext_from_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read().upper()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None


if __name__ == "__main__":
    default_plaintext = "AFFINE CIPHER EXAMPLE"

    user_choice = input("Would you like to input plaintext from a file? (y/n): ").strip().lower()
    if user_choice == 'y':
        filename = input("Enter the filename: ").strip()
        plaintext = read_plaintext_from_file(filename)
        if plaintext is None:
            print("Using default plaintext for testing.")
            plaintext = default_plaintext
    else:
        plaintext = default_plaintext

    print(f"Plaintext: {plaintext}")

    cipher_type = input("Choose cipher type (affine/caesar): ").strip().lower()

    if cipher_type == "affine":
        a = int(input("Enter multiplier 'a' for affine cipher (must be coprime with 26): "))
        b = int(input("Enter shift 'b' for affine cipher: "))
        cipher = SubstitutionCipher(cipher_type="affine", a=a, b=b)
    elif cipher_type == "caesar":
        shift = int(input("Enter shift for Caesar cipher: "))
        cipher = SubstitutionCipher(cipher_type="caesar", shift=shift)
    else:
        print("Invalid cipher type. Exiting.")
        exit(1)

    encrypted_text = cipher.encode(plaintext)
    print(f"Encrypted Text: {encrypted_text}")

    decrypted_text = cipher.decode(encrypted_text)
    print(f"Decrypted Text: {decrypted_text}")
