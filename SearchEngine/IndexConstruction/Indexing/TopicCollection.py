import Classes.Path as Path


class TopicCollection:

    def __init__(self, file=Path.TopicDir):
        self.file = open(file, "r", encoding="utf-8")  # Open file and keep file status in Class instance

    def nextTopic(self):
        # 1. When called, this API processes one document from corpus, and returns its doc number and content.
        # 2. When no document left, eturn null, and close the file.
        topic_No = ""
        topic_title = ""
        line_str = self.file.readline()  # Read the first line
        if line_str != '':  # In python, when reaching the end of a file, it will return a "''"(empty string) instead of null in Java

            while line_str != '' and line_str.strip("\n") != "<top>":  # Keeping reading until reaching the sign of "<top>"
                line_str = self.file.readline()

            while line_str != '' and line_str.strip("\n") == "<top>":  # Getting to the starting signal and start to get topic_No
                line_str = self.file.readline()
                topic_No = line_str[13:].strip()

            while line_str != '' and line_str.strip("\n")[:7] != "<title>":  # Keeping reading until reaching the sign of "<title>"
                line_str = self.file.readline()

            while line_str != '' and line_str.strip("\n")[:7] == "<title>":  # Getting to the starting signal and start to get topic_title
                topic_title = line_str[7:].strip()
                line_str = self.file.readline()

            return [topic_No, topic_title]
        self.file.close()
        return None