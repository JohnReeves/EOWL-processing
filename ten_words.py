import zipfile
import io

class EOWLChecker:
    def __init__(self, zip_file_path):
        self.zip_file_path = zip_file_path
        self.zip_file = None
        self.load_zip_file()

    def load_zip_file(self):
        try:
            self.zip_file = zipfile.ZipFile(self.zip_file_path, 'r')
        except zipfile.BadZipFile:
            print("Error: The file is not a valid zip file.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def is_valid_word(self, word):
        if not self.zip_file:
            print("ZIP file could not be opened.")
            return False

        word = word.lower()
        first_letter = word[0].upper()
        file_name = f"{first_letter} Words.txt"

        if file_name not in self.zip_file.namelist():
            print(f"No file found for the letter '{first_letter}'.")
            return False

        try:
            with self.zip_file.open(file_name) as word_list_file:
                words = set(io.TextIOWrapper(word_list_file).read().splitlines())
                return word in words
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def close_zip_file(self):
        if self.zip_file:
            self.zip_file.close()

if __name__ == "__main__":
    eowl_checker = EOWLChecker('EOWL.zip')

    words = ["widget", "zoological", "aardvark", "xerxes", "athena",
             "grommet", "sprocket", "piston", "ada", "lovelace"]

    for input_word in words:
        if eowl_checker.is_valid_word(input_word):
            print(f"'{input_word}' is a valid word in the EOWL.")
        else:
            print(f"'{input_word}' is not a valid word in the EOWL.")

    eowl_checker.close_zip_file()
