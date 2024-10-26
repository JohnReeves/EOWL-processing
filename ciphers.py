import tkinter as tk
from tkinter import filedialog, messagebox
import argparse
import string
import cmd
import os


class SubstitutionCipher:
    def __init__(self, cipher_type='affine', a=5, b=8):
        self.cipher_type = cipher_type
        self.a = a  # Multiplier for Affine Cipher
        self.b = b  # Shift for both Affine and Caesar Ciphers
        self.alphabet = string.ascii_uppercase
        self.precomputed_alphabets = self.precompute_all_substitution_alphabets()

    def create_substitution_alphabet(self):
        if self.cipher_type == 'caesar':
            shifted_alphabet = self.alphabet[self.b:] + self.alphabet[:self.b]
        elif self.cipher_type == 'affine':
            shifted_alphabet = ''.join(self.alphabet[(self.a * i + self.b) % 26] for i in range(26))
        else:
            raise ValueError(f"Unknown cipher type: {self.cipher_type}")
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

    def precompute_all_substitution_alphabets(self):
        """Precompute alphabets for all possible Caesar and Affine ciphers."""
        caesar_alphabets = {b: self._caesar_shift(b) for b in range(26)}
        affine_alphabets = {(a, b): self._affine_shift(a, b) for a in range(1, 26, 2) for b in range(26) if self._gcd(a, 26) == 1}
        return {'caesar': caesar_alphabets, 'affine': affine_alphabets}

    def _caesar_shift(self, b):
        """Helper to calculate Caesar shift alphabet for a given b."""
        return self.alphabet[b:] + self.alphabet[:b]

    def _affine_shift(self, a, b):
        """Helper to calculate Affine shift alphabet for given a and b."""
        return ''.join(self.alphabet[(a * i + b) % 26] for i in range(26))

    def _gcd(self, a, b):
        """Helper to compute the greatest common divisor."""
        while b != 0:
            a, b = b, a % b
        return a

    def brute_force_decode(self, ciphertext):
        """Try all Caesar and Affine cipher parameters to brute-force decode."""
        brute_force_results = {}

        # Try all Caesar shifts
        for b in range(26):
            self.b = b
            decoded_text = self.decode(ciphertext)
            brute_force_results[f"Caesar b={b}"] = decoded_text

        # Try all valid Affine (a, b) pairs
        for a in range(1, 26, 2):
            if self._gcd(a, 26) == 1:
                for b in range(26):
                    self.a = a
                    self.b = b
                    decoded_text = self.decode(ciphertext)
                    brute_force_results[f"Affine a={a} b={b}"] = decoded_text

        return brute_force_results

    def reset_cipher_alphabet(self, cipher_type=None, a=None, b=None):
        """Reset cipher type and parameters."""
        if cipher_type:
            self.cipher_type = cipher_type
        if a is not None:
            self.a = a
        if b is not None:
            self.b = b
        self.precomputed_alphabets = self.precompute_all_substitution_alphabets()


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
            return file.read().replace("\n", "").replace("\r", "").strip().lower()

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


class CipherEditor:
    def __init__(self, cli_instance, txt_content=None):
        self.cli_instance = cli_instance
        self.root = tk.Tk()
        self.root.title("Cipher Editor")
        self.root.minsize(30, 800)

        self.text = tk.Text(self.root, wrap=tk.WORD)
        self.text.pack(expand=True, fill=tk.BOTH)
        
        if txt_content:
            self.text.insert(tk.END, txt_content)
        
        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        load_button = tk.Button(button_frame, text="Load", command=self.load_file)
        save_button = tk.Button(button_frame, text="Save", command=self.save_file)  # Fixed error here
        edit_button = tk.Button(button_frame, text="Reload", command=self.reload_file)

        load_button.pack(side=tk.LEFT)
        save_button.pack(side=tk.LEFT)
        edit_button.pack(side=tk.LEFT)

    def load_file(self):
        """Load a cipher or plaintext file into the text editor."""
        file_path = filedialog.askopenfilename(
            defaultextension=".txt", 
            filetypes=[("TXT Files", "*.txt"), ("All Files", "*.*")]
            )
        if not file_path:
            return
        with open(file_path, 'r') as file:
            content = file.read()
            self.text.delete(1.0, tk.END) 
            self.text.insert(tk.END, content) 
        messagebox.showinfo("Load", f"Loaded {file_path}")

    def save_file(self):
        """Save the current content of the text editor to a file."""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt", 
            filetypes=[("TXT Files", "*.txt"), ("All Files", "*.*")]
            )
        if not file_path:
            return
        try:
            with open(file_path, 'w') as file:
                file.write(self.text.get(1.0, tk.END))  
            messagebox.showinfo("Save", f"Saved to {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save the file: {e}")

    def reload_file(self):
        """Reload the file into the CLI."""
        file_path = filedialog.askopenfilename(
            defaultextension=".txt", 
            filetypes=[("TXT Files", "*.txt"), ("All Files", "*.*")]
            )
        if not file_path:
            return
        self.cli_instance.load_file(file_path)
        messagebox.showinfo("Reload", f"Reloaded {file_path}")

    def run(self):
        self.root.mainloop()


# Helper function to list available cipher challenge files
def list_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.txt')]


class CipherChallengeCLI(cmd.Cmd):
    intro = """
                                Welcome to the cipher challenge CLI
                                ~~~~~~~~~~~~~~~~*@*~~~~~~~~~~~~~~~~
\033[4mUtility commands\033[0m
    list: Displays the available plaintext or cipher files
    load <filname>: Loads the specified plaintext or cipher file
    save <filename>: Saves the plain or cipher text to a file
    edit: Starts the embedded text editor to edit cipher and plain text

\033[4mCipher commands\033[0m
    set_cipher: Sets the cipher type and its parameters
    show_cipher: Displays the current cipher type and its parameters
    switch_cipher: Quickly switches between the available cipher types
    encode / decode: Encodes / decodes a short message
    try_decrypt_sequence: Decodes a file using a sequence of parameter values
    segment: Separates continuous plain text into a sequence of individual words

\033[4mWhile using the cipher challenge CLI\033[0m
    Type 'help' or '?' to list all the available commands
    Type 'help <command>' to get a reminder of <command>'s syntax
    Type 'quit' or 'exit' to exit the program

\033[4mTo solve ciphers with the cipher challenge CLI\033[0m
    Type 'edit' to copy & paste the cipher challenge text to a file in /cipher_challenge/
    Type 'list' to find the file your want to decode or encode
    Type 'load <filename>' to load the file contents into the cipher challenge CLI

A. to decode the cipher text
    Type 'set_cipher' to select caesar or affine cipher
                      and provide the parameters for the chosen cipher
    Type 'decode' to decode the loaded cipher text using the chosen cipher
    Type 'try_decrypt_sequence' to decode the loaded cipher text using a sequence of cipher values
    Type 'bruteforce' to decode the loaded text by iterating through parameters values for the available ciphers

B. to separate the decoded text into proper words
    Type 'segment' or 'segment <filename>' to run the segmentation function
    Type 'edit' or 'edit <filename>' to load the separated words into a text editor 
                                     and manually correct the word separation and save the plaintext

\033[4mMore ciphers will be added over time as the cipher challenge progresses\033[0m 
    """
    prompt = "(cipher) "
    
    def __init__(self, directory):
        super().__init__()
        self.directory = directory
        self.cipher = SubstitutionCipher(cipher_type='caesar', b=3)
        self.segmenter = WordSegmenter("/usr/share/dict/words", "special_words.txt")  
        self.loaded_text = None  # This stores the loaded file content

    def do_list(self, arg):
        """List all available state machine JSON files in the directory."""
        files = list_files(self.directory)
        if files:
            print("Available cipher challenge files:")
            for f in files:
                print(f"  - {f}")
        else:
            print(f"No cipher files in: {self.directory}")

    def do_load(self, arg):
        """Load a text file: load <file_path>"""
        try:
            filename = arg.strip()
            if not filename:
                print("No filename provided. Please provide a valid filename.")
                return

            filepath = os.path.join(self.directory, filename)
            if not os.path.isfile(filepath):
                print(f"File {filename} does not exist in {self.directory}.")
                return

            self.loaded_text = self.segmenter.load_text_from_file(filepath)
            print(f"Loaded file '{filename}' successfully with content:\n{self.loaded_text[:100]}...")
        except Exception as e:
            print(f"Failed to load file: {e}")
    
    def do_save(self, arg):
        """Write the current buffer text to a file in the /cipher_challenge/ sub-directory."""
        if self.loaded_text:
            if not arg:
                print("Please provide a filename to save the text. Usage: write <filename>")
                return

            file_path = os.path.join(self.directory, arg.strip())

            try:
                with open(file_path, 'w') as file:
                    file.write(self.loaded_text)
                print(f"Buffer text written to file '{file_path}' successfully.")
            except Exception as e:
                print(f"Error writing to file: {e}")
        else:
            print("No text in buffer to save. Load or decode text first.")

    def do_remove_spaces(self, arg):
        """Remove spaces and punctuation from the loaded text or provided text."""
        text = self.loaded_text or arg
        if text:
            self.loaded_text = text.replace(" ", "").replace(",", "").replace(".", "")
            print(f"Spaces and punctuation removed from loaded text:\n{self.loaded_text[:100]}...")
        else:
            print("No text provided or loaded.")

    def do_edit(self, arg):
        """Open the editor to edit the buffer content or load a file."""
        if self.loaded_text:
            if arg:
                file_path = os.path.join(self.directory, arg.strip())
                if not os.path.isfile(file_path):
                    print(f"File {arg} does not exist in {self.directory}.")
                    return
                try:                
                    with open(file_path, 'r') as file:
                        file_content = file.read()
                    editor = CipherEditor(self, file_content)
                except Exception as e:
                    print(f"Error accessing file: {e}")                    
            else:
                buffer_content = self.loaded_text if self.loaded_text else "" 

                editor = CipherEditor(self, buffer_content)
            editor.run()
        else:
            print("No text in buffer to write. Load or decode text first.")
           
    def do_set_cipher(self, arg):
        """Set the cipher type and parameters: set_cipher caesar b=<shift> OR set_cipher affine a=<multiplier> b=<shift>
        """
        try:
            args = arg.split()
            cipher_type = args[0].lower()
            params = {k: int(v) for k, v in (x.split('=') for x in args[1:])}

            if cipher_type == 'caesar':
                self.cipher = SubstitutionCipher(cipher_type='caesar', b=params.get('b', 3))
            elif cipher_type == 'affine':
                self.cipher = SubstitutionCipher(cipher_type='affine', a=params.get('a', 5), b=params.get('b', 8))
            else:
                print(f"Unknown cipher type: {cipher_type}")
        except (IndexError, ValueError):
            print("Invalid parameters. Usage: set_cipher caesar b=<shift> OR set_cipher affine a=<multiplier> b=<shift>")

    def do_switch_cipher(self, arg):
        """Quickly switch between cipher types: caesar, affine: switch_cipher <cipher_type>
        """
        cipher_type = arg.strip().lower()
        if cipher_type == 'caesar':
            self.cipher.reset_cipher_alphabet(cipher_type='caesar', b=3)  # Default Caesar
        elif cipher_type == 'affine':
            self.cipher.reset_cipher_alphabet(cipher_type='affine', a=5, b=8)  # Default Affine
        else:
            print(f"Unknown cipher type: {cipher_type}")
            return
        print(f"Switched to {cipher_type} cipher. Current parameters: a={self.cipher.a}, b={self.cipher.b}")

    def do_show_cipher(self, arg):
        """Display the current cipher state and parameters.
        """
        current_alphabet = self.cipher.create_substitution_alphabet()
        print(f"Current cipher type: {self.cipher.cipher_type}")
        print(f"Parameters: a={self.cipher.a}, b={self.cipher.b}")
        print(f"Substitution alphabet: {''.join(current_alphabet.values())}")

    def do_show_text(self, arg):
        """Display a snippet of the current text buffer.
        """
        if not self.loaded_text:
            print("No text loaded in buffer.")
            return
        print(f"Current loaded text: {self.loaded_text[:100]}...")

    def do_precompute(self, arg):
        """Precompute all substitution alphabets."""
        self.cipher.precompute_all_substitution_alphabets()
        print("Precomputed all substitution alphabets.")

    def do_bruteforce(self, arg):
        """Perform brute-force decryption on the loaded text."""
        if not self.loaded_text:
            print("No text loaded to brute-force decode.")
            return

        results = self.cipher.brute_force_decode(self.loaded_text)
        for params, decoded_text in results.items():
            print(f"Using {params}: {decoded_text[:50]}...")

    def do_reset(self, arg):
        """Reset the cipher type and parameters."""
        args = arg.split()
        cipher_type = args[0] if args else None
        a = int(args[1]) if len(args) > 1 else None
        b = int(args[2]) if len(args) > 2 else None
        self.cipher.reset_cipher_alphabet(cipher_type, a, b)
        print(f"Cipher reset to type: {self.cipher.cipher_type}, a={self.cipher.a}, b={self.cipher.b}")

    def do_encode(self, arg):
        "Encode a message: encode <message>"
        text = arg or self.loaded_text
        if text:
            encoded = self.cipher.encoded(text)
            print(f"Decoded message:\n{encoded[:100]}...")
        else:
            print("No text provided or loaded. Use 'decode <message>' or 'load_file <file_path>'.")

    def do_decode(self, arg):
        "Decode a message: decode <message>"
        text = arg or self.loaded_text
        if text:
            decoded = self.cipher.decode(text)
            self.loaded_text = decoded.lower()
            print(f"Decoded message:\n{self.loaded_text[:100]}...")
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

            #print(f"Attempting decryption with parameters: {params}")
            decoded = self.cipher.decode(self.loaded_text[:100])
            print(f"Decrypted text with parameters {params}: {decoded}")

    def do_segment(self, arg):
        "Segment text: segment <file_path or loaded text>"
        text = self.loaded_text or arg
        if text:
            segmented_words = self.segmenter.word_segmentation(text)
            if segmented_words:
                segmented_text = ' '.join(segmented_words)
                self.loaded_text = segmented_text

                print(f"{len(segmented_words)} words found (with special words priority)\n {segmented_text[:100]}...")
            else:
                print("No valid segmentation found.")
        else:
            print("No text provided or loaded. Use 'segment <file_path>' or 'load <file_path>'.")

    def do_exit(self, arg):
        "Exit the program"
        print("Exiting...")
        return True

    def do_quit(self, arg):
        """Quit the cipher CLI."""
        print("Goodbye!")
        return True


def parse_args_and_run_cli():
    parser = argparse.ArgumentParser(description="Run the cipher challenge CLI to interactively decrypt those messages.")
    
    parser.add_argument(
        "--directory",
        type=str,
        default="./cipher_challenge/",
        help="Directory where the cipher challenge files are stored. Default is './cipher challenge/'"
    )
    
    args = parser.parse_args()

    cli = CipherChallengeCLI(args.directory)
    cli.cmdloop()

if __name__ == "__main__":
    parse_args_and_run_cli()
