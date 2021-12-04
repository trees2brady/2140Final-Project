import SearchEngine.Classes.Path as Path
from nltk import PorterStemmer
# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
class WordNormalizer:

    def __init__(self):
        self.ps = PorterStemmer()  # Instantiate the class to get function to stem

    def lowercase(self, word):
        # Transform the word uppercase characters into lowercase.
        return word.lower() if word is not None else None

    def stem(self, word):
        # Return the stemmed word with Stemmer in Classes package.
        return self.ps.stem(word)