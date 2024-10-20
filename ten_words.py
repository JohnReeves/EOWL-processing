import zipfile
import io

zip_file_path = 'EOWL.zip'

def valid_word(word, zip_path):
    try:
        word = word.lower()
        first_letter = word[0].upper()
        file_name = f"{first_letter} Words.txt"

        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            if file_name not in zip_file.namelist():
                print(f"No file found for the letter '{first_letter}'.")
                return False

            with zip_file.open(file_name) as word_list_file:
                words = set(io.TextIOWrapper(word_list_file).read().splitlines())
                return word in words

    except zipfile.BadZipFile:
        print("Error: The file is not a valid zip file.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

input_word = "widget"

words = ["widget", "zoological", "aardvark", "xerxes", "athena"]

for input_word in words:
    if valid_word(input_word, zip_file_path):
        print(f"'{input_word}' is a valid word in the EOWL.")
    else:
        print(f"'{input_word}' is not a valid word in the EOWL.")
