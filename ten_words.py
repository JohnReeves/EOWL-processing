import string

class WordSegmenter:
    def __init__(self, dictionary_path, special_words_path=None):
        """
        Initialize the WordSegmenter class.
        :param dictionary_path: Path to the general dictionary file.
        :param special_words_path: Path to the special words file (optional). If not provided, uses a hardcoded list.
        """
        self.valid_words = self.load_dictionary(dictionary_path)
        self.special_words = self.load_special_words(special_words_path)

    def load_dictionary(self, file_path):
        """A set of valid English words from a dictionary file"""
        with open(file_path, 'r') as file:
            valid_words = set(word.strip().lower() for word in file)
        return valid_words

    def load_special_words(self, file_path=None):
        """A set of special words either from a file or as a hardcoded list"""
        if file_path:
            with open(file_path, 'r') as file:
                special_words = set(word.strip().lower() for word in file)
        else:
            special_words = {"horsley", "ada", "lovelace", "charles", "babbage", "palmerston"}
        return special_words

    def load_text_from_file(self, file_path):
        """A continuous string of text from a file without spaces or punctuation"""
        with open(file_path, 'r') as file:
            return file.read().replace("\n", "").replace("\r", "").strip()

    def word_segmentation(self, text):
        """Separate text into valid words using a dynamic programming approach, prioritizing special words"""
        cleaned_text = ''.join(char for char in text.lower() if char in string.ascii_lowercase)
        n = len(cleaned_text)

        dp = [None] * (n + 1)
        dp[0] = []

        for i in range(1, n + 1):
            for j in range(i):
                word = cleaned_text[j:i]
                # Prioritize special words list
                if word in self.special_words and dp[j] is not None:
                    if dp[i] is None or len(dp[j]) + 1 < len(dp[i]):
                        dp[i] = dp[j] + [word]
                # Then check the general words list
                elif word in self.valid_words and dp[j] is not None:
                    if dp[i] is None or len(dp[j]) + 1 < len(dp[i]):
                        dp[i] = dp[j] + [word]

        # 'dp[n] is None' means no valid segmentation was found
        return dp[n] if dp[n] is not None else []

# Example usage:
if __name__ == "__main__":
    general_dictionary = "/usr/share/dict/words"
    special_words = "special_words.txt"

    segmenter = WordSegmenter(general_dictionary, special_words)

    sample_text = segmenter.load_text_from_file("sample_text.txt") 
    print(f"Original Text:\n{sample_text}\n")

    segmented_words = segmenter.word_segmentation(sample_text)
    if segmented_words:
        print("Separated text:", * segmented_words)
        print(f"\nNumber of valid words: {len(segmented_words)}")
    else:
        print("No valid segmentation found.")