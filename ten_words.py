import zipfile
import io

zip_file_path = 'EOWL.zip'

def read_eowl_wordlist(zip_path):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            file_names = zip_file.namelist()
            with zip_file.open(file_names[0]) as word_list_file:
                words = io.TextIOWrapper(word_list_file).read().splitlines()
                return words

    except zipfile.BadZipFile:
        print("Error: The file is not a valid zip file.")
    except Exception as e:
        print(f"An error occurred: {e}")

words = read_eowl_wordlist(zip_file_path)
if words:
    print("First 10 words in the EOWL word list:")
    print(*words[:10])  # use * to unpack the list