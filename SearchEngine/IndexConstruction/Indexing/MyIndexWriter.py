import SearchEngine.Classes.Path as Path
from whoosh import index
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.analysis import RegexTokenizer
import os

class MyIndexWriter:

    writer = []

    def __init__(self):
        schema = Schema(nct_id=ID(stored=True),
                        official_title=TEXT(analyzer=RegexTokenizer(), stored=True),
                        breif_summary=TEXT(analyzer=RegexTokenizer(), stored=True),
                        criteia=TEXT(analyzer=RegexTokenizer(), stored=True),
                        detailed_description=TEXT(analyzer=RegexTokenizer(), stored=True))

        if not os.path.exists(Path.IndexTextDir):
            os.mkdir(Path.IndexTextDir)

        if not os.path.exists(Path.OriginalFilePath):
            os.mkdir(Path.OriginalFilePath)

        indexing = index.create_in(Path.IndexTextDir, schema)

        self.writer = indexing.writer()

    def index(self, fields_dict):
        self.writer.add_document(nct_id=fields_dict["nct_id"],
                                 official_title=fields_dict["official_title"],
                                 breif_summary=fields_dict["breif_summary"],
                                 criteia=fields_dict["criteia"],
                                 detailed_description=fields_dict["detailed_description"])
        return

    # Close the index writer, and output all the buffered content (if any).
    def close(self):
        self.writer.commit()
        return
