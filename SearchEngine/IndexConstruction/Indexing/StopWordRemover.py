import SearchEngine.Classes.Path as Path

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
class StopWordRemover:

    def __init__(self, file=Path.StopwordDir):
        # Load and store the stop words from the fileinputstream with appropriate data structure.
        # NT: address of stopword.txt is Path.StopwordDir.
        self.stop_words_dict = {}  # Use dictionary to store stopwords since it is fast to search
        with open(file, "r", encoding="utf-8") as f:  # Open file put all stop words into dictionary
            for line in f:
                word = line.strip("\n")
                if not self.stop_words_dict.get(word.strip()):
                    self.stop_words_dict[word] = 1

    def isStopword(self, word):
        # Return true if the input word is a stopword, or false if not.
        return True if self.stop_words_dict.get(word) else False  # Return True if input word is in pre-stored dictionary
