import SearchEngine.Classes.Path as Path
import re
# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
class WordTokenizer:

    def __init__(self, content):
        # Tokenize the input texts.
        self.words_list = list(filter(lambda v: v != '', re.findall("[a-zA-Z]*", content)))  # Use regular expression to get words and filter empty strings
        self.idx = -1
        self.length = len(self.words_list)

    def nextWord(self):
        # Return the next word in the document.
        # Return null, if it is the end of the document.
        self.idx += 1
        return None if self.idx >= self.length else self.words_list[self.idx]  # Return None if reaching the end of the list