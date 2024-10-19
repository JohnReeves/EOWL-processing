import cmd

# Define the standard alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
m = len(alphabet)  # Size of the alphabet (26 for English)

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

class CipherCmd(cmd.Cmd):
    intro = "Welcome to the cipher CLI! Type 'help' or '?' to list commands.\n"
    prompt = "(cipher) "
    
    def __init__(self):
        super().__init__()
        self.cipher = None
        self.plaintext = "AFFINE CIPHER EXAMPLE"  # Default test plaintext

    def do_set_cipher(self, arg):
        """Set the cipher type and its parameters. Usage: set_cipher affine a=5 b=8 | set_cipher caesar shift=3"""
        args = arg.split()
        if len(args) == 0:
            print("Usage: set_cipher <affine/caesar> [params]")
            return

        cipher_type = args[0].lower()

        if cipher_type == "affine":
            try:
                a = int(args[1].split('=')[1])
                b = int(args[2].split('=')[1])
                self.cipher = SubstitutionCipher(cipher_type="affine", a=a, b=b)
                print(f"Affine cipher set with a={a}, b={b}")
            except (IndexError, ValueError):
                print("Usage for affine cipher: set_cipher affine a=<value> b=<value>")
        elif cipher_type == "caesar":
            try:
                shift = int(args[1].split('=')[1])
                self.cipher = SubstitutionCipher(cipher_type="caesar", shift=shift)
                print(f"Caesar cipher set with shift={shift}")
            except (IndexError, ValueError):
                print("Usage for caesar cipher: set_cipher caesar shift=<value>")
        else:
            print(f"Unsupported cipher type: {cipher_type}")

    def do_set_plaintext(self, arg):
        """Set the plaintext for encryption/decryption. Usage: set_plaintext <text>"""
        self.plaintext = arg.upper()
        print(f"Plaintext set to: {self.plaintext}")

    def do_load_plaintext(self, filename):
        """Load plaintext from a file. Usage: load_plaintext <filename>"""
        try:
            with open(filename.strip(), "r") as file:
                self.plaintext = file.read().upper()
                print(f"Plaintext loaded from {filename}:")
                print(self.plaintext)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")

    def do_encrypt(self, arg):
        """Encrypt the current plaintext."""
        if self.cipher is None:
            print("Please set a cipher first using the 'set_cipher' command.")
        else:
            encrypted_text = self.cipher.encode(self.plaintext)
            print(f"Encrypted Text: {encrypted_text}")

    def do_decrypt(self, arg):
        """Decrypt the current ciphertext."""
        if self.cipher is None:
            print("Please set a cipher first using the 'set_cipher' command.")
        else:
            decrypted_text = self.cipher.decode(arg.upper())
            print(f"Decrypted Text: {decrypted_text}")

    def do_quit(self, arg):
        """Quit the cipher CLI."""
        print("Goodbye!")
        return True

if __name__ == "__main__":
    CipherCmd().cmdloop()
