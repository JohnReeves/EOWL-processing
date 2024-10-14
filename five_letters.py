import zipfile

def decode_line(line, encodings=['utf-8', 'latin-1']):
    for encoding in encodings:
        try:
            return line.decode(encoding).strip().lower()
        except UnicodeDecodeError:
            continue
    return None  # If all encoding attempts fail

# Function to load the EOWL word list from a ZIP file with multiple encodings
def load_eowl_word_list(zip_filename):
    word_list = set()
    
    try:
        with zipfile.ZipFile(zip_filename, 'r') as zip_file:
            for file_name in zip_file.namelist():
                with zip_file.open(file_name) as file:
                    for line in file:
                        word = decode_line(line)
                        if word:
                            word_list.add(word)
    except FileNotFoundError:
        print(f"Error: File {zip_filename} not found.")
    
    return word_list


# Function to read a text file
def read_text_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return ""

# Function to save text to a file
def save_text_to_file(text, filename):
    with open(filename, 'w') as file:
        file.write(text)

# Function to split the text into five-letter sequences
def split_into_five_letter_sequences(text):
    text = ''.join(char for char in text if char.isalnum())
    sequences = [text[i:i+5] for i in range(0, len(text), 5)]
    return ' '.join(sequences)

# Function to convert five-letter sequences back to words using the EOWL word list
def convert_sequences_back_to_words(sequences, word_list):
    letters = sequences.replace(" ", "")
    
    def find_words(letters):
        if not letters:
            return []
        
        for i in range(1, min(len(letters), 10) + 1):
            word_candidate = letters[:i]
            if word_candidate.lower() in word_list:
                result = find_words(letters[i:])
                if result is not None:
                    return [word_candidate] + result
        
        return None
    
    words = find_words(letters)
    return ' '.join(words) if words else "No valid words found."

# Main program
def main():
    zip_filename = "Archive.zip"  # Path to the EOWL word list ZIP file
    word_list = load_eowl_word_list(zip_filename)

    if not word_list:
        print("Failed to load word list. Exiting.")
        return
    
    for x in range(10):
        print(word for word in word_list)

    print("Choose an option:")
    print("1. Read from plaintext file and encode to five-letter sequences")
    print("2. Read from encoded file and decode to plaintext")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        input_filename = input("Enter the name of the plaintext file to read: ")
        output_filename = input("Enter the name of the file to save the five-letter sequences: ")
        
        # Read the plaintext file
        plaintext = read_text_from_file(input_filename)
        if plaintext:
            # Convert to five-letter sequences
            encoded_text = split_into_five_letter_sequences(plaintext)
            print("Encoded text:", encoded_text)
            
            # Save the five-letter sequences to a file
            save_text_to_file(encoded_text, output_filename)
            print(f"Five-letter sequences saved to {output_filename}")

    elif choice == "2":
        input_filename = input("Enter the name of the encoded file to read: ")
        output_filename = input("Enter the name of the file to save the decoded plaintext: ")
        
        # Read the encoded file
        encoded_text = read_text_from_file(input_filename)
        if encoded_text:
            # Convert the sequences back to plaintext
            decoded_text = convert_sequences_back_to_words(encoded_text, word_list)
            print("Decoded text:", decoded_text)
            
            # Save the decoded plaintext to a file
            save_text_to_file(decoded_text, output_filename)
            print(f"Decoded plaintext saved to {output_filename}")
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
