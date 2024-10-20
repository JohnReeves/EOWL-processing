import string

def load_dictionary(file_path):
    """return a word dictionary as a set for easy searching"""
    import random
    with open(file_path, 'r') as file:
        valid_words = set(word.strip().lower() for word in file)
        print(next(iter(valid_words)))
    return valid_words

def load_special_words(file_path=None):
    if file_path:
        with open(file_path, 'r') as file:
            special_words = set(word.strip().lower() for word in file)
    else:
        special_words = {"horsley", "ada", "lovelace", "charles", "babbage", "palmerston"}
    return special_words

def word_segmentation_with_special_words(text, valid_words, special_words):
    """
    Segment text into valid words using a dynamic programming approach, prioritizing special words.
    :param text: Continuous text with no spaces.
    :param valid_words: Set of valid English words.
    :param special_words: Set of special words to prioritize.
    :return: Best segmentation as a list of words.
    """
    cleaned_text = ''.join(char for char in text.lower() if char in string.ascii_lowercase)
    n = len(cleaned_text)
    
    dp = [None] * (n + 1)
    dp[0] = [] 

    for i in range(1, n + 1):
        for j in range(i):
            word = cleaned_text[j:i]
            # Prioritize special words
            if word in special_words and dp[j] is not None:
                if dp[i] is None or len(dp[j]) + 1 < len(dp[i]):
                    dp[i] = dp[j] + [word]
            # Then check the general valid words list
            elif word in valid_words and dp[j] is not None:
                if dp[i] is None or len(dp[j]) + 1 < len(dp[i]):
                    dp[i] = dp[j] + [word]

    # dp[n] is None when there is no valid segmentation
    return dp[n] if dp[n] is not None else []

# Load text from file (without spaces or punctuation)
def load_text_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().replace("\n", "").replace("\r", "").strip()

if __name__ == "__main__":
    valid_words = load_dictionary("/usr/share/dict/words") 
    special_words = load_special_words("special_words.txt") 
    sample_text = load_text_from_file("sample_text.txt")

    print(f"Original text:\n{sample_text}")

    segmented_words = word_segmentation_with_special_words(sample_text, valid_words, special_words)
    if segmented_words:
        print("Segmented text:\n", * segmented_words)
        print(f"Total valid words found (with special words priority): {len(segmented_words)}")
    else:
        print("No valid segmentation found.")