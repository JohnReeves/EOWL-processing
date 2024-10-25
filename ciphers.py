import string
import cmd

class SubstitutionCipher:
    def __init__(self, cipher_type='affine', a=5, b=8):
        self.cipher_type = cipher_type
        self.a = a  # Multiplier for Affine Cipher
        self.b = b  # Shift for both Affine and Caesar Ciphers
        self.alphabet = string.ascii_uppercase

    def create_substitution_alphabet(self):
        if self.cipher_type == 'caesar':
            shifted_alphabet = self.alphabet[self.b:] + self.alphabet[:self.b]
        elif self.cipher_type == 'affine':
            shifted_alphabet = ''.join(self.alphabet[(self.a * i + self.b) % 26] for i in range(26))
        else:
            raise ValueError(f"Unknown cipher type: {self.cipher_type}")
        
        # Create a dictionary that maps the normal alphabet to the substitution alphabet
        return dict(zip(self.alphabet, shifted_alphabet))

    def encode(self, plaintext):
        substitution_dict = self.create_substitution_alphabet()
        plaintext = plaintext.upper()
        return ''.join(substitution_dict.get(char, char) for char in plaintext)

    def decode(self, ciphertext):
        substitution_dict = self.create_substitution_alphabet()
        reverse_dict = {v: k for k, v in substitution_dict.items()}
        ciphertext = ciphertext.upper()
        return ''.join(reverse_dict.get(char, char) for char in ciphertext)


class WordSegmenter:
    def __init__(self, dictionary_path, special_words_path=None):
        self.valid_words = self.load_dictionary(dictionary_path)
        self.special_words = self.load_special_words(special_words_path)

    def load_dictionary(self, file_path):
        with open(file_path, 'r') as file:
            valid_words = set(word.strip().lower() for word in file)
        return valid_words

    def load_special_words(self, file_path=None):
        if file_path:
            with open(file_path, 'r') as file:
                special_words = set(word.strip().lower() for word in file)
        else:
            special_words = {"babbage", "lovelace", "palmerstone", "ada", "charles", "lord"}
        return special_words

    def load_text_from_file(self, file_path):
        with open(file_path, 'r') as file:
            return file.read().replace("\n", "").replace("\r", "").strip()

    def word_segmentation(self, text):
        cleaned_text = ''.join(char for char in text.lower() if char in string.ascii_lowercase)
        n = len(cleaned_text)
        dp = [None] * (n + 1)
        dp[0] = []

        for i in range(1, n + 1):
            for j in range(i):
                word = cleaned_text[j:i]
                if word in self.special_words and dp[j] is not None:
                    if dp[i] is None or len(dp[j]) + 1 < len(dp[i]):
                        dp[i] = dp[j] + [word]
                elif word in self.valid_words and dp[j] is not None:
                    if dp[i] is None or len(dp[j]) + 1 < len(dp[i]):
                        dp[i] = dp[j] + [word]

        return dp[n] if dp[n] is not None else []

class CipherCmd(cmd.Cmd):
    intro = """
    
                                Welcome to the cipher challenge CLI
                                ~~~~~~~~~~~~~~~*@*~~~~~~~~~~~~~~

\033[4mUtility commands\033[0m
    list: Displays the available plaintext or cipher files
    load <filname>: Loads the specified plaintext or cipher file
    write <filename>: write the plaintext or cipher to a file
    edit: Use the embedded text editor to edit plaintext
    quit or exit: Exits the CLI.

\033[4mCipher commands\033[0m
    set_cipher: Set the cipher type and its parameters
    encode: Encode a short message
    decode: Deceode a short cipher text
    try_decrypt_sequence: Decodes a file using a sequence of parameter values
    segmentation: Separation of plaintext into individual words
    goto <state>: Sets the current state to the named state

                                Welcome to the cipher challenge CLI
                                ~~~~~~~~~~~~~~~*@*~~~~~~~~~~~~~~

\033[4mWhile using the State Machine CLI\033[0m
    Type 'help' or '?' to list all the available commands
    Type 'help <command>' to get a reminder of <command>'s syntax

    """
    prompt = "(cipher) "
    
    def __init__(self):
        super().__init__()
        self.cipher = SubstitutionCipher(cipher_type='caesar', b=3)
        self.segmenter = WordSegmenter("/usr/share/dict/words", "special_words.txt")  
        self.loaded_text = None  # This stores the loaded file content

    def do_set_cipher(self, arg):
        "Set the cipher type and parameters: caesar b=<shift>, affine a=<multiplier> b=<shift>"
        args = arg.split()
        cipher_type = args[0]
        params = {k: int(v) for k, v in (x.split('=') for x in args[1:])}
        
        if cipher_type == 'caesar':
            self.cipher = SubstitutionCipher(cipher_type='caesar', b=params.get('b', 3))
        elif cipher_type == 'affine':
            self.cipher = SubstitutionCipher(cipher_type='affine', a=params.get('a', 5), b=params.get('b', 8))
        else:
            print(f"Unknown cipher type: {cipher_type}")
    
    def do_encode(self, arg):
        "Encode a message: encode <message>"
        print("Encoded message:", self.cipher.encode(arg))

    def do_decode(self, arg):
        "Decode a message: decode <message>"
        text = arg or self.loaded_text
        if text:
            decoded = self.cipher.decode(text)
            self.loaded_text = decoded  # Update the buffer with the decoded message
            print("Decoded message:", decoded)
        else:
            print("No text provided or loaded. Use 'decode <message>' or 'load_file <file_path>'.")

    def do_try_decrypt_sequence(self, arg):
        """
        Try a sequence of decryption parameters: 
        For Caesar: try_decrypt_sequence b=n,b=m,...
        For Affine: try_decrypt_sequence a=n b=m,a=o b=p,...
        """
        param_sets = arg.split(',')
        if len(param_set) == 0:
            print("Usage: try_decrypt_sequence <caesar/affine> [params]")
            return
        
        for param_set in param_sets:
            params = {k: int(v) for k, v in (x.split('=') for x in param_set.split())}
            cipher_type = params.get('cipher_type', 'caesar')
            if cipher_type == 'caesar':
                self.cipher = SubstitutionCipher(cipher_type='caesar', b=params.get('b', 3))
            elif cipher_type == 'affine':
                self.cipher = SubstitutionCipher(cipher_type='affine', a=params.get('a', 5), b=params.get('b', 8))
            else:
                print(f"Unknown cipher type: {cipher_type}")
                continue

            print(f"Attempting decryption with parameters: {params}")
            decoded = self.cipher.decode(self.loaded_text)
            print(f"Decrypted text with parameters {params}: {decoded}")

    def do_segmentation(self, arg):
        "Segment text: segment <file_path or loaded text>"
        text = self.loaded_text or arg
        if text:
            segmented_words = self.segmenter.word_segmentation(text)
            if segmented_words:
                print("Best segmentation (with special words priority):", *segmented_words)
                print(f"Total valid words found (with special words priority): {len(segmented_words)}")
            else:
                print("No valid segmentation found.")
        else:
            print("No text provided or loaded. Use 'segment <file_path>' or 'load_file <file_path>'.")

    def do_load(self, arg):
        "Load a text file: load_file <file_path>"
        try:
            with open(arg, 'r') as file:
                self.loaded_text = file.read().replace("\n", "").replace("\r", "").strip()
            print(f"File '{arg}' loaded successfully.")
        except FileNotFoundError:
            print(f"File not found: {arg}")

    def do_write(self, arg):
        "Write the current buffer text to a file: write_file <file_path>"
        if self.loaded_text:
            try:
                with open(arg, 'w') as file:
                    file.write(self.loaded_text)
                print(f"Buffer text written to file '{arg}' successfully.")
            except Exception as e:
                print(f"Error writing to file: {e}")
        else:
            print("No text in buffer to write. Load or decode text first.")

    def do_exit(self, arg):
        "Exit the program"
        print("Exiting...")
        return True

    def do_quit(self, arg):
        """Quit the cipher CLI."""
        print("Goodbye!")
        return True

if __name__ == "__main__":
    CipherCmd().cmdloop()
